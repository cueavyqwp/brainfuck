"""
main
"""

import sys

style = [ ">" , "<" , "]" , "[" , "+" , "-" , "." , "," ]

class bf :

    def __init__( self , code : str = "" ) -> None :
        self.code = code

    def build( self , path ) -> str :
        with open( path , "r" , encoding = "utf-8" ) as file :
            self.code = file.read()
        return self.code

    def save( self , path ) -> None :
        with open( path , "w" , encoding = "utf-8" ) as file :
            file.write( self.code )

    def set( self , code ) -> None :
        self.code = code

    def run( self , func = None , show : bool = True , info : dict = {} ) -> dict :
        output : str = info[ "output" ] if "output" in info else ""
        code_p : int = info[ "code_p" ] if "code_p" in info else 0
        memory : list = info[ "mem" ] if "mem" in info else [ 0 ]
        code : str = info[ "code" ] if "code" in info else self.bfc
        p : int = info[ "p" ] if "p" in info else 0
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
                    char = chr( memory[ p ] )
                    output += char
                    if show :
                        print( char , end = "" )
                case "[" :
                    if not memory[ p ] :
                        code_p += code[ code_p : ].index( "]" )
                case "]" :
                    code_p = code[ : code_p ].rindex( "[" ) - 1
            code_p += 1
            info = { "code" : code , "mem" : memory , "output" : output , "p" : p , "code_p" : code_p }
            func( info ) if func else ...
        return info

    @property
    def bfc( self ) -> str :
        return "".join( filter( lambda code : code in style , self.code ) )

if __name__ == "__main__" :
    args = sys.argv[ 1 : ]
    main = bf()
    main.build( args[ -1 ] )
    main.run()
