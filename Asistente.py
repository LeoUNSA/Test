#Importamos las librerias previamente instaladas
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import os
import tkinter as tk
#Nombre del asistente (inicializado asi), no importante.
name='asistente'
listener=sr.Recognizer() #La función Recognizer hace que nos pueda escuchar.
engine=pyttsx3.init() #Con esta liena de código podemos inicializar el asistente.
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #Establecemos la voz del asistente (al leer dialogos, por ejemplo).
wikipedia.set_lang('es')
def talk(text): #Función para que el asistente hable.
    engine.say(text)
    engine.runAndWait()
def listen(texto): #Función para que el asistente escuche.
    try:
        with sr.Microphone() as source: #Asignamos la fuente de inputs (micrófono).
            print(texto)
            voice=listener.listen(source)
            #Al hablar las palabras se almacenan como texto en la variable rec y se transforman a texto en solo minúsculas.
            rec=listener.recognize_google(voice,language='es-PE')#Hacemos que la libreria trabaje con el Español-Peru (ya que por defecto reconoce dialogos en inglés).
            rec=rec.lower()
            if name in rec:
                rec=rec.replace(name,'') #Eliminamos el nombre del asistente del texto almacenado en la variable rec.
                print('Usted dijo: '+rec)
    except:
        pass
    return rec
def run():
    #Reproducción de videos en Youtube
    rec=listen('Esperando ordenes...')
    if 'reproduce' in rec: #Al escuchar la palabra 'reproduce' (usada normalmente para hacer referencia a contenido multimedia) se ejecuta el bloque de código:
        yt=rec.replace('reproduce','') #Eliminamos la palabra reproduce de la variable rec para evitar su búsqueda
        talk('Reproduciendo'+yt)
        pywhatkit.playonyt(yt)
        run()
    #Información de algo en wikipedia:
    elif 'información de' in rec:
        inf=rec.replace('información de ','')
        rpta=wikipedia.summary(inf,sentences=1)
        talk(rpta)
        run()
    #Hora actual:
    elif 'dime la hora actual' in rec: #Palabras de llamado de la función:
        hora=datetime.datetime.now().strftime('%I:%M %p') #Almacenamos la hora actual en la variable hora
        talk("Son las "+hora) #Salida usando la función talk
        run()
    #Fecha actual
    elif 'dime la fecha actual' in rec: #Palabras de llamado de la función
        fecha=datetime.datetime.now().strftime('%d/%m/%Y') #Almacenamos la fecha actual en la variable hora
        talk("El día de hoy es el "+fecha) #Salida usando la función talk
        run()
    #Búsqueda en el navegador
    elif 'busca' in rec:
        order=rec.replace('busca','')
        talk('Buscando '+order)
        pywhatkit.search(order)
        run()
    #Captura de pantalla
    elif 'captura de pantalla' in rec:
        talk('Sacando captura')
        pywhatkit.take_screenshot('Captura')
        run()
    #Ejecuciíon de algún programa.
    elif 'ejecuta' in rec: #Palabras de llamado de la función
        order=rec.replace('ejecuta','')
        talk('Ejecutando '+order)
        app=order+'.exe'
        os.system(app)
        run()
    #Creación de carpetas
    elif 'crea la carpeta' in rec: #Palabras de llamado de la función
        #Definimos el directorio en el que se crearán las carpetas
        home="C:/Users/Leo\Documents/Tareas/ProyectoArq/CarpetasProyecto/"
        order=rec.replace('crea la carpeta ','')
        if os.path.exists(order): #Comprobando si existe o no la carpeta
            talk('La carpeta ya existe') #Si existe previamente, no se crea.
            run()
        else:
            mrk=os.mkdir(home+order) #Si no existe previamente, se crea la carpeta.
            talk('Carpeta creada satisfactoriamente')
            run()
    #Eliminar carpetas
    elif 'elimina la carpeta' in rec:
        order=rec.replace('elimina la carpeta ','')
        if os.path.exists(order):
            rd=os.rmdir(order)
            talk('Carpeta eliminada satisfactoriamente')
            run()
        else:
            talk('La carpeta no existe')
            run()
    #Creacion de archivos de texto (.txt)
    elif 'crea el archivo' in rec:
        order=rec.replace('crea el archivo ','')
        order=order+'.txt'
        if os.path.exists(order):
            talk('El archivo ya existe')
            run()
        else:
            archivo=open(order,'w')
            archivo.close()
            talk('El archivo fue creado satisfactoriamente')
            run()
    #Borrar archivos de texto (.txt) (No del todo funcional).
    elif 'elimina el archivo' in rec:
        order=rec.replace('elimina el archivo ','')
        order=order+'.txt'
        if os.path.exists(order):
            os.remove(order)
            talk('Archivo eliminado satisfactoriamente')
            run()
        else:
            talk('El archivo no existe')
            run()
    #Redireccionamiento hacia sitios web
    elif 'inicia dutic' in rec:
        case=rec.replace('inicia dutic', '')
        talk("Entrando "+case)
        webbrowser.open("https://dutic.unsa.edu.pe/#/homepage")
        run()
    elif 'adiós' in rec:
        talk("Hasta la próxima")
        pass
    else:
        talk("No te he logrado entender") #Mensaje en caso el asistente no haya entendido la orden o no sea un comando válido
        run() 
#Interfaz simple implementada con Tkinter
asistente=tk.Tk()
asistente.geometry("700x300")
asistente.configure(background="black")
tk.Wm.wm_title(asistente, "Asistente virtual")
tk.Button(
    asistente,
    font=("Courier",14),
    text="Haz click en cualquier parte de la pantalla para empezar.",
    fg="white",
    bg="black",
    justify="center",
    command=run
).pack(
    fill=tk.BOTH,
    expand=True,
)
asistente.mainloop()
#Inicializador del proyecto:
if __name__ == "__main__":
    run()