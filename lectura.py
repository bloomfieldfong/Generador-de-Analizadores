from funciones import *
def read(url):
    
    lista = ["CHARACTERS","KEYWORDS","PRODUCTIONS"]
    
    character = []
    keywords = []
    tokens = []
    producciones = []
    antes = []
    punto = 0
    archivo = []
    my_file = open(url, "r")
    for line in my_file.readlines():
        if line[-1:] == "\n":
            archivo.append((line[:-1]))
        else:
            archivo.append(line)
    my_file.close() 

    for myline in archivo:

        if myline.strip() == "TOKENS":
            punto = 1
        if myline.strip() == "CHARACTERS":
            punto = 2
        if myline.strip() == "KEYWORDS":
            punto = 3
        if myline.strip() == "PRODUCTIONS":
            punto = 4
        if punto == 1:
            tokens.append(myline)
        if punto == 0:
            antes.append(myline)
        if punto == 2:
            character.append(myline)
        if punto == 3:
            keywords.append(myline)
        if punto == 4:
            producciones.append(myline)

    return antes, character, keywords, tokens, producciones

def chequear_char(y):

    if "chr(" in y or "CHR(" in y :

        return True
    else:
        return False
    
def crear(antes, character, keywords, tokens, producciones):
    automata = []
    chars = []
    automata_keywords = []
    if antes[0] != "":
        nombre = antes[0].split(" ")
        if nombre[0] == "COMPILER":
            file = open(nombre[1]+".py",'w')
      
    file.write("from automata import * ")
    file.write("\n")
    file.write("from scanner import *")
    file.write("\n")
    file.write("#keywords")
    keywordss = []
    for i in range(len(keywords)):
        
        if keywords[i].strip() == "KEYWORDS":
            pass
        else:
            if keywords[i] != "":
                x = keywords[i].split("=")
                y = x[1].replace(chr(34), "")
                y = y.replace(chr(39), "")
                y = y.replace(".", "")
                keywordss.append(y.strip())
                
    file.write("\n")
    file.write("keywords ="+str(keywordss))
    file.write("\n")
            
    file.write("#character")
    file.write("\n")
    for i in range(len(character)):
        if character[i].strip() == "CHARACTERS":
            pass
        else:
            last_char_index = character[i].rfind(".")
            new_string = character[i][:last_char_index] + "" + character[i][last_char_index+1:]
            if new_string != "":
                file.write("\n")
                y = new_string.split("=")
                
                if chequear_char(y[1]):
                    chars.append(y[1].lower())
                    file.write(new_string.lower())
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip().lower()+")")
                    
                    file.write("\n")
                elif y[1].strip() == "'A' . 'Z'" or y[1].strip() == "'A' . 'Z'." or y[1].strip()== chr(34)+"A"+chr(34)+ ".." +chr(34)+"Z"+chr(34):
                    y[1]=chr(34)+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+chr(34)
                    file.write(y[0]+'='+y[1])
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                    file.write("\n")
                elif y[1].strip()== "'a' . 'z'" or y[1].strip()== "'a' . 'z'." or y[1].strip()== chr(34)+"a"+chr(34)+ ".." +chr(34)+"z"+chr(34):
                    y[1] =chr(34)+"abcdefghijklmnopqrstuvwxyz"+chr(34)
                    file.write(y[0]+'='+y[1])
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                    file.write("\n")
                else:
                    file.write(new_string)
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                     
                    file.write("\n")

    file.write("#tokens")
    file.write("\n")

    if tokens[-1][0:3] == "END":
        tokens.pop()
    for i in range(len(tokens)):
        if tokens[i].strip() == "TOKENS":
            pass
        else:
            if len(tokens[i]) != 0:
                ##edita los tokens que se ingresan.
                new_string = str_to_list(tokens[i])
                if new_string[len(new_string)-1] == ".":
                    new_string.pop()
                
                new_string = listToStr(new_string)
                new_string = new_string.strip()
                new_string = new_string.replace(chr(34), "+")
                new_string = new_string.replace("(H)", chr(34)+"H"+chr(34))
                new_string = new_string.replace("(","+"+chr(34)+" ("+chr(34)+"+")
                new_string = new_string.replace(")","+"+chr(34)+")"+chr(34))
                new_string = new_string.replace("|","+"+chr(34)+"|"+chr(34)+"+")
                new_string = new_string.replace(".", chr(34)+". "+chr(34))
                new_string = new_string.replace("{", "+"+chr(34)+" (("+chr(34)+"+")
                new_string = new_string.replace("[", "+"+chr(34)+" (("+chr(34)+"+")
                new_string = new_string.replace("}", "+"+chr(34)+")*) "+chr(34)+"+")
                new_string = new_string.replace("]", "+"+chr(34)+")*) "+chr(34)+"+")

                ######### ver si el txt tiene except keyword
                texx = new_string.split()
                  
                if len(texx)>2 and texx[len(texx)-1] == "KEYWORDS" and texx[len(texx)-2] == "EXCEPT" :
                     texx.pop()
                     texx.pop()
                     automata_keywords.append(texx[0])
                else:
                    automata.append(texx[0])
                     
                
                texx = listToStr(texx)
                texx = texx.split("=")
                
                texx[1]= texx[1].replace(")*)", ")*) ")
                     
                if texx[1][0]== "+":
                    texx[1] = texx[1].replace("+","",1)
                if texx[1][-1] == "+":
                    texx[1] = texx[1][:-1]
                
                se = str_to_list(texx[1])
                if se[-2] == " ":
                    se.pop(len(se)-2)
                    
                for i in range(len(se)):
                    if se[i] == "." or se[i] == ",":
                        se.insert(i+1, " ")
                texx[1] = listToStr(se)
                
                
                final = texx[0]+"="+listToStr(texx[1])
                final = final.replace("((", " ((")
                final = final.replace("+++", " +")
                final = final.replace("++", " +")
                final = final.replace(chr(34)+"("+chr(34), chr(34)+" ("+chr(34))
                    
                
                ###quitar el espacio del principio
                hola = final.split("=")
                
                if str_to_list(hola[1])[1] == " ":
                    x = str_to_list(hola[1])
                    x.pop(1)
                    hola[1] = listToStr(x)
            
            
                final = hola[0]+"="+listToStr(hola[1])
                file.write(final)
                file.write("\n")
                
    file.write("automata_keyword=" +strL(automata_keywords))
    file.write("\n")
    file.write("automata ="+strL(automata))
    file.write("\n")
    file.write("charss ="+strL(chars))
    file.write("\n")
    file.write("scanner(keywords, automata , automata_keyword, charss)")
    file.write("\n")
    
    
    ############### PRODUCCIONES ################

    if producciones[-1][0:3] == "END":
        producciones.pop()

    proddd = []
    resp =[]
    for i in range(len(producciones)):
        if producciones[i] == "PRODUCTIONS"  or producciones[i]== "":
            pass
        else:
            proddd.append(producciones[i])
            if producciones[i] =="." or producciones[i] =="\t.":
                resp.append(proddd)
                proddd = []
                    
            

    for z in range(len(resp)):
        if resp[z][0] != "\t":
            s = resp[z][0].split("=",1)
            x = s[0].replace("<", "(")
            x = x.replace(">", "):")
            x = x.replace("ref int", "")
            s[0] = x
            if s[0].find("(") >=0:
                resp[z][0] = "def "+s[0]+s[1]
            else:
                
                resp[z][0] = "def "+s[0]+"():"+s[1]
                
                    

        else:
            s = resp[z][1].split("=",1)
            x = s[0].replace("<", "(")
            x = x.replace(">", "):")
            x = x.replace("ref int", "")
            s[0] = x

            if s[0].find("(") >=0:
                resp[z][1] = "def "+s[0]+s[1]
            else:
                resp[z][1] = "\ndef "+s[0]+"():"+s[1]


    for i in range(len(resp)):
        for s in range(len(resp[i])):
            resp[i][s] = resp[i][s].replace("\t", "")
            resp[i][s] = resp[i][s].replace(".)", "")
            resp[i][s] = resp[i][s].replace(";", "")
            resp[i][s] = resp[i][s].replace("<", "(")
            resp[i][s] = resp[i][s].replace(">", ")")
            resp[i][s] = resp[i][s].replace("ref int", "")
            resp[i][s] = resp[i][s].replace("ref", "")
            resp[i][s] = resp[i][s].replace("(.", "\n")
            resp[i][s] = resp[i][s].replace(":", ":")
    
    nuev = []
    asdf = []
    hola= []
    correecta = []
    a = 2
    for i in range(len(resp)):
        for s in range(len(resp[i])):
            po = resp[i][s]
            
            if len(po)!= 0:
                if po[0] == "{":
                    a = 1
                if po[0] == "}":
                    correecta.append(editarOrWhile(asdf))
                    a = 2
                    nuev = []    
            if a == 1:
                asdf.append(resp[i][s])
            elif a == 2:
                correecta.append(resp[i][s])
                nuev.append(asdf)
                asdf = []

                
