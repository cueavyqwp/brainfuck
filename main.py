import brainfuck
import sys
import os

if __name__ == "__main__" :
    file = sys.argv[ -1 ]
    if not ( len( sys.argv ) > 1 and os.path.exists( file ) and os.path.isfile( file ) ) : raise FileNotFoundError
    if os.path.splitext( file )[ -1 ] != ".bf" : exit()
    main = brainfuck.brainfuck()
    with open( file , "r" , encoding = "utf-8" ) as fp : main.load( fp.read() )
    main.run()
