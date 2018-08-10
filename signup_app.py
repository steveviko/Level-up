import re
class Signup(object):
    def __init__(self, FirstName, LastName, email_addr):
        self.FirstName = str(FirstName)
        self.LastName = str(LastName)
        self.email_addr = Signup.validate_email(email_addr)        
        self.User_db= []

    def Full_Names(self):
        if not (self.FirstName and self.LastName):
            return {'response':'please enter your first name and last name '}
        else:
            return {self.FirstName+" " + self.LastName}

    def submit(self):
        if not (self.FirstName and self.LastName):
            return {'response':'please enter your first name and last name '}
        else:
            self.users = {'FirstName': self.FirstName,
                        'LastName': self.LastName, 'email': self.email_addr}
            self.User_db.append(self.users)
            return self.User_db

   
    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return email



   