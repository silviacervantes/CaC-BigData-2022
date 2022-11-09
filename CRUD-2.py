from tkinter import *

'''
=======================================
          INTERFAZ GRÁFICA
=======================================
'''
raiz = Tk()
raiz.geometry('270x360')
raiz.resizable(width=0, height=0)
raiz.title('CRUD - Com22605')


# -------- BARRA DE MENÚ ---------
barramenu = Menu(raiz)

bbddmenu = Menu(barramenu, tearoff=False)
bbddmenu.add_command(label = 'Conectar')
bbddmenu.add_command(label = 'Salir')

borrarmenu = Menu(barramenu, tearoff=False)
borrarmenu.add_command(label="Limpiar")

ayudamenu = Menu(barramenu, tearoff=False)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de...")

barramenu.add_cascade(label='BBDD', menu = bbddmenu)
barramenu.add_cascade(label="Limpiar", menu=borrarmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

raiz.config(menu = barramenu)

# -------- FRAME CAMPOS ---------
framecampos = Frame(raiz, bg='skyblue1')

'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''
legajo = StringVar()
alumno = StringVar()
email =  StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

legajo_input = Entry(framecampos, textvariable = legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10, pady=10)


# -------- LABELS ---------
'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

# Apunte: posicionamiento de elemento en tkinter:
# https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/

# USAMOS EL MÉTODO DE GRILLA PARA EL POSICIONAMIENTO

legajolabel = Label(framecampos, text='Legajo:')
legajolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

alumnolabel  = Label(framecampos, text="Alumno:")
alumnolabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

emaillabel  = Label(framecampos, text="Email:")
emaillabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

calificacionlabel  = Label(framecampos, text="Calificación:")
calificacionlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

escuelalabel  = Label(framecampos, text="Escuela:")
escuelalabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

localidadlabel  = Label(framecampos, text="Localidad:")
localidadlabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

provincialabel  = Label(framecampos, text="Provincia:")
provincialabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

framecampos.pack(fill=X)


# -------- FRAME BOTONERA ---------
framebotones = Frame(raiz, bg='orchid1')


boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column=0, padx=10, pady=10)

boton_leer = Button(framebotones, text="Leer")
boton_leer.grid(row=0, column=1, padx=10, pady=10)

boton_actualizar = Button(framebotones, text="Actualizar")
boton_actualizar.grid(row=0, column=2, padx=10, pady=10)

boton_borrar = Button(framebotones, text="Borrar")
boton_borrar.grid(row=0, column=3, padx=10, pady=10)

framebotones.pack(fill=X)


# -------- FRAME PIE ---------
framecopy = Frame(raiz, bg='lemon chiffon')
framecopy.pack(fill=X)

copylabel = Label(framecopy, text='(2022) por C#22605 - BigData', bg='lemon chiffon')
copylabel.pack(side='top', padx=10, pady=5)

raiz.mainloop()
