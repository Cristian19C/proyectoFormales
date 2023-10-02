import os
import re

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile


def update_line_numbers(event=None):
    line_numbers.config(state=NORMAL)
    line_numbers.delete(1.0, END)
    line_count = editor.get(1.0, "end-1c").count('\n') + 1
    for line in range(1, line_count + 1):
        line_numbers.insert(END, f"{line}\n")
    line_numbers.config(state=DISABLED)
    contenido = editor.get(1.0, "end-1c")
    language = detect_language(contenido)
    mensaje_text.delete(1.0, END + "-1c")  # Limpiamos el widget de mensajes
    messaje_paradigm = ""
    messaje_sintaxis = ""
    mensaje_semantica = ""
    if language:
        messaje_languaje = f"Este código parece estar escrito en {language}.\n\n"
        print("Lenguaje detectado:", language)
        paradigm = detect_paradigm(language, contenido)
        sintaxis = detect_syntax_errors(contenido, language)
        semantica = detect_semantic_errors(contenido, language)
        # semantica = ""
        print(sintaxis)
        if paradigm:
            messaje_paradigm = f"Paradigma: Programación {paradigm} \n\n"
        else:
            messaje_paradigm = "No se pudo detectar el paradigma \n\n"
        if sintaxis:
            messaje_sintaxis = f"{sintaxis} \n\n"
        else:
            messaje_sintaxis = "No hay errores de sintaxis \n\n"
        if semantica:
            mensaje_semantica = f"{semantica} \n\n"
        else:
            mensaje_semantica = "No hay errores de semantica"

    else:
        messaje_languaje = "No se pudo detectar el lenguaje con certeza."
    mensaje_text.insert(END, messaje_languaje + messaje_paradigm + messaje_sintaxis+mensaje_semantica)
    mensaje_text2.insert(END, messaje_sintaxis)


def scroll_text_sync(*args):
    editor.yview(*args)
    line_numbers.yview(*args)


def copy():
    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())


def paste():
    editor.insert(INSERT, editor.clipboard_get())


def cut():
    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")


def undo():
    editor.edit_undo()


def redo():
    editor.edit_redo()


def new():
    editor.delete(1.0, END)


def detect_language(content):
    patterns = {
        'julia': r'\b(julia|function|using|global|let|struct|importall|println)\b',
        'ruby': r'\b(ruby|require|puts|def|alias|class|elsif|module)\b',
        'perl': r'\b(perl|use|print|sub|__DATA__|__END__|rand|split|local|exec)\b'
    }

    detected_language = None

    for language, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            detected_language = language
            break

    return detected_language

def detect_syntax_errors_perl(code):
    # Expresión regular para buscar paréntesis desequilibrados
    unbalanced_parentheses_pattern = re.compile(r'^[^()]*\([^()]*$')
    # Expresión regular para buscar líneas sin punto y coma al final
    missing_semicolon_pattern = re.compile(r'[^;]\s*$')
    missing_brackets_pattern = re.compile(r'^[^\[\]]*\[[^\[\]]*$')
    # Divide el código en líneas
    lines = code.split('\n')
    # Lista para almacenar mensajes de error
    errors = []
    for line_number, line in enumerate(lines, start=1):
        if unbalanced_parentheses_pattern.search(line) and not line.strip().startswith('#'):
            errors.append(f"Error en línea {line_number}: Paréntesis desequilibrados")
        elif missing_semicolon_pattern.search(line) and not line.strip().startswith('#'):
            # La línea no termina con un punto y coma y no es un comentario
            errors.append(f"Error en línea {line_number}: Falta punto y coma al final")
        elif missing_brackets_pattern.search(line) and not line.strip().startswith('#'):
            # La línea no termina con un punto y coma y no es un comentario
            errors.append(f"Error en línea {line_number}: Corchetes desequilibrados")
    if errors:
        return "\n".join(errors)
    else:
        return "No se encontraron errores de sintaxis"
    

