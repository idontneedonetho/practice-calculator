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

        #Check if the user input anything, if not, then close
        if wow == "":
            print("Closing...")
            break

        else:
            
            #Move on to seperating the numbers in the user input
            first = wow[0]
            second = wow[-1]

            #Check if the user put a second number, if not, then it defualts to 0
            if wow[-1] == "":
                second = int(0)

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

            #Do the operation
            if add == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                print(sum(fin))
                continue
            
            elif sub == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] - sum(fin[1:])
                print(ans)
                continue

            elif mult == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] * sum(fin[1:])
                print(ans)
                continue

            elif div == True:
                fin = [int(i) for i in wow.split() if i.isdigit()]
                ans = fin[0] / sum(fin[1:])
                print(ans)
                continue
            
            #If the user input something other than defined, tell them
            else:
                print("Only: +, -, *, /")
                continue

    #Tell the user they didn't put spaces while inputting their equation
    except IndexError:
        print("Put spaces between each character")
        continue
