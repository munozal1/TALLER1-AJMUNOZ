from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self,user_id:int,username:str,password:str,is_admin: bool):
        self.id=user_id
        self.username=username
        self.password=password
        self.is_admin=is_admin
        

user_db={
    'alvaromm': User(1,'alvaromm','TopSecret2025',True),
    'usuario2': User(2,'usuario2','Usuario22025',False),
    'usuario3': User(3,'usuario3','Usuario32025',False)    
}