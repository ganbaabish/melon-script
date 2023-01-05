import ssl
import smtplib
from email.message import EmailMessage

def run(err:str=''):

    mail_sender = 'ganbaabish@gmail.com'
    mail_receiver = 'edu.ganbaa@gmail.com'
    mail_pass = 'huvb hnpk dnwd iwtv'

    subject = 'Script is stopped...!'

    body = """
        Something went wrong...!
        Server is shutting down...!
        Please check your server...!
        Error:
    """ +err

    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_sender, mail_pass)
        smtp.sendmail(mail_sender, mail_receiver, em.as_string())
