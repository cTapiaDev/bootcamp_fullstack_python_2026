import pprint

entregas = [
    ['2023-01-01', '09:00', 'Insumos básicos'],
    ['2023-02-15', '10:00', 'Utensilios de cocina'],
    ['2023-05-01', '12:00', 'Bebidas'],
]

entregas.append(['2023-01-05', '08:00', 'Verduras frescas'])

print(f"{entregas}\n")

for entrega in entregas:
    if entrega[0] == '2023-02-15':
        entrega[0] = '2023-02-16'

print(f"{entregas}\n")


for entrega in entregas:
    if entrega[2] == 'Bebidas':
        entregas.remove(entrega)


print(f"{entregas}\n")

entregas.append(['2023-12-24', '07:00', 'Carnes'])
entregas.append(['2023-12-31', '07:00', 'Lácteos'])

entregas.sort()

print(f"{entregas}\n")

pprint.pprint(entregas)