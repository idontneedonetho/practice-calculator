#V2.75 - 60 lines of code before comments
#Set up a while loop so that the program doesn't close when you complete an operation
while True:
    #Get user input and set vars to false for later
    inp = input("").lower()
    add = sub = mult = div = avg = com = rng = sqr = root = go = False
    operations = {'+', '-', '*', '/', '^', '2r', '~=', '-=', ',', '='}
    #Check if the user put an acceptable operation
    for substring in operations:
        if substring in inp:
            go = True
    #Check if the user input anything, if not, then close
    if inp == (""):
        print("Closing...")
        break
    #Help function
    elif inp == ('help'):
            print("'+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)\n'~='/'-=' (after list of numbers for average/range, using spaces for separation\nTo close program, press enter while blank")
            continue
    #If the user input something other than defined, tell them what they can do
    if go == False:
        print("Only use: '+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '2r' (square root)\n'~='/'-=' (after list of numbers for average/range, using spaces for separation)")
        continue
    #Else, move on to this:
    if go == True:
        #Have a 'try' set up to catch errors
        try:
            #Define a master function, 'calcu()' and put sub-functions. Sub-function: "if splt[1] == ('+')"
            def calcu():
                #Set 'ans' to 1 for later
                ans = 1
                #This splits everything in the string up into a list:
                # "1 + 2 + 3 + 4" -> ['1', '+', '2', '+', '3', '+', '4']
                splt = inp.split(' ')
                splt = [i for i in splt if i not in ('' '')]
                #Takes the new list and removes anything in the 'operations' var that was set up at the start:
                #['1', '+', '2', '+', '3', '+', '4'] -> ['1', '2', '3', '4']
                fin = [e for e in splt if e not in operations]
                #Changes the strings to be intagers:
                #['1', '2', '3', '4'] -> [1, 2, 3, 4]
                fin = [float(i) for i in fin]
                #Addition
                if splt[1] == ('+'):
                    #Adds everything together
                    ans = sum(fin)
                #Subtraction
                elif splt[1] == ('-'):
                    #This separates the fist number, addes the rest together, then takes that answer and subtracts the first number
                    #[5, 2, 1, 3] -> 5, 2 + 1 + 3 -> 5 - 6 = -1
                    ans = (fin.pop(0) - sum(fin))
                #Average
                elif splt[-1] == ('~='):
                    splt.remove('~=')
                    ans = (sum(fin)/len(fin))
                #Multiplication
                elif splt[1] == ('*'):
                    #Loop for each number in the list
                    for x in fin:
                        #'*=' is the operation for "x = x * ?", where '?' is our input, in this case 'ans'
                        ans *= x
                #Division
                elif splt[1] == ('/'):
                    #This multiplies everything after the first number in the list
                    for x in fin[1:]:
                        ans *= x
                        #Then divids that answer by the first number in the list, just like with subtraction
                        ans = (fin[0] / ans)
                #Range
                elif splt[-1] == ('-='):
                    #Remove the operation as it's already known
                    splt.remove('-=')
                    #Sort the list from above
                    fin.sort()
                    #Then subtract the largest number from the smallest
                    ans = (float(fin[-1]) - float(fin[0]))
                #Exponent
                elif splt[1] == ('^'):
                    #'**' is python's built in exponent function
                    ans = fin[0] ** fin[-1]
                    #Check if the first number is negative and the exponent is '10'
                    #If they are, multiply 'ans' by -1 to make it negative
                    scab = ['-']
                    for substring in scab:
                        if substring in splt[0] and fin[-1] == (10):
                            ans = ans * -1
                #Square Root
                elif splt[-1] == ('2r'):
                    splt.remove('2r')
                    ans = float(fin[0]) ** (1/2)
                #This sets the value of 'calcu()' to whatever 'ans' is
                return ans
            #Because we used 'return ans' to set the value of 'calcu()' we can then just print 'calcu()' to get the answer
            print("= " + str(calcu()))
            continue
        except ZeroDivisionError:
            print("You can't divide by 0")
            continue
        except ValueError:
            print("Error:\nIf you used commas for seperation, please use spaces instead")
            continue