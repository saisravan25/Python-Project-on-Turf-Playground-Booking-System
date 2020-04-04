from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def Email(Manager_Name,username,password,Email_ID):

    msg = MIMEMultipart()
    msg['Subject'] = "Welcome to Bangalore Sports Club"

    body = f'''Hi {Manager_Name},
    \nCongratulations on joining Bangalore Sports Club.\n\
    \nPlease find your Login credentials and kindly do not share to anyone as they are stricly restricted for respective Manager's.\n
    \nUsername : {username}\nPassword : {password}
    '''

    msg.attach(MIMEText(body, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("saisravanviru25@gmail.com", "darlingfan")
    text = msg.as_string()
    try:
        s.sendmail("saisravanviru25@gmail.com",Email_ID, text)
        s.quit()
        return True
    except smtplib.SMTPRecipientsRefused as e:
        return False

