import bf

main = bf.bf()
info = { "mem" : [ 0 ] }

while True :
    while True :
        try :
            inp = input( ">" )
        except KeyboardInterrupt :
            quit()
        if inp :
            break
    match inp :
        case "info" :
            print( info )
        case "init" :
            info = {}
        case "mem" :
            print( info[ "mem" ] )
        case _ :
            if any( s not in bf.style for s in inp ) :
                print( "style error" )
            else :
                info[ "code_p" ] = 0
                info[ "code" ] = inp
                info = main.run( info = info )
                if info[ "output" ] and info[ "output" ][ -1 ] != "\n" :
                    print()
                print( info )
