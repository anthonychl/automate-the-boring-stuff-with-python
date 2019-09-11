'''
SMTP simple mail transfer protocol
'''
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp object with the connexion settings: server and port

conn.ehlo() # command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
# (250, b'smtp.gmail.com at your service, [an IP address goes here]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nSMTPUTF8')

conn.starttls() # start tls encryption to secure our credentials
# (220, b'2.0.0 Ready to start TLS')

conn.login('my@gmail.com','password')
'''
with google you can set 'application specific passwords' for your account
so the password used by your python apps doesnt have to be the
same as your regular password
'''

conn.sendmail('my@gmail.com','toAddress@gmail.com','Subject: Hello. \n\n The body of the email starts here')
# if the response is a [] it means the email(s) were sent correctly
# else it will contain a list of the unsent mail
conn.quit()