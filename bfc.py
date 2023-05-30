def build( file_path ) :
    with open( file_path , "r" , encoding = "utf-8" ) as file :
        code = file.read()
    print(code)
    code_c = ""
    for i in code :
        if i in [ ">" , "<" , "]" , "[" , "+" , "-" , "." , "," ] :
            code_c += i
    return code_c

def run( file_path ) :
    pass
