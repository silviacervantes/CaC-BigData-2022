from tkinter import *
from tkinter import messagebox #mensaje tipo popup
import sqlite3 as sq3

#Variables globales
con = None
cur = None


''''
=======================================
          PARTE FUNCIONAL
=======================================
'''
# --- MENU BBDD ---

def conectar():
  # Vuelvo a poner global para indicarle q voy a modificarla
  global con 
  global cur
  if con == None:
    con = sq3.connect('crud.db')
    cur = con.cursor()
  messagebox.showinfo('STATUS','Conectado a la BBDD')
    
def cerrar():
  rta = messagebox.askquestion('CONFIRME','¿Desea salir dela app?')
  if rta =='yes':
    if con != None: 
      con.close()
    raiz.destroy()

# --- MENU Limpiar ---
def limpiar():
  legajo.set('')
  alumno.set('')
  email.set('')
  calificacion.set('')
  grado.set('')
  escuela.set('Seleccione')
  localidad.set('')
  provincia.set('')
  legajo_input.config(state='normal') #normal habilita para editar

# --- MENU Ayuda ---
def licencia():
  gnugpl = '''
    Licencia de uso
    bla
    bla
  '''
  messagebox.showinfo("LICENCIA",gnugpl)

def acerca():
  msj = '''
    Creado por Silvia Cervantes
    para Codo a Codo 
  '''
  messagebox.showinfo("Acerca de...",msj)

# --- CRUD ---

def borrar():
  valor = messagebox.askquestion('Borrar','¿borrar?')
  if valor == 'yes' and con != None and legajo.get()!='':
    query = "DELETE FROM alumnos WHERE legajo LiKE " + legajo.get()
    cur.execute(query)
    con.commit()
    messagebox.showinfo('STATUS','Registro eliminado')
    limpiar()

def crear():
  valor = messagebox.askquestion('Borrar','¿borrar?')
  if valor == 'yes' and con != None and legajo.get()!='':
    query = "INSERT INTO alumnos (legajo,nombre,email) VALUES({},{},{}).format()"
      
    #  WHERE legajo LiKE " + legajo.get()
    cur.execute(query)
    con.commit()
    messagebox.showinfo('STATUS','Registro eliminado')
    limpiar()

# --- Configuracion de los inputs ---
def config_input(input,fila,status='normal'):
  espaciado_inputs = {'column':1,'padx':10,'pady':10}
  pass

'''
=======================================
          INTERFAZ GRÁFICA
=======================================
'''
raiz = Tk()
raiz.geometry('270x400')
raiz.resizable(width=0, height=0) #height=1 es modifiable el tamaño
raiz.title('CRUD - Com22605')


# -------- BARRA DE MENÚ ---------
barramenu = Menu(raiz)

bbddmenu = Menu(barramenu, tearoff=False)
bbddmenu.add_command(label = 'Conectar', command=conectar)
bbddmenu.add_command(label = 'Salir',command=cerrar)

borrarmenu = Menu(barramenu, tearoff=False)
borrarmenu.add_command(label="Limpiar",command=limpiar)

ayudamenu = Menu(barramenu, tearoff=False)
ayudamenu.add_command(label="Licencia",command=licencia)
ayudamenu.add_command(label="Acerca de...",command=acerca)

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
grado = IntVar()
escuela = StringVar()
escuela.set('Seleccione')
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

grado_input = Entry(framecampos, textvariable=grado)
grado_input.grid(row=4, column=1, padx=10, pady=10)


escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=5, column=1, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=6, column=1, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=7, column=1, padx=10, pady=10)


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

gradolabel  = Label(framecampos, text="Grado:")
gradolabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


escuelalabel  = Label(framecampos, text="Escuela:")
escuelalabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

localidadlabel  = Label(framecampos, text="Localidad:")
localidadlabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

provincialabel  = Label(framecampos, text="Provincia:")
provincialabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

framecampos.pack(fill=X)


# -------- FRAME BOTONERA ---------
framebotones = Frame(raiz, bg='orchid1')


boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column=0, padx=10, pady=10)

boton_leer = Button(framebotones, text="Leer")
boton_leer.grid(row=0, column=1, padx=10, pady=10)

boton_actualizar = Button(framebotones, text="Actualizar")
boton_actualizar.grid(row=0, column=2, padx=10, pady=10)

boton_borrar = Button(framebotones, text="Borrar",command=borrar)
boton_borrar.grid(row=0, column=3, padx=10, pady=10)

#fill=x se estira todo el eje de las x
framebotones.pack(fill=X) 


# -------- FRAME PIE ---------
framecopy = Frame(raiz, bg='lemon chiffon')
framecopy.pack(fill=X)

copylabel = Label(framecopy, text='(2022) por C#22605 - BigData', bg='lemon chiffon')
copylabel.pack(side='top', padx=10, pady=5)

raiz.mainloop()
