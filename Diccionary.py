#diccionario
coders = {
    1: {
        "id": 1048229292,
        "nombre": "Jander",
        "apellido": "Arguello",
        "edad": 30,
        "nvlIngles": "-A0"
    },
    2: {
        "id": 1048229296,
        "nombre": "Luisa",
        "apellido": "De la Rosa",
        "edad": 19,
        "nvlIngles": "C30"
    },
    3: {
        "id": 1048229297,
        "nombre": "Maria",
        "apellido": "Sanchez",
        "edad": 19,
        "nvlIngles": "C1"
    }
}


'''print(coders)

nombre = input("dig un nombre: ")

#Nuevo coder

coders[4] = {"id":100203033,"nombre":nombre, "apellido":"Guzman","edad": 20, "nvlIngles": "B2"}

print("imprimiendo luego de añadir otro coder\n")

print(coders)

print("Buscando el nombre de un coder especifico")

print(coders[4])

print("Buscando con el metodo get")

print(coders.get(11, "No encontrado"))



print("Buscando por numero de documento")

busqueda_id = 1048229292
coder_encontrado = None

for llave, coder in coders.items():
    if coder["id"] == busqueda_id:
        coder_encontrado = coder

print(coder_encontrado)


for j, k in coders.items():
    if k["id"] == busqueda_id:
        print("Encontrado")'''

#Para buscar un coder por ID
def buscar_por_id(coders, busqueda_id):
    coder_encontrado = None
    
    for llave, coder in coders.items():

        if coder["id"] == int("busqueda_id"):
            coder_encontrado = coder
           
            
    return coder_encontrado

print (buscar_por_id)