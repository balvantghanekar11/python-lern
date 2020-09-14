#tut69

class Employe:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}{lname}.{lname}@blu.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def printemail(self):
        pass


hs=Employe("harsh","patel")
nr=Employe("neeraj","patel") 

print(hs.email)