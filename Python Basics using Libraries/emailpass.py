import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("username@gmail.com","password")
message="""ewd
"""
server.sendmail('username@gmail.com','reciever@gmail.com',message)





















