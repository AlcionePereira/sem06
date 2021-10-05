def numero(n):
    
    if n >= '0' and n <= '9' :
        
        return True
    
    else:
        
        return False



num = input()
resultado = numero(num)
print(resultado)
