import bfc
import sys
import os

args = sys.argv[1:]
argl = len(args)
if not argl :
    args = [ "" ]

if argl == 1 and os.path.exists( args[0] ) :
    file_path = args[0]
    filetype = os.path.splitext( os.path.split( file_path )[-1] )[-1]
    print(filetype)
elif args[0] == "-b" and argl > 1 :
    file_path = args[1]
    print("b")
elif args[0] == "-r" and argl > 1 :
    file_path = args[1]
    print("r")
else : \
print( \
"""
[ --build / -b ] [ --run / -r ] file
run and build '.bfc' file | 运行并生成'.bfc'文件

-b : build '.bfc' file | 生成`.bfc`文件
-r : run brainfuck file | 运行brainfuck文件
""")