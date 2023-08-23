import os
from tkinter import *

from tkinter import messagebox

from tkinter.filedialog import askopenfile, asksaveasfile



def copiar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

def pegar():

    editor.insert(INSERT, editor.clipboard_get())

def cortar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")

def deshacer():

    editor.edit_undo()

def rehacer():

    editor.edit_redo()

def nuevo():

    editor.delete(1.0,END)

def abrir():

    documento = askopenfile(filetypes=[("Archivo de pearl","*.pl"), ("Archivo de julia","*.jl"), ("Archivo de ruby","*.rb")])

    editor.delete(1.0, END)
    editor.insert(1.0, documento.read())

def guardar():
    opciones = [("Documento de pearl", "*.pl"), ("Documento de julia", "*.jl"), ("Documento de ruby", "*.rb")]
    documento = asksaveasfile(filetypes=opciones, defaultextension=".pl")

    if documento:
        contenido = editor.get(1.0, END)
        documento_nombre = documento.name
        extension_documento = os.path.splitext(documento_nombre)[1]

        if extension_documento:
            documento.write(contenido)
            documento.close()
            print(f"Documento guardado con extensión: {extension_documento}")
        else:
            print("No se especificó una extensión al guardar.")

def acerca():

    messagebox.showinfo("Acerca de Bloc de notas Codigazo", "Bloc de notas Codigazo es un lector de archivos de texto plano,"

                                                         " realizar una aplicación de este tipo ayuda al estudiante a practicar"

                                                         " el uso de interfaces gráficas, la manipulación de archivos de texto"

                                                         " y algunas funciones extra."

                                                         "\n\n"

                                                         "A pesar de ser sencillo tenemos 2 funcionalidades que no tiene el"

                                                         " bloc de notas de Windows, la primera es la opción de rehacer,"

                                                         " la segunda característica es que se puede deshacer o rehacer tantas veces"

                                                         " como se desee a diferencia del bloc denotas de Windows que solo permite"

                                                         " deshacer 2 veces y la segunda cuenta como un rehacer.")





if __name__ == "__main__":



    ventana = Tk()



    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo     ", command=nuevo)

    archivo.add_command(label="Abrir     ", command=abrir)

    archivo.add_command(label="Guardar     ", command=guardar)

    archivo.add_command(label="Salir     ", command=ventana.quit)

    menubar.add_cascade(label="Archivo", menu=archivo)



    editar = Menu(menubar, tearoff=0)

    editar.add_command(label="Deshacer     ", command=deshacer)

    editar.add_command(label="Rehacer     ", command=rehacer)

    editar.add_separator()

    editar.add_command(label="Copiar     ", command=copiar)

    editar.add_command(label="Pegar     ", command=pegar)

    editar.add_command(label="Cortar     ", command=cortar)

    menubar.add_cascade(label="Edición", menu=editar)



    ayuda = Menu(menubar, tearoff=0)

    ayuda.add_command(label="Acerca de Bloc de notas ", command=acerca)

    menubar.add_cascade(label="Ayuda", menu=ayuda)



    editor = Text(ventana, undo="true")

    editor.pack(side=TOP, fill=BOTH, expand=1)



    ventana.title("Codigazo: Bloc de notas")

    ventana.geometry("800x500")

    ventana.config(menu=menubar)

    ventana.mainloop()