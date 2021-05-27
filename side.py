#V2
while True:

    #Have a 'try' set up to catch errors
    try:

        #Get my user input and set my vars to false for later
        wow = input("")
        add = False
        sub = False
        mult = False
        div = False
        avg = False
        com = False

        #Check if the user input anything, if not, then close
        if wow == "":
            print("Closing...")
            break

        else:

            #Check which operation the user put
            sym = ['+']
            for substring in sym:
                if substring in wow:
                    add = True
            sym1 = ['-']
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

            if com == True:
                print("If you're trying to get an average, do not use commas for seperation")
                continue
            
            #To the operations
            elif add == True:

                #This looks for integers in the list and separates them from whatever else there is
                fin = [int(i) for i in wow.split() if i.isdigit()]

                #Takes the two numbers in the new list and does the operation
                ans = fin[0] + fin[1]

                #Then it prints the final answer
                print(ans)
                continue
            
            elif sub == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] - fin[1]
                print(ans)
                continue

            elif mult == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] * fin[1]
                print(ans)
                continue

            elif div == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] / fin[1]
                print(ans)
                continue

            elif avg == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                print(sum(fin)/len(fin))
            
            #If the user input something other than defined, tell them
            else:
                print("Only: '+' -> (for addition), '-' -> (for subtraction), '*' -> (for multiplication), '/' -> (for division), '~=' -> (at end of list of numbers for the average, no ',')")
                continue

    #Tell the user they didn't put spaces while inputting their equation
    except IndexError:
        print("Put spaces between each character")
        continue