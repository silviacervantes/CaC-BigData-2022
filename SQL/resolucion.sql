USE educa22605;
#1) Seleccionar todos los datos de la tabla alumnos:
# SELECT * FROM alumnos;

#2) Seleccionar solamente el legajo y el nombre de los alumnos:
# SELECT legajo, nombre FROM alumnos;

#3) Mostrar todos los datos de aquellos alumnos aprobados (con notas mayores o iguales a 7)
# SELECT * FROM alumnos WHERE nota >=7;

#4) Mostrar el id y el nombre de aquellas escuelas cuya capacidad sea inferior a 200 (no mostrar la columna capacidad).
#SELECT id, nombre FROM escuelas WHERE capacidad <200;
#5) Mostrar el nombre y la nota de aquellos alumnos cuya nota se encuentre entre 8 y 10
#SELECT nombre,nota FROM alumnos WHERE nota >= 8 AND nota <= 10;

#6) Repetir el ejercicio anterior, utilizando BETWEEN
#SELECT nombre,nota FROM alumnos WHERE nota BETWEEN 8 AND 10;

#7) Mostrar el nombre, la localidad y la provincia de aquellas escuelas situadas en Buenos Aires o Jujuy
#SELECT nombre, localidad, provincia FROM escuelas WHERE provincia IN ('Buenos Aires', 'Jujuy');

