
import json
import os

#DECORATOR
def CheckPath(func):                
    def wrapper(self):
        if os.path.exists('users.json'):
            func(self)
        else:
            return False
    return wrapper
#CLASS
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
#CLASS
class UserRepository:
    def __init__(self):
        self.IsLoggedIn = False
        self.users = []
        self.loadusers()
        
    def Register(self,user:User):
        self.users.append(user)
        self.savetofile()
        
    def Login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                print('Loggin Successfull.')
                self.IsLoggedIn == True 
            else:
                print('Access denied !!')

    def Logout(self):
        self.IsLoggedIn = False

    def Identity(self):
        if self.IsLoggedIn:
            print('You are logged in')
        else:
            print('You are not logged in')

    def savetofile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open('users.json','w') as file:
            json.dump(list,file)
   
    @CheckPath
    def loadusers(self):
        with open("users.json",'r', encoding= 'utf-8') as file:
            users = json.load(file)
            for user in users:
                new_user =  json.loads(user)
                new_user = User(new_user['username'],new_user['password'],new_user['email'])
                self.users.append(new_user)

repo = UserRepository()

while True:
    print(" Menü ".center(50,'*'))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    if secim == '1':
        username = input('Username: ')
        password = input('password: ')
        email = input('email: ')
        user = User(username,password,email)
        repo.Register(user)
    
    elif secim == '2':
        if repo.IsLoggedIn == True:
            print('You are already logged in')
        else:
            username = input('Username: ')
            password = input('password: ')
            repo.Login(username,password)

    elif secim == '3':
        if repo.IsLoggedIn == True:
            repo.Logout()
        else:
            print('You are not already logged in')
    elif secim == '4':
        repo.Identity()
    else:
        print('EXITING ...')
        break





