
def get():
    lista = "1+2"
    s = lista[i]
    i+=1
    return s

def Expr(): 
    while(True):
        Stat("")
    get()
def Stat (): 
    value = 0  
    value = Factor(value)
    value = input()
def Expression( result): 
    result1 = 0
    result2 = 0
    result1 = Term(result1)

    while(get() == '+' or get() == '-'):
        if(get()=='+'):
            result2=Term(result2)
            result1+=result2
        elif(get()=='-'):
            result2=Term(result2)
            result1-=result2

    result=result1
def Term( result):
    result1 = 0
    result2 = 0
    result1 = Factor(result1)

    while(get() == '*' or get() == '/'):
        if(get()=='*'):
            result2=Factor(result2)
            result1*=result2
        elif(get()=='/'):
            result2=Factor(result2)
            result1/=result2

    result=result1

def Factor( result): 
    signo=1
    if get() == "-":
        signo = -1


    result*=signo

def Number( result):
    number 
    result = int(value)


Stat()