def detect_syntax_errors_julia(code):
    print("entro al metodo de julia")
    # Expresión regular para buscar paréntesis desequilibrados
    unbalanced_parentheses_pattern = re.compile(r'^[^()]*\([^()]*$')
    missing_brackets_pattern = re.compile(r'^[^\[\]]*\[[^\[\]]*$')
    # Divide el código en líneas
    lines = code.split('\n')

    # Lista para almacenar mensajes de error
    errors = []

    for line_number, line in enumerate(lines, start=1):
        if unbalanced_parentheses_pattern.search(line) and not line.strip().startswith('#'):
            # La línea tiene paréntesis desequilibrados y no es un comentario
            errors.append(f"Error en línea {line_number}: Paréntesis desequilibrados")
        elif missing_brackets_pattern.search(line) and not line.strip().startswith('#'):
            # La línea tiene paréntesis desequilibrados y no es un comentario
            errors.append(f"Error en línea {line_number}: Corchetes desequilibrados")
        

    if errors:
        return "\n".join(errors)
    else:
        return "No se encontraron errores de sintaxis"
    
def detect_syntax_errors_ruby(code):
    # Expresión regular para buscar paréntesis desequilibrados
    unbalanced_parentheses_pattern = re.compile(r'^[^()]*\([^()]*$')
    missing_brackets_pattern = re.compile(r'^[^\[\]]*\[[^\[\]]*$')
    # Divide el código en líneas
    lines = code.split('\n')

    # Lista para almacenar mensajes de error
    errors = []

    for line_number, line in enumerate(lines, start=1):
        if unbalanced_parentheses_pattern.search(line) and not line.strip().startswith('#'):
            # La línea tiene paréntesis desequilibrados y no es un comentario
            errors.append(f"Error en línea {line_number}: Paréntesis desequilibrados")
        elif missing_brackets_pattern.search(line) and not line.strip().startswith('#'):
            # La línea tiene paréntesis desequilibrados y no es un comentario
            errors.append(f"Error en línea {line_number}: Corchetes desequilibrados")
        

    if errors:
        return "\n".join(errors)
    else:
        return "No se encontraron errores de sintaxis"
    
# errores de sintaxis
def detect_syntax_errors(code, language):
    if language == "perl":
        return detect_syntax_errors_perl(code)
    elif language == "julia":
        return detect_syntax_errors_julia(code)
    elif language == "ruby":
        return detect_syntax_errors_julia(code)
    else:
        return "No hay errores de sintaxis"

#errores semanticos



def detect_semantic_errors(code, language):
    semantic_errors = []
    if language == "perl":
    
        # Buscar variables declaradas de manera incorrecta en el código
        incorrectly_declared_vars = re.finditer(r'(my\s+(\w+)\s*=)', code)
        
        for match in incorrectly_declared_vars:
            declaration_line = match.group(1)  # Línea de la declaración incorrecta
            variable_name = match.group(2)  # Nombre de la variable
            # Verificar si la declaración incluye el signo '$'
            if '$' not in declaration_line:
                semantic_errors.append(f"Variable '{variable_name}' declarada incorrectamente en la línea: {declaration_line}")
            # Buscar funciones que no están definidas
        pass
    elif language == "julia":
          # Buscar variables declaradas de manera incorrecta en el código de Julia
        incorrectly_declared_vars = re.finditer(r'(^\s*(?:const\s*)?(\w+)\s*=)', code, re.MULTILINE)

        for match in incorrectly_declared_vars:
            declaration_line = match.group(1)  # Línea de la declaración incorrecta
            variable_name = match.group(2)  # Nombre de la variable
            # Verificar si la declaración incluye el signo '='
            if '=' not in declaration_line:
                semantic_errors.append(f"Variable '{variable_name}' declarada incorrectamente en la línea: {declaration_line}")
        pass
    elif language == "ruby":
        incorrectly_declared_vars = re.finditer(r'(\w+)\s*=', code)

        for match in incorrectly_declared_vars:
            declaration_line = match.group(0)  # Línea de la declaración incorrecta
            variable_name = match.group(1)  # Nombre de la variable
            # Verificar si la declaración incluye el signo '='
            if '=' not in declaration_line:
                semantic_errors.append(f"Variable '{variable_name}' declarada incorrectamente en la línea: {declaration_line}")
        pass
    
    return semantic_errors




