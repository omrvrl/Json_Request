import json
import os

# DECORATOR
def CheckPath(func):
    def wrapper(self):
        if os.path.exists('users.json'):
            func(self)
        else:
            return False
    return wrapper

# CLASS
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# CLASS
class UserRepository:
    def __init__(self):
        self.IsLoggedIn = False
        self.users = []
        self.loadusers()
        self.index = 0  # Initialize the index for custom __next__

    def __iter__(self):                                               #            }
        return self

    def __next__(self):
        if self.index < len(self.users):                             #           CLASS İÇERİSİNDE CLASS İTERATOR KULLANMA
            current_user = self.users[self.index]
            self.index += 1
            return current_user
        else:
            raise StopIteration                                      #               }

    def Register(self, user: User):
        self.users.append(user)
        self.savetofile()

    def Login(self, username, password):              
        for user in self:                                            #             BURADA KULLANILDI 
            if user.username == username and user.password == password:
                self.IsLoggedIn = True
                print('Logging successful')
                break
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
        user_list = []
        for user in self.users:
            user_list.append(json.dumps(user.__dict__))
        
        with open('users.json', 'w') as file:
            json.dump(user_list, file)

    @CheckPath
    def loadusers(self):
        if os.path.exists("users.json"):
            with open("users.json", 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    new_user = json.loads(user)
                    new_user = User(new_user['username'], new_user['password'], new_user['email'])
                    self.users.append(new_user)

repo = UserRepository()

while True:
    print(" Menu ".center(50, '*'))
    choice = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice: ")
    
    if choice == '1':
        username = input('Username: ')
        password = input('Password: ')
        email = input('Email: ')
        user = User(username, password, email)
        repo.Register(user)
    
    elif choice == '2':
        if repo.IsLoggedIn:
            print('You are already logged in')
        else:
            username = input('Username: ')
            password = input('Password: ')
            repo.Login(username, password)

    elif choice == '3':
        if repo.IsLoggedIn:
            repo.Logout()
        else:
            print('You are not already logged in')
    
    elif choice == '4':
        repo.Identity()
    
    elif choice == '5':
        print('EXITING ...')
        break
