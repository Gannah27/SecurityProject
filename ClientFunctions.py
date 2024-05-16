from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
import socket, threading
import queue
from RSA import *
from key_management_module import distribute_keys
from block_cipher import *
import queue


class ClientSocket(threading.Thread):
    def __init__(self,type):
        threading.Thread.__init__(self)
        host = 'localhost'
        port = 10000
        self.size = 2048

        self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.csocket.connect((host, port))
        self.type = type
        if self.type == 'recv':
            data = self.csocket.recv(self.size)
            if len(data):
                print('Received:', data.decode('utf-8'))
    def run(self):
        if self.type == 'recv':
            # data = self.csocket.recv(2048)
            # self.item.append(str(data.decode()))
            data = "dummydata"
            while len(data):
                data = self.csocket.recv(2048)
                print("After Decryption: ", self.decrypt_after_recieve(data))
                decrypted_msg = self.decrypt_after_recieve(data)

                # if self.name+" disconnected from chat" == data.decode():
                #     self.item.append(str(data.decode()))
                #     data = ''
                #     print(self.name+" disconnected from chat")
                #     print("QUIT")
                # else:
                self.item.append(str(decrypted_msg))
            # data = self.csocket.recv(2048)
            # decrypted_msg = self.decrypt_after_recieve(data)
            # self.item.append(decrypted_msg)
            self.csocket.close()


    def sendToServer(self, text):
        # Check if text is already encoded
        if not isinstance(text, bytes):
            text = text.encode()
        self.csocket.send(text)

    def decrypt_after_recieve(self,msg):
        if self.encryption == "RSA":
            mess = rsa_decrypt(msg, self.keys["private"])
        else:
            print("Decrypting ", self.encryption, " message")
            mess = decrypt_message(self.encryption, self.keys, self.iv, msg)
            mess = mess.decode('utf-8')
        return mess
    # def recieveFromServer(self):
    #     try:
    #         self.csocket.recv(self.size)
    #
    #     except socket.timeout as e:
    #         err = e.args[0]
    #         if err == 'timed out':
    #             print('recv timed out, retry later')
    #             return ""

class MyGUI(QMainWindow):
    def __init__(self):
        self.ClientSocketRec = ClientSocket('recv')
        self.ClientSocketSend = ClientSocket('send')
        self.ClientSocketSend.start()
        super(MyGUI,self).__init__()
        uic.loadUi("chatgui.ui",self)
        self.show()
        self.Name.setFont(QFont('Arial', 14))
        self.msgBox.setFont(QFont('Arial', 13))
        self.pushButton.clicked.connect(lambda: self.send(self.msg.toPlainText()))
        name = input("Enter your Name: ")
        self.encryption = input("Enter the encryption type: ")
        self.pushButton.setEnabled(True)
        self.msg.setEnabled(True)
        self.name = name
        self.ClientSocketRec.item = self.msgBox
        self.ClientSocketRec.name = self.name
        self.ClientSocketRec.start()
        self.ClientSocketSend.sendToServer(name)
        self.Name.setText(name)
        
        key = distribute_keys('client_keys.txt')
        self.keys=key[self.encryption]
        self.ClientSocketRec.encryption = self.encryption
        
        if self.encryption == "AES":
            self.keys = self.keys[0]
            self.ClientSocketRec.keys = self.keys
            b = str(self.keys[1]).encode()
            # Ensure the byte string is exactly 8 bytes long
            b = b.ljust(16, b'\0')  # pad with zeros if necessary
            b = b[:16]  # truncate to 8 bytes if necessary
            self.iv = b
            self.ClientSocketRec.iv = b
            print(self.keys, self.iv)
            print("AES")
        elif self.encryption == "DES":
            self.keys = self.keys[0]
            self.ClientSocketRec.keys = self.keys
            b = str(self.keys[1]).encode()
            # Ensure the byte string is exactly 8 bytes long
            b = b.ljust(8, b'\0')  # pad with zeros if necessary
            b = b[:8]  # truncate to 8 bytes if necessary
            self.iv = b
            self.ClientSocketRec.iv = b
            print(self.keys, self.iv)
            print("DES")
        
        

    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        self.ClientSocketSend.sendToServer(self.name+": quit")
        self.ClientSocketSend.csocket.close()
        print("Just closed the window!")

    def encrypt_before_send(self, msg):
        if self.encryption == "RSA":
          print("RSA")
          mess= rsa_encrypt(msg,self.keys["public"])
        else:
            mess, _ = encrypt_message(self.encryption, msg, self.keys, self.iv)
        return mess
        
    def send(self, msg):
        if len(msg) > 0:
            print("Sent!")
            Name = self.Name.text()
            msgToSend = Name+": "+msg
            msgToSend = self.encrypt_before_send(msgToSend)
            self.ClientSocketSend.sendToServer(msgToSend)
            # if msgToSend.split(":")[1].replace(" ","") == "quit":
            #     self.ClientSocketSend.csocket.close()
            self.msg.setText('')
        else:
            print("Write a Msg!")
            message = QMessageBox()
            message.setText("Write a msg!")
            message.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = MyGUI()
    app.exec_()

# encrypt the message when send and decrypt when recieved
# take encryption type as input from user


