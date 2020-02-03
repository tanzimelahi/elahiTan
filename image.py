import math
fl=open("image.ppm","w")
initialstr="P3\n50 50\n255\n"
fl.write(initialstr)
data=list(range(2500))
def createimage():
    # the first for is x value
    for i in range(50):
        #y value
        for j in range(50):
            if((i-25)**2+(j-25)**2<=625):
                a=["255","0","0"]
                data[j*50+i]=a
            else:
                a=["0","0","0"]
                data[j*50+i]=a

createimage()
for ls in data:
    for a in ls:
        initialstr+=a+" "
fl.write(initialstr)
fl.close()
print(initialstr)
