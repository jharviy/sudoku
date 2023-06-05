from Crypto.Cipher import AES
from secrets import token_bytes
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def enc_aes(input):

    key = token_bytes(16)   # 128-bit (16x8) random key generator
    with open(input, 'rb') as file:
        file = file.read()

    # AES encryption (from documentation https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce    # nonce for non-deterministic result
    cipherdata, tag = cipher.encrypt_and_digest(file)

    # "input" is object name, get path only (no filename) then change directory
    path = os.path.dirname(input)
    os.chdir(path)

    # "input" is object name, get filename only
    file_name = os.path.basename(input)
    # splits name to ext name (abc.jpg to ["abc","jpg"])
    name = os.path.splitext(file_name)

    # append "enc-" on file_name then write ciphered data
    with open("enc-"+ file_name, 'wb') as enc_file:
        enc_file.write(cipherdata)

    # create key file with appended key, nonce, tag
    with open("key-"+ name[0], 'wb') as key_file:
        key_file.write(key + nonce + tag)

def dec_aes(input, key):
    # separate key, non, and tag from appended key file
    with open(key, 'rb') as keynonce:
        keynonce = keynonce.read()
    key = keynonce[0:16]
    nonce = keynonce[16:32]
    tag = keynonce[32:]

    # AES decryption (from documentation https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)
    with open(input, 'rb') as file:
        file = file.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(file)

    try:
        # verify tag if decryption is valid
        cipher.verify(tag)

        # "input" is object name, get path only (no filename) then change directory
        os.chdir(os.path.dirname(input))
        file_name = os.path.basename(input)

        # append "dec-" on file_name then write deciphered data
        with open("dec-"+ file_name, 'wb') as enc_file:
            enc_file.write(plaintext)
        messagebox.showinfo("Message", "Done Decryption. Message Valid")

    except ValueError:
        messagebox.showinfo("Message", "Message Invalid")

def file_path():
    global file
    file = filedialog.askopenfilename(title="SELECT FILE TO ENCRYPT/DECRYPT")
    #Update label to show chosen file
    file_dir.config(text=file, fg= "black")

def key_path():
    global key
    key = filedialog.askopenfilename(title="SELECT KEY FILE")
    # Update label to show chosen file
    key_dir.config(text=key, fg= "black")

def encrypt_file():
    try:
        enc_aes(file)
        messagebox.showinfo("Message", "Done Encryption. Key File generated")
    except:
        messagebox.showerror("Error", "Pick a file to be Encrypted")

def decrypt_file():
    try:
        dec_aes(file, key)
    except:
        messagebox.showerror("Error", "Pick an encrypted file and key.")

if __name__ == "__main__":

    window = Tk()

    file_button = Button(text="FILE", command=file_path)
    file_button.place(x=15, y=10, height= 25, width=75)

    key_button = Button(text="KEY", command=key_path)
    key_button.place(x=15, y=45, height= 25, width=75)

    enc_button = Button(text="Encode", command=encrypt_file)
    enc_button.place(x=380, y=80, height=25, width=80)

    dec_button = Button(text="Decode", command=decrypt_file)
    dec_button.place(x=470, y=80, height=25, width=80)

    file_dir = Label(window, text="/directory ", borderwidth=5, fg= "gray", bg="white", height=1, width=60)
    file_dir.place(x=100, y=10, height= 25, width=450)

    key_dir = Label(window, text="/key (no key needed if encoding)", borderwidth=5, fg= "gray", bg="white", height=1, width=60)
    key_dir.place(x=100, y=45, height= 25, width=450)

    window.title("jharvi's File Encryptor-Decryptor")
    window.geometry("570x110")
    window.mainloop()

    #pip install pyinstaller
    #pyinstaller --onefile -w --icon wmelon.ico main.py