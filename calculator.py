def Plus(a, b):
        return print ("Das Ergebnis ist : " ,a + b)

def Minus(a, b):
    return print ("Das Ergebnis ist : " ,a - b)

def Mal(a, b):
        return print ("Das Ergebnis ist : " ,a * b)

def Geteilt(a, b):
        return print ("Das Ergebnis ist : " ,a / b)
    
def debug(s):
    return print(s)

while(True):

    print("Bitte Setze deine Zahlen! ")

    x = int(input("Zahl 1 : "))
    y = int(input("Zahl 2 : "))

    print("")
    print("Plus [1] , Minus[2], Mal [3] , Geteilt [4] ")
    print("")
    
    op = int(input())
            
    if op == 1 :
        Plus(x, y)  
    if op == 2 :
        Minus(x,y)
    if op == 3 :
        Mal(x,y)
    if op == 4 :
        Geteilt(x,y)

    close = input("Noch eine Runde ? [Y] || [N] : ")
    
    if close.upper() or close.islower() == "Y":
        continue
    if close.upper() or close.islower() == "N":
        print("TaschenRechner aus")
        break

#
# # :)