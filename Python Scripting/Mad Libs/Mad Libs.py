import os
# os.mkdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Mad Libs\\Madlibs.txt')

os.chdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Mad Libs\\Madlibs.txt')

for i in range(10):
    print('-------Welcome to Mad Libs------- ')
    print('')
    print('The ___1___ panda walked to the ___2___ and then ___3___. A nearby ___4___ was unaffected by these events.')
    print('')
    blank1 =  str(input('Enter 1: '))
    blank2 =  str(input('Enter 2: '))
    blank3 =  str(input('Enter 3: '))
    blank4 =  str(input('Enter 4: '))

    madlibs = open('Madlibs.txt', 'w')
    madlibs.write('The {} panda walked to the {} and then {}. A nearby {} was unaffected by these events.\n'.format(blank1, blank2, blank3, blank4))
    madlibs.close()

    madlibs = open('Madlibs.txt')
    Mad_file = madlibs.read()
    print(Mad_file)
    madlibs.close()