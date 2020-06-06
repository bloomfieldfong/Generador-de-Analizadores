from automata import * 
from scanner import *
#keywords
keywords =['while', 'do', 'if', 'switch']
#character

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
letter = character(letter)

digit = "0123456789" 
digit = character(digit)

tab = chr(9)
tab = character(tab)

eol = chr(10)
eol = character(eol)
#tokens
ident=letter+" (("+letter+"|"+digit+")*)"
number=digit+" (("+digit+")*)"
automata_keyword=[ident]
automata =[number]
charss =[ chr(9), chr(10)]
scanner(keywords, automata , automata_keyword, charss)



def Expr(): 
	while(True):
		Stat ("")
	get(".")

	return result

def Stat (): 
	value = 0  
	value = input()
	value = Factor(value)

	return result

def Expression( result): 
	result1 = 0
	result2 = 0
	result1 = Term(result1)
	while(follow() == '+' or follow() == '-'):
		if(follow()=='+'):
			result2=Term(result2)
			result1+=result2
		elif(follow()=='-'):
			result2=Term(result2)
			result1-=result2

	result=result1

	return result

def Term( result):
	result1 = 0
	result2 = 0
	result1 = Factor(result1)
	while(follow() == '*' or follow() == '/'):
		if(follow()=='*'):
			result2=Factor(result2)
			result1*=result2
		elif(follow()=='/'):
			result2=Factor(result2)
			result1/=result2

	result=result1

	return result


def Factor( result): 
	signo=1
	if follow() =="-":
		signo = -1

	 ## "("Expression(  result)")") 
	result*=signo

	return result


def Number( result):   
	result = int(value)

	return result