#    fun = open("producciones.txt",'w')
#    fun.write(str(resp))
#    for i in range(len(resp)):
#        for s in range(len(resp[i])):
#            if resp[i][s] != ".":
#                fun.write("\n")
#                fun.write(str(resp[i][s]))
    
    for e in range(len(correecta)):
        correecta[e] = correecta[e].replace("{", "\nwhile(True):\n\t")
        correecta[e] = correecta[e].replace("}", "")
        correecta[e] = correecta[e].replace("Term(  result1)", "result1 = Term(result1)")
        correecta[e] = correecta[e].replace("Term(  result2)", "result2 = Term(result2)")
        correecta[e] = correecta[e].replace("Factor( result2)", "result2 = Factor(result2)")
        correecta[e] = correecta[e].replace("Factor( result1)", "result1 = Factor(result1)")
        correecta[e] = correecta[e].replace("Expression(  value)", "value = Factor(value)")
        correecta[e] = correecta[e].replace("Expression(  value)", "value = Factor(value)")
        correecta[e] = correecta[e].replace(chr(34)+"."+chr(34), "\nget("+chr(34)+"."+chr(34)+")")
        correecta[e] = correecta[e].replace("["+chr(34)+"-"+chr(34), "if follow() =="+chr(34)+"-"+chr(34)+":\n\tsigno = -1")
        correecta[e] = correecta[e].replace("signo = -1]", "")
        correecta[e] = correecta[e].replace("( Number( result) |", " ##")
         
    fun = open("producciones.py",'w')
    for i in range(len(correecta)):
        if correecta[i] != ".":
            fun.write(correecta[i])
            fun.write("\n")
        if correecta[i] == ".":
            fun.write("\nreturn result\n\n")

    fun.close()
    sigue = []

    with open('producciones.py', 'r') as fh:
        for line in fh:
            sigue.append(line)
    
    for i in range(len(sigue)):
        e = sigue[i].split()
        if len(e) !=0:
            if e[0] != "def":
                sigue[i] = "\t"+sigue[i]
    
    fh.close()
    
    file.write("\n")
    file.write("\n")
    file.write("\n")
    fun = open("producciones.py",'w')
    for i in range(len(sigue)):
        if sigue[i] != ".":
            file.write(sigue[i])
            
    
    
            