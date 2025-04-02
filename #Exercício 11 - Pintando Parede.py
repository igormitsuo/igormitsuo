# Exercício Python #011 - Pintando Parede#
a= float(input("altura da parede em metros"))
l= float(input("largura da parede em metros"))
area=l*a
litros= area/2
print("sua parede tem a dimenção de {} x {} metros e a area é de {} m²".format(a,l,area))
print("para pintar essa parede, voce precisara de {} litros de tinta".format(litros))