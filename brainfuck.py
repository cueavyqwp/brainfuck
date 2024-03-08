"""
brainfuck
"""

class brainfuck :

    def __init__( self ) -> None :
        self.style : list[ str ] = [ "<" , ">" , "+" , "-" , "," , "." , "[" , "]" ]
        self.goto : dict[ int , int ] = {}
        self.memory : list[ int ] = [ 0 ]
        self.position : int = 0
        self.index : int = 0
        self.code : str = ""

    def get_goto( self , code : str | None = None ) -> dict[ int , int ] :
        if code is None : code = self.code
        goto = {}
        for index in range( len( code ) ) :
            text = code[ index ]
            if text == "[" : goto[ index ] = code.index( "]" , index , -1 )
            elif text == "]" : goto[ index ] = code.rindex( "[" , 0 , index )
        return goto

    def load( self , code : str ) -> None :
        self.code , code = code , ""
        for line in self.code.splitlines() : code += "".join( filter( lambda text : text in self.style , line.split( "#" )[ 0 ] ) )
        start = code.count( "[" )
        end = code.count( "]" )
        num = abs( start - end )
        if start > end : code = code.replace( "[" , "" , num )
        elif start < end : code = code[ : : -1 ].replace( "]" , "" , num )[ : : -1 ]
        self.goto = self.get_goto( code )
        self.code = code

    def run( self ) :
        while self.position < len( self.code ) : self.main()

    def main( self ) :
        match self.code[ self.position ] :
            case "<" : self.left()
            case ">" : self.right()
            case "+" : self.plus()
            case "-" : self.minus()
            case "," : self.input()
            case "." : self.output()
            case "[" : self.begin()
            case "]" : self.end()
        self.position += 1

    def left( self ) -> None :
        if self.index > 0 : self.index -= 1

    def right( self ) -> None :
        self.index += 1
        if len( self.memory ) <= self.index : self.memory.append( 0 )

    def plus( self ) -> None :
        self.memory[ self.index ] += 1

    def minus( self ) -> None :
        self.memory[ self.index ] -= 1

    def input( self ) -> None :
        try : num = ord( input()[ : 1 ] )
        except : num = 0
        self.memory[ self.index ] = num

    def output( self ) -> None :
        print( chr( self.memory[ self.index ] ) , end = "" )

    def begin( self ) -> None :
        if not self.memory[ self.index ] : self.position = self.goto[ self.position ]

    def end( self ) -> None :
        self.position = self.goto[ self.position ] - 1
