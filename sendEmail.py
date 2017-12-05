import smtplib
import authenticationInfo
 
login = authenticationInfo.login
password = authenticationInfo.password
smtpserver='smtp.gmail.com:587'

SPENDING_LIMIT = "150 NOK"

def constructMessage(santaName, santeeName):
    greeting = "Dear " + santaName + ",\n\n"
    body = ("Thank you for participating in this year's Shortcut Secret Santa exchange!"
            " You are Santa to " + santeeName + ".\n\n"
            "Kindly remember: there is a " + SPENDING_LIMIT + " on gifts. "
            "You can alternatively make or bake something for " + santeeName +
            ", if you think they would like that.\n\n"
            "Finally, please remember you have until their last day before leaving for the holidays to sneakily deliver your gift ;) "
            "You can check the 2017 Ferie calendar to find out that date.\n\n\n")
    closing = "Ho ho ho, \nSanta Sarah"
    fullmessage = greeting + body + closing
    return fullmessage

def sendemail(from_addr, to_addr, message):
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr, message)
    server.quit()
    

#message = 'test message'
#sendemail(login, 'sarah.fullmer@gmail.com', message)
