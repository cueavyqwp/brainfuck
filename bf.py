"""
主文件

---

main
"""
import bfc
import sys
import os

args = sys.argv[1:]
argl = len(args)
if not argl :
    args = [ "" ]

if argl == 1 and os.path.exists( args[0] ) :
    file_path = args[0]
    file_type = os.path.splitext( os.path.split( file_path )[-1] )[-1]
    print(file_type)
elif args[0] == "-b" and argl > 1 and os.path.exists( args[1] ) :
    file_path = args[1]
    code_c =  bfc.build( file_path )
    file_dir = os.path.split( file_path )[0]
    if not file_dir :
        file_dir = "." + os.sep
    file_name = os.path.splitext( file_path )[0]
    if argl > 3 and os.path.exists( args[3] ) :
        code_c_path = os.path.join( args[3] , file_name + ".bfc" )
    else :
        code_c_path = os.path.join( file_dir , file_name + ".bfc" )
    bfc.save_file( code_c_path , code_c )
elif args[0] == "-r" and argl > 1 and os.path.exists( args[1] ) :
    file_path = args[1]
    print("r")
else : \
print( \
"""
[ --build / -b ] [ --run / -r ] file
run and build '.bfc' file | 运行并生成'.bfc'文件

-b [ path ] : build '.bfc' file | 生成`.bfc`文件
-r : run brainfuck file | 运行brainfuck文件
""")