#Aldo López Barrios
#21310106   6E


import re

texto = "Temo el día en que la tecnología sobrepase nuestra humanidad"

'''Nos ayuda a buscar paabras en concreto, incluso sin necesidad de escribir por completo lo que deseamos.
Al igual que las letras o letras con acento'''

#resultado = re.findall("so....ase", texto)  
resultado = re.findall("tecnolog.a|humanidad|.emo|lacra", texto)      
print(resultado)