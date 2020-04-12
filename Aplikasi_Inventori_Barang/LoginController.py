from User import User

class LoginController:
    def __init__(self):
        self.user=User()
    
    def Login(self,username, password):
        user=User(username)
        if password==user.getPassword():
            return user.getRole()


