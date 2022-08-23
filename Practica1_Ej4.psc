Proceso cobro
	unidad_total = 0
	Para n=1 hasta 5 Hacer
		Escribir "Ingrese unidades producidas dia",n
		Leer unidad
		unidad_total = unidad_total + unidad
	FinPara
	paga = unidad_total*1500
	Si unidad_total > 100 Entonces
		paga = paga + 7000
	FinSi
	Escribir "La paga total es de:", paga
FinProceso
