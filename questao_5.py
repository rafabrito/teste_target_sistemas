string = str(input('Digite uma palavra ou frase para ser invertida: '))
string_aux = ''

# Inverter a string digitada
for indice in range(len(string)-1, -1, -1):
    string_aux += string[indice]
