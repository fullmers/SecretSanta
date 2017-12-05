import smtplib
import authenticationInfo
 
login = authenticationInfo.login
password = authenticationInfo.password
smtpserver='smtp.gmail.com:587'
          
def sendemail(from_addr, to_addr, message):
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr, message)
    server.quit()
    

message = 'test message'
sendemail(login, 'sarah.fullmer@gmail.com', message)
