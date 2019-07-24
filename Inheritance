class school_member:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Initialized schoolmember {}\n'.format(self.name))
        
    def tell(self):
        print('Name:{} Age:{}\n'.format(self.name,self.age))
        
        
class Teacher(school_member):
    def __init__(self,name,age,salary):
        school_member.__init__(self,name,age)
        self.salary=salary
        print('Initialized teacher {}\n'.format(self.name))
    
    
    def tell(self):
        print('Name:{} Age:{} Salary:{}\n'.format(self.name,self.age,self.salary))
        
        
class Student(school_member):
    def __init__(self,name,age,grade):
        school_member.__init__(self,name,age)
        self.grade=grade
        print('Initialized student {}\n'.format(self.name))
        
    def tell(self):
        print('Name:{} Age:{} Grade:{}'.format(self.name,self.age,self.grade))
    


t=Teacher('Pushpa','35','70,000')
s=Student('Abhishek','21','A')


members=[t,s]

for member in members:
    member.tell()
