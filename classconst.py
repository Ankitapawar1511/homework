# student has features like name roll and subject with marks. there are 5 subject for every student with some marks.
#  student has one operation which will display per of student
# use dic for sub and marks

class student :
       def __init__(self,n,r):
            self.name=n
            self.roll=r
            self.subject={}

       def sub_marks(self,sub,mark):
             self.subject[sub]=mark
             
       def per(self):
            total=sum(self.subject.values())  
            no_of_sub=(len(self.subject)*100)
            per= (total/no_of_sub )*100
            return per
s=student("ram",1)
s.sub_marks("math",85)
s.sub_marks("eng",84)
s.sub_marks("mar",87)
s.sub_marks("his",89)
s.sub_marks("scie",85)

print(f"name: {s.name}")
for sub,marks in s.subject.items():
      print(f"{sub}:{marks}")
per=s.per()
print(f"per:{per}%")

















    #    def dis(self):
    #         print(f"name is:{self.name}\n salary is:{self.roll}\n email is:{self.sub}")
     
      
