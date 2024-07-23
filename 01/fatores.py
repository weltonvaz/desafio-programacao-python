from sympy import divisors, divisor_count

def fatores_primos(numero):
    fatores = []
    a = divisors(numero)
    a.remove(1)
    for i in a:
        if (divisor_count(i)) == 2:
            fatores.append(i)
    return fatores
            
# comandos usados na vídeo para referência
if __name__ == '__main__':
    print(fatores_primos(630))  # [2, 3, 3, 5, 7]
    print(fatores_primos(13))  # [13]            
    
    
    