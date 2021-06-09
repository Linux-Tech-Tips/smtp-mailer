# Python script that allows sending mail through an account with an open SMTP server
import smtplib, ssl

# Email address and password used to access an SMTP server to send the email
actualSender = str(input("Input the email address of the actual sender: "))
senderPass = str(input("Input the password of the actual sender email: "))

# Email address that receives the email
actualReceiver = str(input("Input email address of receiver: "))

# Name and address of the sender that the receiver sees
senderName = str(input("Input the sender's name that the receiver sees: "))
senderAdress = str(input("Input an email that the receiver sees as the sender's mail: (leave empty to use the actual sender address) "))
if(senderAdress == ""):
    senderAdress = actualSender

# Name and address of the receiver that the receiver sees
receiverName = str(input("Input the receiver's name to be displayed: "))
receiverAdress = actualReceiver

# Email subject
subject = str(input("Input the email subject: "))

# Email message
message = str(input("Input the actual message of the email: "))

# SMTP server and port, often can be found on the email provider's website
serverName = str(input("Input the SMTP server address of the actual sender email: "))
serverPort = str(input("Input the port the SMTP server is running at: "))
server = smtplib.SMTP_SSL(serverName, serverPort)

# Logging into the SMTP server
server.login(actualSender, senderPass)

# Sending the email
server.sendmail(actualSender, actualReceiver, "From: " + senderName + " <" + senderAdress + ">\nTo: " + receiverName + " <" + receiverAdress + ">\nSubject: " + subject + "\n\n" + message)
server.close()
