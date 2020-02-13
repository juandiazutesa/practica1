colores = ["verde", "morado", "amarillo"]
person = {"name":"juan", "lastname":"diaz", "age":"34"}

colores.append("rojo")
for value in colores:
    print (value)

for key, value in person.items():
    print(key,": ",value)
