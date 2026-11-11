# Matriz de información personal
"""
[
    ["Jehidam", "jja@test.com", 123],
    ["Dylan", "djg@test.com", 134],
    ["Julian", "jss@test.com", 145]
]
"""

datos_personales = [["Jehidam", "jja@test.com", 123], ["Dylan", "djg@test.com", 134], ["Julian", "jss@test.com", 145]]

print("Dato fila 1, índice 0:", datos_personales[1][0])
print("Dato fila 2, índice 0:", datos_personales[2][1])
print("Dato fila 0, índice 2:", datos_personales[0][2])

otros_datos = [["Jehidam", "jja@test.com", [123, 523]], ["Dylan", "djg@test.com", [134, 541]], ["Julian", "jss@test.com", [145, 124]]]
print("Dato 523:", otros_datos[0][2][1])