from tkinter import *
raiz = Tk()
raiz.title('Python CRUD ')

#MENU
barramenu = Menu(raiz)

bbddmenu = Menu(barramenu,tearoff=False)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Salir')

borrarmenu = Menu(barramenu,tearoff=False)
borrarmenu.add_command(label='Limpiar')

ayudamenu = Menu(barramenu,tearoff=False)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de...')

barramenu.add_cascade(label='BBDD',menu=bbddmenu)
barramenu.add_cascade(label='Limpiar',menu=borrarmenu)
barramenu.add_cascade(label='Ayuda',menu=ayudamenu)

raiz.config(menu = barramenu)

#CAMPOS FORMULARIO
framecampos = Frame(raiz)

#variables de entrada
legajo = StringVar()
alumno = StringVar()

#inputs
legajo_input = Entry(framecampos,textvariable = legajo)
legajo_input.grid(row=0, column=1,padx=10,pady=10)

legajo_input = Entry(framecampos,textvariable = alumno)
legajo_input.grid(row=1, column=1,padx=10,pady=10)

#labels
legajolabel = Label(framecampos,text='Legajo:') 
legajolabel.grid(row=0, column=0,sticky="w",padx=10, pady=10)

legajolabel = Label(framecampos,text='Alumno:') 
legajolabel.grid(row=1, column=0,padx=10, pady=10)

framecampos.pack()

#BOTONES
framebotones = Frame(raiz)

boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column=0, sticky = 'e',padx=10, pady='10')

boton_leer = Button(framebotones, text='Leer')
boton_leer.grid(row=0, column=1, sticky = 'e',padx=10, pady='10')

boton_modificar = Button(framebotones, text='Modificar')
boton_modificar.grid(row=0, column=2, sticky = 'e',padx=10, pady='10')

boton_borrar = Button(framebotones, text='Borrar')
boton_borrar.grid(row=0, column=3, sticky = 'e',padx=10, pady='10')

framebotones.pack()

#FRAME PIE
framecopy = Frame(raiz)
copylabel= Label(framecopy, text='COPYRIGHT')
copylabel.grid(pady=10)
framecopy.pack()
raiz.mainloop()
