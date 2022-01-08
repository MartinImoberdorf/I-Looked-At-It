from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sqlite3
import time


def Crear_BBDD():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()

    try:
        cursor.execute("""CREATE TABLE Data(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Hora Text,
                Dia Text,
                Titulo text,
                Tipo text

                )""")
    except:      
        pass

def limpiarCampos():
    tituloEntry.set("")
    comboBoxOpcion.set("")

def Registrar():
    if tituloEntry.get()=="" or comboBoxOpcion.get()=="":
        messagebox.showwarning("Información","No se pueden dejar campos vacíos")
    else:
        horaIngreso=time.strftime('%H:%M:%S', time.localtime())
        diaIngreso=date.today()

        conexion=sqlite3.connect('BBDD')

        cursor=conexion.cursor()
  
        hora=str(horaIngreso)
        dia=str(diaIngreso)
        titulo=tituloEntry.get()
        tipo=comboBoxOpcion.get()

        mensaje="¿Desea registrar {} en la base de datos?".format(titulo)

        try:
            opcion=messagebox.askquestion(message=mensaje)
            if opcion=="yes":
                cursor.execute("INSERT INTO Data(Hora,Dia,Titulo,Tipo) VALUES (?,?,?,?)",(hora,dia,titulo,tipo))
                messagebox.showinfo("Información","Se han registrado los datos correctamente.")
                limpiarCampos()
        except:
            pass
        
        conexion.commit()
        conexion.close() 

def verificar():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()

    titulo=tituloEntry.get()

    cursor.execute("SELECT * FROM Data")

    data=cursor.fetchall()

    for i in data:
        if i[3]==titulo:
            mensaje="Se ha encontrado la {} , {} registra el día {} a las {}".format(i[4],i[3],i[2],i[1])
            messagebox.showinfo("Información",mensaje)
          
def ocultarBoton():
    botonNuevo1.destroy()     



def main():
    Crear_BBDD()

    root=Tk()

    ancho_ventana =450
    alto_ventana= 180

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="black")
    root.title("")
    root.resizable(width=False,height=False)
    root.iconbitmap('Imgs/Logo.ico')

    global botonNuevo1
    img = PhotoImage(file='Imgs/LogoMain.png')
    botonNuevo1 = Button(text="test",image=img,bg="yellow",command=ocultarBoton)
    botonNuevo1.pack(expand=True)
    botonNuevo1.config(bg="black",activebackground="black",activeforeground="black",highlightbackground="black")

    #Frame de Entrys y Labels

    miFrame=Frame(root)
    miFrame.configure(background='black')
    miFrame.pack()

    global tituloEntry
    tituloEntry=StringVar()

    cuadroTitulo=Entry(miFrame,textvariable=tituloEntry,width=25)
    cuadroTitulo.grid(row=1,column=1 , padx=5,pady=12)
    cuadroTitulo.config(justify="left",font=("Bahnschrift SemiBold Condensed",15))

    global comboBoxOpcion
    comboBoxOpcion=ttk.Combobox(miFrame,values=["Película","Serie"],width=23,state="readonly")
    comboBoxOpcion.grid(row=2,column=1, sticky="w", padx=5,pady=12)
    comboBoxOpcion.config(justify="left",font=("Bahnschrift SemiBold Condensed",15))


    tituloLabel=Label(miFrame, text="TÍTULO :",width=10)
    tituloLabel.grid(row=1,column=0, sticky="e" , padx=5, pady=12)
    tituloLabel.config(bg="black",fg="white",justify="left",font=("Bahnschrift SemiBold Condensed",15))

    tipoLabel=Label(miFrame, text="TIPO :",width=10)
    tipoLabel.grid(row=2,column=0, sticky="e" , padx=5, pady=12)
    tipoLabel.config(bg="black",fg="white",justify="left",font=("Bahnschrift SemiBold Condensed",15))



    #Frame de botones
    miFrame2=Frame(root)
    miFrame2.configure(background="black")
    miFrame2.pack()

    buton=Button(miFrame2,text="Registrar",width=20,command=Registrar)
    buton.grid(row=4,column=1, sticky="w" , padx=10, pady=10)
    buton.config(background="white",justify="left",font=("Bahnschrift SemiBold Condensed",15))

    buton2=Button(miFrame2,text="Verificar",width=20,command=verificar)
    buton2.grid(row=4,column=2, sticky="e" , padx=10, pady=10)
    buton2.config(background="white",justify="left",font=("Bahnschrift SemiBold Condensed",15))

    root.mainloop()


if __name__ == '__main__':
    main()