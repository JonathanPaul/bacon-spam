# Coded by Max00355 & Jonathan8Paul
import smtplib as s
import time
print"\n\r\n\rWelcome to Jon Paul's Bacon SPAMMING Client. 17+ lines of code as of 10/21/2014."
#name = raw_input("Name: ")
name = "bob farmer"
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login("internationalbaconstation", "FIXTHISNOW")
print "Logged In! \n\r"
email = raw_input("Destination Email Address aka Where the Bacon will be Sent: ")
#message = raw_input("Email Message: ")
print "> Connecting to International Bacon Station."
time.sleep(1)
print "> Sending bacon into the void."
while True:
    obj.sendmail("username", email, "YOU'VE RECIEVED BACON!\n\r---From your friend " + name)
    print "ya!"
print "Sent!"
