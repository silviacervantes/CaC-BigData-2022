Proceso mayor_de
	Escribir "================================="
	Escribir "          Representantes"
	Escribir "================================="
	Escribir " [A] Aníbal "
	Escribir " [B] Berenice "
	Escribir " [C] Claudio "
	Escribir " [O] Voto en Blanco"
	voto_a = 0
	voto_b = 0
	voto_c = 0
	voto_o = 0
	
	Para n = 1 hasta 20 Hacer
		Escribir "Ingrese voto"
		Leer voto
		Segun voto hacer
			"A": 
				voto_a = voto_a +1
			"B":
				voto_b = voto_b+1
			"C":
				voto_c = voto_c+1
			"O":
				voto_o = voto_o +1
			De Otro Modo:
				Escribir "Opcion incorrecta"
		FinSegun
	FinPara
	Escribir "================================="
	Escribir "        Recueto de votos"
	Escribir "================================="
	Escribir "  Candidato Aníbal: ",voto_a
	Escribir "  Candidato Berenice: ",voto_b
	Escribir "  Candidato Claudio: ",voto_c
	Escribir "  Votos nulos: xx votos",voto_o
	Escribir "================================="
	ganador = voto_a
	candidato_ganador = "Anibal"
	Si voto_b > ganador Entonces
		ganador = voto_b
		candidato_ganador = "Berenice"
	SiNo
		Si voto_c > ganador Entonces
			gandor = voto_c
			candidato_ganador = "Claudio"
		SiNo
			Si voto_o > ganador Entonces
				gandor = voto_o
				candidato_ganador = "Blanco"
			FinSi
		FinSi
	FinSi
	Escribir "GANADOR:",candidato_ganador
	
	
FinProceso
