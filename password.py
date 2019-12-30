import random
import smtplib
r=""
sender="devanshsampatjain@gmail.com"
reciever="devanshsjain@gmail.com"
password="devansh@1999"
obj=smtplib.SMTP('smtp.gmail.com',587)
obj.starttls()
obj.login(sender,password)

for i in range(5):
 a=chr(random.randint(32,108))
 r=r+a
 r=str(a)
obj.sendmail(sender,reciever,r)
obj.quit()
