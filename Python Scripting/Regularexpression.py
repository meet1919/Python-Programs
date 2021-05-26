import re

Text = input('')
def phone_number(x):
    phn = re.compile(r'\d{10}')
    mo = phn.search(x)
    print('Phone Number is: ', mo.group())

def email_address(x):
    email = re.compile(r'\w+@\S+')  # or re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.com') this can be used for
                                    # a particular type of email address which contains .com at the end
    mo1 = email.search(x)
    print('Email Address is: ', mo1.group())

phone_number(Text)
email_address(Text)
