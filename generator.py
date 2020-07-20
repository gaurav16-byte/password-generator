import random           #random string selection
import sys      #for exiting if wrong choice entered

l_case=list('abcdefghijklmnopqrstuvwxyz')   #lowercase
u_case=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   #uppercase
digits=list('1234567890')   #digits
char=list('!@#$%^&*-_+')   #special caharcters

global n    #taking n as global to take n from user only once

n=int(input('Enter length of your password'))

def easy():     #easy password only upper and lowercase
    pw=''
    for i in range(1,n+1):
        pw+=random.choice(l_case+u_case)
    print(pw)

def medium():   #lower,uppercase and digits
    pw=''
    for j in range(1,n+1):
        pw+=random.choice(l_case+u_case+digits)
    print(pw)

def strong():   #all characters
    pw=''
    for k in range(1,n+1):
        pw+=random.choice(l_case+u_case+digits+char)
    print(pw)

print('A) Easy Password')
print('B) Medium Password')
print('C) Strong Password')
choice=input('Enter Your Choice')
if choice=='a' or choice=='A':
    easy()
elif choice=='b' or choice=='B':
    medium()
elif choice=='c' or choice=='C':
    strong()
else:
    sys.exit()
