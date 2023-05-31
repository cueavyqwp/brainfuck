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
    code = bfc.build( file_path )
    bfc.run( code )
elif args[0] == "-b" and argl > 1 and os.path.exists( args[1] ) :
    file_path = args[1]
    code = bfc.build( file_path )
    bfc.save_file( file_path + "c" , code )
else : \
print( \
"""
[ --build / -b ] file
run and build '.bfc' file | 运行并生成'.bfc'文件
-b [ path ] : build '.bfc' file | 生成`.bfc`文件
""")
