import pyrebase
import socket



firebaseCon={
  'apiKey': "AIzaSyBygXEE7-GG97RJMNEYBGIuyDN71OBoweo",
  'authDomain': "security-project-78410.firebaseapp.com",
  'projectId': "security-project-78410",
  'storageBucket': "security-project-78410.appspot.com",
  'messagingSenderId': "885154241798",
  'appId': "1:885154241798:web:e6341fb7f9767f45309287",
    'databaseURL':"xx"
}
firebase=pyrebase.initialize_app(firebaseCon)
auth=firebase.auth()

def login():
    print("Log in..")
    email = input("Enter email:")
    password = input("Enter password:")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in")
        return 0
    except:
        print("invalid email or password")
        return 1

def signup():
    print("sign up..")
    email=input("Enter email:")
    password=input("Enter password:")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("account made successfully")
        return 0
    except:
        print("Email already exists")
        return 1

ans= input("Are you a new user?[y/n]")
if __name__ == "__main__":
        if ans =='n':
            while True:
                flag1 = login()
                if (flag1):
                    print("please renter your credentials:")
                    login()
                else:
                    break
        elif ans =='y':
            while True:
                flag1 = signup()
                if(flag1):
                    print("please enter other email:")
                    signup()
                else:
                    break

        # would be server between 2 clients
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12345
        client_socket.connect((host, port))

        msg = client_socket.recv(1024)

       #send to server data
        #receive from server

        client_socket.close()