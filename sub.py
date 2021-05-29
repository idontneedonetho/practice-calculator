#V2.5
#Set up a while loop so that the program doesn't close when you complete an operation
while True:

    #Have a 'try' set up to catch errors
    try:

        #Get my user input and set my vars to false for later
        wow = input("").lower()
        add = sub = mult = div = avg = com = rng = sqr = root = finie = False
        operations = {'+', '-', '*', '/', '^', '2r', '~=', '#='}

        #Check if the user input anything, if not, then close
        if wow == (""):
            print("Closing...")
            break

        else:
            #Check if the user put an operation
            oper = operations
            for substring in oper:
                if substring in wow[1] or wow[-1]:
                    oper = True

                #If the user input something other than defined, tell them what they can do
        if oper == False:
            print("Only: '+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)")
            print("'~='/'#=' (after list of numbers for average/range)")
            continue

        if oper == True:

            #Help function
            if wow == ('help'):
                print("'+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root), '~='/'#=' (after list of numbers for average/range)")
                print("To close program, press enter while blank")
                continue

            else:

                #Check which operation the user input

                #Sets 'sym' as '+'
                sym = ['+']

                #Substring sees what 'sym' is
                for substring in sym:

                    #Checks if the value of 'sym' is in the user input
                    if substring in wow:

                    #And if it is, then it will run this code:

                        #This splits everything in the string up into a list:
                        # "1 + 2 + 3 + 4" -> ['1', '+', '2', '+', '3', '+', '4']
                        fin = wow.split(' ')

                        #Takes the new list and removes anything in the 'operations' var that I set up at the start:
                        #['1', '+', '2', '+', '3', '+', '4'] -> ['1', '2', '3', '4']
                        fin = [e for e in fin if e not in operations]

                        #Changes the strings to be intagers:
                        #['1', '2', '3', '4'] -> [1, 2, 3, 4]
                        fin = [float(i) for i in fin]

                        #And adds everything together
                        print(sum(fin))
                        continue

                sym1 = ['- ']
                for substring in sym1:
                    if substring in wow:
                        fin = wow.split(' ')
                        fin = [e for e in fin if e not in operations]
                        fin = [float(i) for i in fin]

                        #This separates the fist number, addes the rest together, then takes that answer and subtracts the first number
                        #[5, 2, 1, 3] -> 5, 2 + 1 + 3 -> 5 - 6 = -1
                        print(fin.pop(0) - sum(fin))
                        continue

                sym2 = ['*']
                for substring in sym2:
                    if substring in wow:
                        fin = wow.split()
                        fin = [g for g in fin if g not in operations]
                        fini = [float(i) for i in fin]

                        #Here we create a new var
                        ans = 1

                        #Then, we loop for each number in the list
                        for x in fini:

                            #*= is the operation for x = x * '?', where '?' is our input, in this case 'ans'
                            ans *= x
                        print(ans)
                        continue

                sym3 = ['/']
                for substring in sym3:
                    if substring in wow:
                        fin = wow.split()
                        fin = [e for e in fin if e not in operations]
                        fin = [float(i) for i in fin]
                        print(fin[0] / fin[-1])
                        continue

                sym4 = ['~=']
                for substring in sym4:
                    if substring in wow:
                        fin = wow.split(' ')
                        fin.remove('~=')
                        fini = [float(i) for i in fin]

                        #Adds up all the numbers, then divides by the amount of numbers. len() returns the amount of items in a list
                        print(sum(fini)/len(fin))
                        continue

                sym5 = [',']
                for substring in sym5:
                    if substring in wow:
                        print("If you're trying to get an average or range, do not use commas for seperation, only spaces")
                        continue

                sym6 = ['#=']
                for substring in sym6:
                    if substring in wow:

                        #Here we split the string up
                        fin = wow.split(' ')

                        #Then we remove the operation as we know what it already is
                        fin.remove('#=')

                        #We search the list for intagers and put them in a new list
                        fini = [float(i) for i in fin]

                        #Sort that list
                        fini.sort()

                        #Check if there's a negative number
                        scab = ['-']
                        for substring in scab:
                            if substring in fin:

                            #If there is, we remove the '-'
                                fini.remove('-')

                                #And add the numbers
                                print(float(fini[-1]) + float(fini[0]))
                            else:

                                #If there isn't, we just subtract
                                print(float(fini[-1]) - float(fini[0]))
                            continue

                sym7 = ['^']
                for substring in sym7:
                    if substring in wow:
                        fin = wow.split(' ')
                        fin.remove('^')
                        fini = [float(i) for i in fin]

                        #'**' is python's built in square function
                        ans = fini[0] ** fini[-1]

                        #I need to check if the first number is negative
                        scab = ['-']
                        for substring in scab:
                            if substring in wow[0]:
                                        
                                #If it is, we add a '-' in front of the answer to make it "negative"
                                print(f"-{ans}")
                                continue
                            else:
                                print(ans)
                                continue

                sym8 = ['2r']
                for substring in sym8:
                    if substring in wow:
                        fin = wow.split(' ')
                        fin.remove('2r')
                        fini = [float(i) for i in fin]
                        ans = float(fini[0]) ** (1/2)
                        print(ans)
                        continue
        else:
            print("Only: '+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)")
            print("'~='/'#=' (after list of numbers for average/range)")
            continue

    #Tell the user they didn't put spaces while inputting their equation
    except IndexError:
        print("Put spaces between each character")
        continue