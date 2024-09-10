# Código 5
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = "Exemplo"
print(inverter_string(string))
