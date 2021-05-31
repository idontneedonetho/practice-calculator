#V2.5 - ~132 Lines of code without spaces and comments
#Set up a while loop so that the program doesn't close when you complete an operation
while True:

    #Have a 'try' set up to catch errors
    try:

        #Get user input and set vars to false for later
        wow = input("").lower()
        add = sub = mult = div = avg = com = rng = sqr = root = finie = oper = False
        operations = {'+', '-', '*', '/', '^', '2r', '~=', '#=', ',', '='}

        #Check if the user input anything, if not, then close
        if wow == (""):
            print("Closing...")
            break

        #Help function
        if wow == ('help'):
            print("'+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)")
            print("'~='/'#=' (after list of numbers for average/range, using spaces for separation)")
            print("To close program, press enter while blank")
            continue

        #Check if the user put an acceptable operation
        for substring in operations:
            if substring in wow:
                oper = True

        #If the user input something other than defined, tell them what they can do
        if oper == False:
            print("Only use: '+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)")
            print("'~='/'#=' (after list of numbers for average/range, using spaces for separation)")
            continue

        #Else, move on to this:
        elif oper == True:

            #Check which operation the user input

            #Addition
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

                    #Takes the new list and removes anything in the 'operations' var that was set up at the start:
                    #['1', '+', '2', '+', '3', '+', '4'] -> ['1', '2', '3', '4']
                    fin = [e for e in fin if e not in operations]

                    #Changes the strings to be intagers:
                    #['1', '2', '3', '4'] -> [1, 2, 3, 4]
                    fin = [float(i) for i in fin]
                    ans = float(sum(fin))

                    #And adds everything together
                    print("= %s" % ans)
                    continue

            #Subtraction
            sym1 = ['- ']
            for substring in sym1:
                if substring in wow:
                    fin = wow.split(' ')
                    fin = [e for e in fin if e not in operations]
                    fin = [float(i) for i in fin]

                    #This separates the fist number, addes the rest together, then takes that answer and subtracts the first number
                    #[5, 2, 1, 3] -> 5, 2 + 1 + 3 -> 5 - 6 = -1
                    ans = (fin.pop(0) - sum(fin))
                    print("= %s" % ans)
                    continue

            #Multiplication
            sym2 = ['*']
            for substring in sym2:
                if substring in wow:
                    fin = wow.split()
                    fin = [g for g in fin if g not in operations]
                    fin = [float(i) for i in fin]

                    #Create a new var
                    ans = 1

                    #Then, loop for each number in the list
                    for x in fin:

                        #'*=' is the operation for "x = x * ?", where '?' is our input, in this case 'ans'
                        ans *= x
                    print("= %s" % ans)
                    continue

            #Division
            sym3 = ['/']
            for substring in sym3:
                if substring in wow:
                    fin = wow.split()
                    fin = [e for e in fin if e not in operations]
                    fin = [float(i) for i in fin]
                    ans = 1

                    #This multiplys everything after the first number in the list
                    for x in fin[1:]:
                        ans *= x
                    
                    #Then divids that answer by the first number in the list, just like with subtraction
                    final = (fin[0] / ans)
                    print("= %s" % final)
                    continue

            #Average
            sym4 = ['~=']
            for substring in sym4:
                if substring in wow:
                    fin = wow.split(' ')
                    fin.remove('~=')
                    fini = [float(i) for i in fin]

                    #Adds up all the numbers, then divides by the amount of numbers. len() returns the amount of items in a list
                    ans = (sum(fini)/len(fin))
                    print("= %s" % ans)
                    continue

            #Comma for error
            sym5 = [',']
            for substring in sym5:
                if substring in wow:
                    print("If you're trying to get an average or range, do not use commas for seperation, only spaces")
                    continue

            #Range
            sym6 = ['#=']
            for substring in sym6:
                if substring in wow:

                    #Split the string up
                    fin = wow.split(' ')

                    #Remove the operation as it's already known
                    fin.remove('#=')

                    #Search the list for numbers and put them in a new list
                    fini = [float(i) for i in fin]

                    #Sort that list
                    fini.sort()

                    #Check if there's a negative number
                    scab = ['-']
                    for substring in scab:
                        if substring in fin:

                            #If there is, remove the '-'
                            fini.remove('-')

                            #And add the numbers
                            ans = (float(fini[-1]) + float(fini[0]))
                            print("= %s" % ans)
                            continue
                        else:

                            #If there isn't, just subtract
                            ans = (float(fini[-1]) - float(fini[0]))
                            print("= %s" % ans)
                            continue

            #Exponent
            sym7 = ['^']
            for substring in sym7:
                if substring in wow:
                    fin = wow.split(' ')
                    fin.remove('^')
                    fini = [float(i) for i in fin]

                    #'**' is python's built in exponent function
                    ans = fini[0] ** fini[-1]

                    #Check if the first number is negative and the exponent is '10'
                    scab = ['-']
                    for substring in scab:
                        if substring in wow[0] and fini[-1] == (10):
                                        
                            #If they are, add a '-' in front of the answer to make it "negative"
                            print("= -%s" % ans)
                            continue
                        else:
                            print("= %s" % ans)
                            continue

            #Square Root
            sym8 = ['2r']
            for substring in sym8:
                if substring in wow:
                    fin = wow.split(' ')
                    fin.remove('2r')
                    fini = [float(i) for i in fin]
                    ans = float(fini[0]) ** (1/2)
                    print("= %s" % ans)
                    continue

            #Equals to
            sym9 = [' = ']
            for substring in sym9:
                if substring in wow:
                    fin = wow.split(' ')
                    if fin[0] == fin[-1]:
                        print("True")
                        continue
                    else:
                        print("False")
                        continue

    #Tell the user they put too many or not enough spaces somewhere
    except ValueError:
        print("Error: you put too many or not enough spaces somewhere")
        print("Make sure you're using one space inbetween each number/operation")
        continue
