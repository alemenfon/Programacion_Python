'''
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.
'''



palabraBuscada="hola"
cadena="shybaoxlna"
def encontrarPalabra(cadena):
    palabraEscondida=True
    palabraEncontrada=""
    for c in cadena:
        for l in palabraBuscada:
            if c==l:
                palabraEncontrada+=(c)   
    return palabraEscondida

print(encontrarPalabra(cadena))
   
            
                
          
    


    
            
            
    