# Scope
continent = 'South America'

def get_continent():
    print(f"Ambiente Global detectado: {continent}")

get_continent()

# Modificar la variable global

continent = 'Asia'

print(continent)

num = 30

def modificar_continente():
    num = 10
    global continent
    continent = 'Africa'
    print(num)

modificar_continente()
print(continent)


print(num)
