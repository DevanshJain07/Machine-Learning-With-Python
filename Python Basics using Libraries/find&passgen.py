def rotate_left3(l,n): 
    return l[n:] + l[:n]

#general
def rotate_left3(nums):
    l=len(nums)
    k=[]
    for i in range(1,l):
        k.append(nums[i])
    k.append(nums[0])
    return k    

def middle(a,b):
    x=len(a)
    y=len(b)
    x=a[int(x/2)]
    y=b[int(y/2)]
    c=[x,y]
    return c

'''PASSWORD GENERATOR CODE'''
p="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%^&*abcdefghijklmnopqrstuvwxyz"
p=list(p)
m=len(p)
l=6
import numpy
k=numpy.random.randint(0,69,6)
password=p[k[0]]+p[k[1]]+p[k[2]]+p[k[3]]+p[k[4]]+p[k[5]]
print(password)

"""password generator"""
scope="abcdefghijklmnopqrstuvxyz0123456789@!#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ"

l=list(scope)
print(len(l))
import numpy
position=numpy.random.randint(0,69,6)





























