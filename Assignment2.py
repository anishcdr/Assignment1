#Assignment 2
#1. Creating a calculator (Using if)
a=input("a=")
b=input("b=")
op=input("operator=")
file1=open("calculator.txt","a+")
if(op=='+'):
  print("result=",(int(a)+int(b)))
  file1.write("result={}".format(int(a)+int(b)))
if(op=='-'):
  print("result=",(int(a)-int(b)))
  file1.write("result={}".format(int(a)-int(b)))
if(op=='*'):
  print("result=",(int(a)*int(b)))
  file1.write("result={}".format(int(a)*int(b)))
if(op=='/'):
  print("result=",(int(a)/int(b)))
  file1.write("result={}".format(int(a)/int(b)))
else:
  print("Not a valid operator")
  file1.write("Not a valid operator")
print(file1.read())

#2.
a=open("a2.txt","r+")
a.write("Writing with r+")
print(a.read())
a=open("a2.txt","w+")
a.write("Overwriting with w+\n")
print(a.read())
a=open("a2.txt","a+")
a.write("Writing with a+\n")
print(a.read())
