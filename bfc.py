"""
生成.bfc文件 和 运行brainfuck文件

---

build '.bfc' file and run brainfuck file
"""

def build( file_path ) :
    with open( file_path , "r" , encoding = "utf-8" ) as file :
        code = file.read()
    code_c = ""
    for i in code :
        if i in [ ">" , "<" , "]" , "[" , "+" , "-" , "." , "," ] :
            code_c += i
    return code_c

def save_file( code_c_path , code_c ) :
    with open( code_c_path , "w" , encoding = "utf-8" ) as file :
        file.write( code_c )

def run( code ) :
    p = 0
    memory = [0]
    code_p = 0
    code_len = len(code)
    while code_p < code_len :
        i = code[code_p]
        if i == ">" :
            p += 1
            if len( memory ) <= p :
                memory.append(0)
            code_p += 1
        elif i == "<" :
            p -= 1
            code_p += 1
        elif i == "+" :
            memory[p] += 1
            code_p += 1
        elif i == "-" :
            memory[p] -= 1
            code_p += 1
        elif i == "," :
            while 1 :
                try :
                    inp = ord( input() )
                    memory[p] = inp
                    break
                except TypeError :
                    pass
            code_p += 1
        elif i == "." :
            print( chr( memory[p] ) , end = "" )
            code_p += 1
        elif i == "[" :
            if memory[p] :
                code_p += 1
            else :
                code_p += code[code_p:].index( "]" ) + 1
        elif i == "]" :
            code_p = code[:code_p].rindex( "[" )
