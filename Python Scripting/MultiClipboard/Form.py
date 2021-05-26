import shelve

ShelveFile = shelve.open('clipboard')

name = str(input('Name: '))
address = str(input('Address: '))
emailid = str(input('Email id: '))
describe = str(input('Describe Yourself: '))
# Form
if name == '''ShelveFile['Name']''':
    name_input = ShelveFile['Name']
    print(name_input)
else:
    print(name)

if address == '''ShelveFile['Address']''':
    address_input = ShelveFile['Address']
    print(address_input)
else:
    print(address)

if emailid == '''ShelveFile['Emailid']''':
    emailid_input = ShelveFile['Emailid']
    print(emailid_input)
else:
    print(emailid)

if describe == '''ShelveFile['Describe']''':
    describe_input = ShelveFile['Describe']
    print(describe_input)
else:
    print(describe)