def detect_paradigm(language, content): 
    if language == "ruby":
        patterns = {
            'estructurada': r'\b(if|else|while|for|unless|until|case|when|elsif|else|do)\b',
            'funcional': r'\b(map|select|reduce|lambda|proc)\b',
            'orientada a objetos': r'\b(class|module|def|@\w+|\w+\s*=\s*\w+\.new)\b'
        }

        detected_paradigm = None

        for paradigm, pattern in patterns.items():
            if re.search(pattern, content):
                detected_paradigm = paradigm
                break

        return detected_paradigm

    elif language == "perl":
        patterns = {
            'estructurada': r'\b(if|else|while|for|foreach|until|given|when)\b',
            'funcional': r'\b(map|grep|shift)\b',
            'orientada a objetos': r'\b(package|new|bless|\$self)\b'
        }

        detected_paradigm = None

        for paradigm, pattern in patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                detected_paradigm = paradigm
                break

        return detected_paradigm


    elif language == "julia":

        patterns = {
            'estructurada': r'\b(if|else|while|for|break|continue)\b',
            'funcional': r'\b(map|filter|reduce|lambda)\b',
            'orientada a objetos': r'\b(type|mutable|immutable|struct|function|end)\b'

        }

        detected_paradigm = None

        for paradigm, pattern in patterns.items():
            if re.search(pattern, content):
                detected_paradigm = paradigm
                break

        return detected_paradigm


def open_file():
    try:
        documento = askopenfile()
        if documento:
            print("Archivo abierto con éxito")
            contenido = documento.read()
            print("Contenido leído")
            editor.delete(1.0, END)
            editor.insert(1.0, contenido)

            update_line_numbers()
            print("Mensaje insertado")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Error al abrir el archivo", str(e))


def save():
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


def about():
    messagebox.showinfo("Editor auto detector de lenguaje",
                        "El editor logra detectar si se esta usando uno de tres tipos"

                        " de lenguajes. Perl, Ruby o Julia.\n\n"

                        "Para esto se hace uso de las expresiones regulares"

                        " y algunas funciones extra.\n\n")


if __name__ == "__main__":
    ventana = Tk()

    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo     ", command=new)

    archivo.add_command(label="Abrir     ", command=open_file)

    archivo.add_command(label="Guardar     ", command=save)

    archivo.add_command(label="Salir     ", command=ventana.quit)

    menubar.add_cascade(label="Archivo", menu=archivo)

    editar = Menu(menubar, tearoff=0)

    editar.add_command(label="Deshacer     ", command=undo)

    editar.add_command(label="Rehacer     ", command=redo)

    editar.add_separator()

    editar.add_command(label="Copiar     ", command=copy)

    editar.add_command(label="Pegar     ", command=paste)

    editar.add_command(label="Cortar     ", command=cut)

    menubar.add_cascade(label="Edición", menu=editar)

    ayuda = Menu(menubar, tearoff=0)

    ayuda.add_command(label="Acerca de Bloc de notas ", command=about)

    menubar.add_cascade(label="Ayuda", menu=ayuda)

    line_numbers = Text(ventana, width=4, undo=False, state=DISABLED)
    line_numbers.pack(side=LEFT, fill=Y)

    editor = Text(ventana, undo=True)
    editor.pack(side=LEFT, fill=BOTH, expand=True)

    mensaje_text = Text(ventana, undo=False)
    mensaje_text2 = Text(ventana, undo=False)
    mensaje_text.pack(side=LEFT, fill=BOTH, expand=True)

    editor.bind("<Key>", update_line_numbers)
    editor.bind("<Configure>", update_line_numbers)
    editor.bind("<MouseWheel>", scroll_text_sync)
    editor.bind("<Button-4>", scroll_text_sync)
    editor.bind("<Button-5>", scroll_text_sync)
    editor.config(yscrollcommand=scroll_text_sync)

    ventana.title("Interprete")
    ventana.geometry("880x500")
    ventana.config(menu=menubar)
    ventana.mainloop()
