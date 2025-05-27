from cryptography.fernet import Fernet, InvalidToken
from hashlib import sha256
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64,os,string,random,re,getpass,sys
import tkinter as tk
from tkinter import filedialog
#import os
#import string
#import random
#import re
#import getpass


def passcheck(password):
    if(len(password)<=7):
        return True   
    if(not re.fullmatch("^[a-zA-Z][a-zA-Z0-9@_!#$%^&*<>?~:]*$",password)):
        return True 
    return False

    
def keygen(password):
   
    if(passcheck(password)):
        print("*********************************** \n")
        print("The password must contain 1 number any 1 special character (@ _ ! # $ % ^ & * < > ? ~ : ]*$ ) atleast")
        print("The password is too weak please restart the process")
        print("*********************************** \n")


    kdf=PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt =  base64.urlsafe_b64decode((sha256((password.encode('utf-8'))).hexdigest())[0:16]),
        iterations = 4800,
        )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('ascii')))
    
    with open(str(getpass.getuser()+".key"), 'wb') as keyfile:
        keyfile.write(key)

def restrictedzone(info):
    USER_OS = sys.platform
    danger_roots = {
    "win32": ["c:\\windows","c:\\program files","c:\\program files (x86)","c:\\users","c:\\programdata"],
    "linux": ["/bin", "/sbin", "/usr", "/etc", "/var"],
    "darwin": ["/bin", "/sbin", "/usr", "/etc", "/var", 
                "/System"]}

    # For each system, all paths EQUAL to these are 
    # considered sensitive
    danger_path = {
    "win32": ["c:\\"],
    "linux": ["/"],
    "darwin": ["/"]}

    info = info.lower()

    for root_path in danger_roots[USER_OS]:
        if info.startswith(root_path):
            return True
        
    for root_path in danger_path[USER_OS]:
        if info == root_path:
            return True
        
    return False


def encrypt(info,keyfile):
    if(restrictedzone(info)):
        print("These files cannot be encrypted they are restricted access !!")
        return
    with open(info,'rb') as file:
        original=file.read()

    with open(keyfile,'rb') as kf:
        enckey=kf.read()
    f = Fernet(enckey)
    encrypted=f.encrypt(original)
    
    with open(info,'wb') as encfile:
        encfile.write(encrypted)

def secureDelete(info):
    usrint=input("Are you sure you want to secure delete "+info+" (Y/N) :")
    if(usrint.lower()=='n'):
        return
    if(usrint.lower()=='y'):
        with open(info,'rb') as file:
            original=file.read()
        for x in range(10):
            key=keygen(''.join(random.choices(string.ascii_letters + string.digits,k=10)))
            encrypted=key.encrypt(original)
            with open(info,'wb') as decfile:
                decfile.write(encrypted)
            os.remove(info)
    else:
        print("Wrong input")
    


def decrypt(info,keyfile):

    with open(info,'rb') as file:
        original=file.read()
    with open(keyfile,'rb') as kf:
        deckey=kf.read()
    f = Fernet(deckey)

    encrypted=f.decrypt(original)

    with open(info,'wb') as decfile:
        decfile.write(encrypted)

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
def GUI():
    root=tk.Tk()
    root.title("Encryptonator")
    label1=tk.Label(root,text="Select keyfile")
    label2=tk.Label(root,text="Select file you want to encrypt/decrypt")
    #label1.place(x=50,y=50)
    #label1.grid(row=0,column=0)
    #label2.grid(row=1,column=0,columnspan=4)
    button = tk.Button(root, text='Open', command=UploadAction)
    button.pack()


    root.mainloop()





info='enc.rtf'
key=keygen("Chandana2@")
#GUI()
#secureDelete(info)
#encrypt('test.txt',"chandan.key")
#decrypt('test.txt',"chandan.key")

'''The password has to be 7 charecters long containing words,numbers and symbols'''
'''The encrypt function encrypts the file and decrypt functions decrypts the file'''
'''The restricted zone section checks if the files you are encrypting are not placed in essential system directories'''
'''The keygen function is used to generate the keys'''
'''The passcheck function is used to check if the enterned password is valid or not'''
