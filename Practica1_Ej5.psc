Proceso mayor_de
	Escribir "Ingrese numero 1:"
	Leer nro_1
	Escribir "Ingrese numero 2:"
	Leer nro_2
	Escribir "Ingrese numero 3:"
	Leer nro_3
	
	mayor = nro_1
	Si nro_2 > mayor Entonces
		mayor = nro_2 
	Sino 
		Si nro_3 > mayor Entonces
			mayor = nro_3
		FinSi
	FinSi
	Escribir "El mayor de los TRES es:",mayor

FinProceso
