import os
import re

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.scrolledtext import ScrolledText  # Use ScrolledText for text with scrollbar
from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound


def update_line_numbers(event=None):
    line_numbers.config(state=NORMAL)
    line_numbers.delete(1.0, END)
    line_count = editor.get(1.0, "end-1c").count('\n') + 1
    for line in range(1, line_count + 1):
        line_numbers.insert(END, f"{line}\n")
    line_numbers.config(state=DISABLED)

def scroll_text_sync(*args):
    editor.yview(*args)
    line_numbers.yview(*args)

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

def detect_language(content):
    patterns = {
        'julia': r'\b(julia|end|function|if|else)\b',
        'perl': r'\b(perl|print|sub|if|else)\b',
        'ruby': r'\b(ruby|puts|def|if|else)\b'
    }

    detected_language = None

    for language, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            detected_language = language
            break

    return detected_language

def abrir():
    try:
        documento = askopenfile()
        if documento:
            print("Archivo abierto con éxito")
            contenido = documento.read()
            print("Contenido leído")
            editor.delete(1.0, END)
            editor.insert(1.0, contenido)

            detected_language = detect_language(contenido)
            mensaje_text.delete(1.0, END + "-1c")  # Limpiamos el widget de mensajes
            if detected_language:
                mensaje = f"Este código parece estar escrito en {detected_language}."
                print("Lenguaje detectado:", detected_language)
            else:
                mensaje = "No se pudo detectar el lenguaje con certeza."
            # mensaje_text.insert(END, "prueba uno")
            mensaje_text.insert(END, mensaje)
            print("Mensaje insertado")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Error al abrir el archivo", str(e))

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

    

    line_numbers = Text(ventana, width=4, undo=False, state=DISABLED)
    line_numbers.pack(side=LEFT, fill=Y)


    


    editor = Text(ventana, undo="true")
    editor.pack(side=LEFT, fill=BOTH, expand=True)

    mensaje_text = Text(ventana, undo=False)
    mensaje_text.pack(side=LEFT, fill=BOTH, expand=True)

    editor.bind("<Key>", update_line_numbers)
    editor.bind("<Configure>", update_line_numbers)
    editor.bind("<MouseWheel>", scroll_text_sync)
    editor.bind("<Button-4>", scroll_text_sync)
    editor.bind("<Button-5>", scroll_text_sync)
    editor.config(yscrollcommand=scroll_text_sync)

    ventana.title("Interprete")
    ventana.geometry("800x500")
    ventana.config(menu=menubar)
    ventana.mainloop()