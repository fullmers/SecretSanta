import smtplib
import authenticationInfo
 
LOGIN = authenticationInfo.login
PASSWORD = authenticationInfo.password
SMTPSERVER='smtp.gmail.com:587'

SPENDING_LIMIT = "150 NOK"

def constructMessage(santaName, santeeName):
    greeting = "Dear " + santaName + ",\n\n"
    body = ("Thank you for participating in this year's Shortcut Secret Santa exchange!"
            " You are Santa to " + santeeName + ".\n\n"
            "Kindly remember: there is a " + SPENDING_LIMIT + " spending limit on gifts. "
            "You can alternatively make or bake something for " + santeeName +
            ", if you think they would like that.\n\n"
            "Finally, please remember you have until their last day before leaving for the holidays to sneakily deliver your gift ;) "
            "You can check the 2017 Ferie calendar to find out that date.\n\n\n")
    closing = "Ho ho ho, \nSanta Sarah"
    fullmessage = greeting + body + closing
    return fullmessage

def send(to_addr, message):
    server = smtplib.SMTP(SMTPSERVER)
    server.starttls()
    server.login(LOGIN,PASSWORD)
    server.sendmail(LOGIN, to_addr, message)
    server.quit()
    

#message = 'test message'
#sendemail(login, 'sarah.fullmer@gmail.com', message)
