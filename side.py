#V2
while True:

    #Have a 'try' set up to catch errors
    try:

        #Get my user input and set my vars to false for later
        wow = input("")
        add = sub = mult = div = avg = com = rng = sqr = root = finie =  False

        #Check if the user input anything, if not, then close
        if wow == "":
            print("Closing...")
            break

        else:

            #Check which operation the user input

            #sets 'sym' as '+'
            sym = ['+']

            #sets 'substring' as 'sym'
            for substring in sym:

                #Checks if the value of 'substring' is in the user input
                if substring in wow:

                    #And if it is, then add will turn true
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
            elif add == True:

                #This looks for integers in the list and separates them from whatever else there is
                fin = wow.split()

                #Takes the two numbers in the new list and does the operation
                ans = float(fin[0]) + float(fin[-1])

                #Then it prints the final answer
                print(ans)
                continue
            
            elif sub == True:
                fin = wow.split()
                ans = float(fin[0]) - float(fin[-1])
                print(ans)
                continue

            elif mult == True:
                fin = wow.split()
                ans = float(fin[0]) * float(fin[-1])
                print(ans)
                continue

            elif div == True:
                fin = wow.split()
                ans = float(fin[0]) / float(fin[-1])
                print(ans)
                continue

            elif avg == True:
                fin = wow.split(' ')
                fin.remove('~=')
                fini = [int(i) for i in wow.split() if i.isdigit()]
                print(sum(fini)/len(fin))
                continue

            elif rng == True:
                fin = wow.split(' ')
                fin.remove('#=')
                fini = [int(i) for i in fin]
                fini.sort()
                scab = ['-']
                for substring in scab:
                    if substring in fin:
                        finie = True
                if finie == True:
                    fini.remove('-')
                    ans = float(fini[-1]) + float(fini[0])
                    print(ans)
                else:
                    ans = float(fini[-1]) - float(fini[0])
                    print(ans)
                continue

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