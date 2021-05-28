#V2
while True:

    #Have a 'try' set up to catch errors
    try:

        #Get my user input and set my vars to false for later
        wow = input("")
        add = sub = mult = div = avg = com = rng = sqr = root = finie = False
        operations = {'+', '-', '*', '/'}

        #Check if the user input anything, if not, then close
        if wow == "":
            print("Closing...")
            break

        else:

            #Check which operation the user input

            #Sets 'sym' as '+'
            sym = ['+']

            #Sees what 'sym' is
            for substring in sym:

                #Checks if the value of 'sym' is in the user input
                if substring in wow:

                    #And if it is, then 'add' will turn true
                    add = True

            sym1 = ['- ']
            for substring in sym1:
                if substring in wow:
                    sub = True
            sym2 = ['*']
            for substring in sym2:
                if substring in wow:
                    mult = True
            sym3 = ['/']
            for substring in sym3:
                if substring in wow:
                    div = True
            sym4 = ['~=']
            for substring in sym4:
                if substring in wow:
                    avg = True
            sym5 = [',']
            for substring in sym5:
                if substring in wow:
                    com = True
            sym6 = ['#=']
            for substring in sym6:
                if substring in wow:
                    rng = True
            sym7 = ['^']
            for substring in sym7:
                if substring in wow:
                    sqr = True
            sym8 = ['%=']
            for substring in sym8:
                if substring in wow:
                    root = True

            if com == True:
                print("If you're trying to get an average or range, do not use commas for seperation, only spaces")
                continue

            #To the operations

            #Addition
            elif add == True:

                #This splits everything in the string up into a list: "This is a list" -> ['This', 'is', 'a', 'list']
                fin = wow.split(' ')

                #Takes the new list and removes the operation sign
                fin = [e for e in fin if e not in operations]

                #Changes the list to be intagers
                fin = [int(i) for i in fin]

                #Takes list and adds everything together
                print(sum(fin))
                continue
            
            #Subtraction
            elif sub == True:
                fin = wow.split(' ')
                fin = [e for e in fin if e not in operations]
                fin = [int(i) for i in fin]
                ans = fin[0] - fin[-1]
                print(ans)
                continue

            #Multiplication
            elif mult == True:
                fin = wow.split()
                ans = float(fin[0]) * float(fin[-1])
                print(ans)
                continue

            #Division
            elif div == True:
                fin = wow.split()
                ans = float(fin[0]) / float(fin[-1])
                print(ans)
                continue

            #Average
            elif avg == True:
                fin = wow.split(' ')
                fin.remove('~=')
                fini = [int(i) for i in wow.split() if i.isdigit()]
                print(sum(fini)/len(fin))
                continue

            #Range
            elif rng == True:

                #Here we split the string up
                fin = wow.split(' ')

                #Then we remove the operation as we know what it already is
                fin.remove('#=')

                #We search the list for intagers and put them in a new list
                fini = [int(i) for i in fin]

                #Sort that list
                fini.sort()

                #Check if there's a negative number
                scab = ['-']
                for substring in scab:
                    if substring in fin:
                        finie = True
                
                #If there...
                if finie == True:

                    #...is, then we remove the '-'
                    fini.remove('-')

                    #And add the numbers
                    ans = float(fini[-1]) + float(fini[0])
                    print(ans)
                else:

                    #...isn't, then we just subtract
                    ans = float(fini[-1]) - float(fini[0])
                    print(ans)
                continue

            #Square
            elif sqr == True:
                fin = wow.split(' ')
                fin.remove('^')
                fini = [int(i) for i in fin]
                ans = fini[0] ** fini[-1]
                scab = ['-']
                for substring in scab:
                    if substring in wow:
                        finie = True
                if finie == True:
                    print(f"-{ans}")
                else:
                    print(ans)
                continue

            #elif root == True:
                #fin = 100 ** (-10)
                #print(fin)
            
            #If the user input something other than defined, tell them
            else:
                print("Only: '+' (addition), '-' (subtraction), '*' (multiplication), '/' (division), '^' (square), '~='/'#=' (after list of numbers for average/range)")
                continue

    #Tell the user they didn't put spaces while inputting their equation
    except IndexError:
        print("Put spaces between each character")
        continue
