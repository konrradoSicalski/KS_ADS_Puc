#recebe uma caractere e converte para decimal, hexa e binário

caractere = input("Digite um caractere")
print("Você digitou: " + caractere)
print("Em unicode: " + str(ord(caractere)))
print("Em hexadecimal: " + (hex(ord(caractere))))
print("em binário: " + bin(ord(caractere)))

