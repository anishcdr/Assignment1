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
