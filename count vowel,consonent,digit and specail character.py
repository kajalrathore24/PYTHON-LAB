st=input("enter string")
v=0
c=0
d=0
s=0
for i in st:
    if i>="a" and i<="z" or i>="A" and i<="Z":
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            v+=1
        else:
            c+=1
    elif i>="0" and i<="9":
        d+=1
    else:
        s+=1
print("no. of vowel={} \n no. of consonent={} \n no. of digit {} \n no. of special character {}".format(v,c,d,s))
