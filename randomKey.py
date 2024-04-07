import os 
import sys
def generateSecretKey(length):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-@()=_'
    secret_key = ''.join([allowed_characters[ord(os.urandom(1)) % len(allowed_characters)] for _ in range(length)])

    return secret_key

if len(sys.argv) > 1:
    try:
        # Intenta convertir el argumento a un entero
        key_length = int(sys.argv[1])
        if key_length <= 0:
            raise ValueError
    except ValueError:
        print("Por favor, proporcione un número entero positivo como argumento para la longitud de la clave.")
        sys.exit(1)
else:
    print("Por favor, proporcione un argumento para la longitud de la clave.")
    sys.exit(1)
    
    
secretKey = generateSecretKey(key_length)
print(secretKey)