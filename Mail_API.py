import os  # This lib helps me to get my email
import smtplib  # this lib does everything work

email_address = os.environ.get('email_chrome_python') #In order not to place personal data here, I use environmental variables.
email_password = os.environ.get('password_chrome_python')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Dont understand this. But it allows me to encrypt my code and allow it to understand that I'm using gmail to send it.
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    # Down here I define the subject and message as well as who will receive the message
    smtp.login(email_address, email_password)
    # Improved! Now you chose the message you want to send away.
    subject = input('Subject: ')
    body = input('Text: ')

    msg = f'subject: {subject} \n\n{body}'
    # here I send the email
    smtp.sendmail(email_address, input("Email Address: "), msg)
