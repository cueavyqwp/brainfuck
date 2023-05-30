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

def run( file_path ) :
    pass
