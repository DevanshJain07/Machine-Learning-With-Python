def myfun(hincm):
    assert (hincm>0),"Please enter a valid height"
    return int(hincm)/100

try:
    f=open('myfile.txt','w')
    f.write("I am trying to write data to the file")
except IOError:
    print("Error:you have open file with r permission")
else:
    print("You are successful here")
finally:
    print("Yes")


