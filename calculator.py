while(True):

    print("Bitte Setze deine Zahlen! ")

    x = int(input("Zahl 1 : "))
    y = int(input("Zahl 2 : "))

    print("")
    print("Plus [1] , Minus[2], Mal [3] , Geteilt [4] ")
    print("")

    op = int(input())
            
    if op == 1 :
        print ("Das Ergebnis ist : " , x + y)
                    
    if op == 2 :
        print("Das Ergebnis ist : " , x - y)

    if op == 3 :
        print("Das Ergebnis ist : " , x * y)
                
    if op == 4 :
        print("Das Ergebnis ist : " , x / y)
    
    close = input("Noch eine Runde ? [Y] || [N] : ")

    if close.upper() == "Y":
        continue
    if close.upper() == "N":
        print("TaschenRechner aus")
        break
