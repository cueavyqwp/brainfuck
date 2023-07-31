"""
main
"""

import sys

class bf :

    def __init__( self ) -> None :
        self.code = ""

    def build( self , path ) -> str :
        with open( path , "r" , encoding = "utf-8" ) as file :
            self.code = "".join( [ code if code in [ ">" , "<" , "]" , "[" , "+" , "-" , "." , "," ] else "" for code in file.read() ] )
        return self.code

    def save( self , path ) -> None :
        with open( path , "w" , encoding = "utf-8" ) as file :
            file.write( self.code )

    def set( self , code ) -> None :
        self.code = code

    def run( self ) -> bool :
        code = self.code
        memory = [ 0 ]
        code_p = 0
        p = 0
        while code_p < len( code ) :
            match code[ code_p ] :
                case ">" :
                    p += 1
                    if len( memory ) <= p :
                        memory.append( 0 )
                case "<" :
                    p -= 1
                case "+" :
                    memory[ p ] += 1
                case "-" :
                    memory[ p ] -= 1
                case "," :
                    while True :
                        try :
                            memory[ p ] = ord( input() )
                            break
                        except TypeError :
                            pass
                case "." :
                    print( chr( memory[ p ] ) , end = "" )
                case "[" :
                    if not memory[ p ] :
                        code_p += code[ code_p : ].index( "]" )
                case "]" :
                    code_p = code[ : code_p ].rindex( "[" ) - 1
            code_p += 1

if __name__ == "__main__" :
    args = sys.argv[ 1 : ]
    main = bf()
    main.build( args[ -1 ] )
    main.run()
