class Student(object):
    def __init__(self):
        self.students = []
    
    def set_name(self, name):
        self.students.append({name:{}})

    def get_names(self):
        names=[]
        for i in self.students:
            names.append(i.keys()[0])
        return names  
    
    def __str__(self):
        return str(self.students)  

    def delete_name(self, name):
        for i in self.students:
            key=i.keys()[0]
            if key==name:
                self.students.remove(i)
        



a=Student()
a.set_name('nishant')
a.set_name('shivam')
a.set_name('vikas')
print a

results=a.get_names()
print results
a.delete_name('nishant')
print a





