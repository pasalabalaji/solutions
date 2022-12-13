class student:
      def __init__(self,username,password):
          self.username=username
          self.password=password
          print("user with name ",self.username," created successfully...")
      def validate(self,username,password):
          if self.username==username and self.password==password:
               print("login successfully...")
          else:
               print("incorrect details")
name=input("enter name ")
password=input("enter password ")
obj=student(name,password)

t=input("enter your username ")
y=input("enter your password")
obj.validate(t,y)
