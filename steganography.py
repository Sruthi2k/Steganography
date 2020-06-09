import cv2 as cv
import string
import os
d={}
c={}


for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)




x=cv.imread("sunrise.png")  #reading image in which text will be encrypted
i=x.shape[0]
j=x.shape[1]
print(i,j)  #prints dimensions of the image


key=input("\n Enter/Set a security key to encrypt:") #it acts like a password 
text=input("\n Enter text to hide:")                 #text to be encrypted

kl=0
tln=len(text)
z=0    #decides plane
n=0    #number of rows
m=0    #number of columns

l=len(text)

#Hides data in image in pixels

for i  in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n=n+1                         #Spacing
    m=m+1
    m=(m+1)%3                     #prints in verical line
    kl=(kl+1)%len(key)

#Saves image and shows it
    
cv.imwrite("encrypted_img.png",x)
os.startfile("encrypted_img.png")  #Shows image in ImageViewer
print("\n Data hidden succesfully:)\n don't worry ur text is safe!!")


kl=0
tln=len(text)
z=0     #decides plane
n=0     #number of rows
m=0     #number of columns

#Decrypt text from image

ch=int(input("\n Enter 1 to extract data from image:"))

if ch==1:
    key1=input("Re-enter security key to extract text(VERIFICATION): ")
    decrypt=""

    if key==key1:
        for i  in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key)
        print("\n HURRAY!! KEY is RIGHT:)\n Encrypted text was: ",decrypt)
    else:
         print("\n Key not matched,seems like you are a HACKER!!!")
