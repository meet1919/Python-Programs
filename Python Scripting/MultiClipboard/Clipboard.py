import shelve

ShelveFile = shelve.open('clipboard')

# General Form
Name = [str(input('Name: '))]
Address = [str(input('Address: '))]
Emailid = [str(input('Email id: '))]
Describe = [str(input('Describe Yourself: '))]

ShelveFile['Name'] = Name
ShelveFile['Address'] = Address
ShelveFile['Emailid'] = Emailid
ShelveFile['Describe'] = Describe

ShelveFile.close()
