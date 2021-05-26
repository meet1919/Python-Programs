def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return pow(x,y)
def area_square(x):
    return x * x
def area_rectangle(x,y):
    return x * y
def profit_calulator(x,y):
    profit = (x-y)
    print("Profit is = ",profit)
    profit_percentage = float((profit/y)*100)
    print("Profit Percentage is : ",profit_percentage)
def simple_interest(x,y,z):
    si = (x * y * z)/100
    print(si)
def compound_interest(x,y,z):
    first_part = float(1 + (0.01*y))
    second_part = float(pow(first_part,z))
    third_part = x * second_part
    ci = int(third_part - x)
    print(ci)

print("Python Calculator")
print("")
i=0
while i<=20:
    print("")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Area of Square")
    print("7.Area of Rectangle")
    print("8.Profit and Profit Percentage")
    print("9.Interest")
    print("10.Unit Conversion")
    choice = input("Enter Choice 1/2/3/4/5/6/7/8/9/10: ")

    if choice <= '5':
        a = int(input("Enter 1st number : "))
        b = int(input("Enter 2nd number : "))

        if choice == '1':
            print("Your sum is : ")
            print(add(a,b))

        elif choice == '2':
            print("Your difference is : ")
            print(substract(a,b))

        elif choice == '3':
            print("Your product is : ")
            print(int(multiply(a,b)))

        elif choice == '4':
            print("Your answer is : ")
            print(int(divide(a,b)))

        elif choice == '5':
            print(power(a,b))

        else:
            print("Invalid input")

    elif choice > '5':

        # noinspection SyntaxError
        if choice == '6':
            s = float(input("Enter Side Length : "))
            print(area_square(s))

        elif choice == '7':
            l = int(input("Enter Length : "))
            b = int(input("Enter Breadth : "))
            print(area_rectangle(l,b))

        elif choice == '8':
            cp = float(input("Enter Cost Price : "))
            sp = float(input("Enter Sell Price : "))
            print(profit_calulator(sp,cp))

        elif choice == '9':
            print("Which type of Interest? \n 1.Simple Interest \n 2.Compound Interest")
            choice1 = input("Enter your choice : ")

            if choice1 == '1':
                principle_amount = float(input("Enter Principle amount : "))
                rate = float(input("Enter Rate of Interest : "))
                time_period = float(input("Enter Time Period in years : "))
                print(simple_interest(principle_amount,rate,time_period))

            elif choice1 == '2':
                principle_amount = float(input("Enter Principle amount : "))
                rate = float(input("Enter Rate of Interest : "))
                time_period = float(input("Enter Time Period in years : "))
                compound_interest(principle_amount,rate,time_period)

        elif choice == '55':
            print("Select Conversion types \n 1.Length \n 2.Weight ")
            choice2 = int(input("Enter your choice of conversion : "))

            if choice2 == '1':
                print("1. ft to m \n 2 in to m.\n 3. in to ft \n 4. AU to km \n 5. Light Years to km")
                choice3 = int(input("Enter your option : "))

                if choice3 == '1':
                    feet = float(input("Enter Length in feet : "))
                    meter1= float(feet * 0.3048)
                    print(meter1)

                elif choice3 == '2':
                    inch = float(input("Enter Length in feet : "))
                    meter2= float(inch * 0.0254)
                    print(meter2)

                else:
            elif choice2 == '2':

        else:
            print("Invalid Input")

    else:
        print("Invalid Input")

    i+=1
