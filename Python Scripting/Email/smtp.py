import smtplib, os

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
recipient = input('Enter recipient Email Address: ')
subject = input('Enter Subject: ')
smtpobj.sendmail(sender, recipient, subject)
smtpobj.quit()