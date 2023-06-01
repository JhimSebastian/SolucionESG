from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

def solucionarEcuacion (a,b,c) :
    solucion.definirParametros ( a , b , c )
    solucion.solucionESG ( )
    solucion.imprimirSolución ( )

if __name__ == '__main__':
    solucion = EcuacionSegundoGrado ( )

    solucionarEcuacion ( 1 , 2 , 1 )
    solucionarEcuacion ( 1 , 2 , 3 )
    solucionarEcuacion ( "1" , "2" , "1" )
    solucionarEcuacion ( "a" , "b" , "c" )

