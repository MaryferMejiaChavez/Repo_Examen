                    ########################################
                    #           EXAMEN UNIDAD 3            # 
                    #    PROGRAMACIÓN LÓGICA Y FUNCIONAL   #
                    ########################################
                    
                    
                    
########################################
#Garcia Sabino Montserrat              #
#Mejia Chavez Maria Fernanda           #
########################################
"""

 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
"""
print('opcion 2')
print('')
def generador1(M):
	j=1
	i=1
	c=0
	while i<(M+1):
		while j<(M+1):
			if i%j==0:
				c=c+1
			j=j+1
		if c == 2:
			yield i
		c=0
		i=i+1
		j=1
a=[z for z in generador1(30)]
print("Numeros primos")
print(a)
"""
Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
print(' B A D A B O O M ')	
def genBadaBoom(max):
	i=1
	while i<max:
		if i%3 ==0 and i%5==0:
			yield "Bada Boom!!"
		elif i%3==0:
			yield "Bada"
		elif i%5==0:
			yield "Boom"
		else:
			yield i
		i = i + 1
a = genBadaBoom(31)
z = [e for e in a]
print(z)

"""
Combinaciones <Comprensión de listas> 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print ('')
print(' C O M B I N A C I O N   D E   C O N J U N T O S ')	
C=['roja','negra','azul','morada','cafe']
P=['negro','azul','cafe','obscuro','crema']
A=['cinturon','tirantes', 'lentes', 'fedora']
print([(x, y, z) for x in C for y in P for z in A])
R=[(x, y, z) for x in C for y in P for z in A]
print("Cantidad de combinaciones")
print(len(R))
print('')

"""
    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
	
	
"""
print ('')
print(' C O M B I N A C I O N   D E   C O N J U N T O S ** F E D O R A ** ')	
C=['roja','negra','azul','morada','cafe']
P=['negro','azul','cafe','obscuro','crema']
A=['cinturon','tirantes', 'lentes', 'fedora']
print([(x, y, z) for x in C for y in P for z in A if z=='fedora'])
R=[(x, y, z) for x in C for y in P for z in A if z=='fedora']
print("Cantidad de combinaciones")
print(len(R))
print('')
