from pymongo import MongoClient

class User:
    def __init__(self, username=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["databasebarang"]
        self.colusers=dbName["user"]
        if username:
            self.username=username
    
    def addUser(self, username, password, name, telp, address, position, email, role):
        user_attr={"username":username, "password":password, "name":name, "telp":telp, "address":address, "position":position, "email":email, "role": role}
        return self.colusers.insert_one(user_attr)

    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        set_username={"$set": {"username":username}}
        return self.colusers.update_one({"username":self.username}, set_username)
    
    def getPassword(self):
        get_pass=self.colusers.find_one({"username":self.username})
        return get_pass['password']
    
    def getName(self):
        get_name=self.colusers.find_one({"username":self.username})
        return get_name['name'] 

    def setName(self, name):
        set_name={"$set": {"name":name}}
        return self.colusers.update_one({"username":self.username}, set_name)
    
    def getTelp(self):
        get_telp=self.colusers.find_one({"username":self.username})
        return get_telp['telp'] 

    def setTelp(self, telp):
        set_telp={"$set": {"telp":telp}}
        return self.colusers.update_one({"username":self.username}, set_telp)

    def getAddress(self):
        get_address=self.colusers.find_one({"username":self.username})
        return get_address['address'] 

    def setAddress(self, address):
        set_address={"$set": {"address":address}}
        return self.colusers.update_one({"username":self.username}, set_address)
    
    def getPosition(self):
        get_position=self.colusers.find_one({"username":self.username})
        return get_position['position'] 

    def setPosition(self, position):
        set_position={"$set": {"position":position}}
        return self.colusers.update_one({"username":self.username}, set_position)
    
    def getEmail(self):
        get_email=self.colusers.find_one({"username":self.username})
        return get_email['email'] 

    def setEmail(self, email):
        set_email={"$set": {"email":email}}
        return self.colusers.update_one({"username":self.username}, set_email)
    
    def getRole(self):
        get_role=self.colusers.find_one({"username":self.username})
        return get_role['role'] 
    
    def deleteUser(self):
        del_user={"username": self.username}
        return self.colusers.delete_one(del_user)
    
    def updateUser(self, name, telp, address, position, email, role):
        update_user={"$set": {"name":name, "telp":telp, "address":address, "position":position, "email":email, "role": role}}
        return self.colusers.update_one({"username":self.username}, update_user)
    
    def getDataUser(self):
        return self.colusers.find_one({"username":self.username})
    
    def getAllUsers(self):
        users=self.colusers.find()
        list_user=[]
        for user in users:
            list_user.append(user)
        return list_user




    
    





