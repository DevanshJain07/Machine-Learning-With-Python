import random
import smtplib
import webbrowser
r=""
sender="devanshsampatjain@gmail.com"
reciever="devanshsjain@gmail.com"
password="devansh1999"
obj=smtplib.SMTP("smtp.gmail.com",587) 
obj.starttls()
obj.login(sender,password)
for i in range(5):
    a1=chr(random.randint(32,108))
    r=r+a1
    r=str(r)
obj.sendmail(sender,reciever,r)
obj.quit()
r1=input("enter otp") 
if(r1==r):
    
    a=input("enter your favourite movie")
    if(a=="comedy"):
        webbrowser.open_new_tab("https://www.google.com/search?q=hero&oq=hero&aqs=chrome..69i57j0l5.2396j0j7&sourceid=chrome&ie=UTF-8")
    elif(a=="romantic"):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=-KfsY-qwBS0")
    elif(a=="action"):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=fxm4KcKDQl0")
    else:
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=mSlgu8AQAd4")



