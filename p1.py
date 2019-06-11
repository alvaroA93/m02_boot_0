def sumatodos(limitTo):
    resultado=0
    for i in range(0,limitTo):
        resultado+= 1
    return resultado

def sumatodosloscuadrado(limitTo):
    resultado=0
    for i in range(limitTo+1):
        resultado+= i*i
        
    return resultado

print(sumatodos(100))
print(sumatodosloscuadrado(3))