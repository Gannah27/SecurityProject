import pyrebase

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
    except:
        print("invalid email or password")
    return

def signup():
    print("sign up..")
    email=input("Enter email:")
    password=input("Enter password:")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("account made successfully")
    except:
        print("Email already exists")
    return

ans= input("Are you a new user?[y/n]")

if ans =='n':
    login()
elif ans =='y':
    signup()