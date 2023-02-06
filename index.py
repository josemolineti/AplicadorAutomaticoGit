from tkinter import *
from tkinter import messagebox
import keyboard
import pyautogui
import sqlite3

database = sqlite3.connect('data_bases.db')
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS coordenadas (id integer,registrado integer, x_abrir integer, y_abrir integer, x_cinza integer, y_cinza integer, x_verde integer, y_verde integer, x_amarelo integer, y_amarelo integer, x_azul integer, y_azul integer, x_vermelho integer, y_vermelho integer, x_branco integer, y_branco integer)")

#cursor.execute("UPDATE coordenadas SET registrado = 0 WHERE registrado = 1")

#cursor.execute("INSERT INTO coordenadas (id) VALUES(1)")

database.commit()

def zerar_valores():
    cursor.execute("UPDATE coordenadas SET registrado = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_abrir = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_abrir = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_cinza = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_cinza = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_verde = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_verde = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_amarelo = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_amarelo = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_azul = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_azul = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_vermelho = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_vermelho = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET x_branco = 0 WHERE id = 1")
    cursor.execute("UPDATE coordenadas SET y_branco = 0 WHERE id = 1")


zerar_valores()




inicial=Tk()


def colect_points(titulo, txt, alerta, pontox, pontoy):
    messagebox.showinfo(titulo, txt)
    keyboard.wait('F12')
    x, y = pyautogui.position()
    print(x, y)
    messagebox.showwarning("Sucesso", alerta)
    cursor.execute("UPDATE coordenadas SET "+str(pontox)+" = "+str(x)+","+str(pontoy)+" = "+str(y)+" WHERE id = 1")

    database.commit()

    return 0



def register_points():
    try:

        ("UPDATE coordenadas IF(registrado = 0  SET registrado = 1 WHERE registrado >= 1")

    except NameError as erro:
        #print(erro)
        quest = messagebox.askquestion("Erro", "Você já registrou as coordenadas. \n\nDeseja registrar novamente?")
        if quest == 'Yes':
            cursor.execute("UPDATE coordenadas SET registrado = 0 WHERE id = 1")
            database.close()
            cursor.close()
        else:
            pass
    #finally:
        # cursor.execute("UPDATE coordenadas SET registrado = 0 WHERE id = 1")
        database.commit()

        messagebox.showinfo("Registrar pontos na tela","Para iniciar, esteja com o Habbo aberto e entre em algum quarto. Em seguida, aperte OK e siga os passos.")

        # COLETAR PALETA DE BALÕES
        colect_points("Paleta de Balões","1 - Coletar posição da paleta de balões, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o botão de abrir a seleção de balões (NÃO clique);\n3. Com o mouse em cima, aperte F12;","Coordenadas coletadas com SUCESSO.", "x_abrir", "y_abrir")

        # COLETAR BALÃO CINZA
        colect_points("Balão Cinza","2 - Coletar Balão cor CINZA, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão CINZA (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão CINZA coletadas com SUCESSO.", "x_cinza", "y_cinza")

        # COLETAR BALÃO VERDE
        colect_points("Balão Verde","3 - Coletar Balão cor VERDE, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão VERDE (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão VERDE coletadas com SUCESSO.", "x_verde", "y_verde")

        # COLETAR BALÃO AMARELO
        colect_points("Balão Amarelo","4 - Coletar Balão cor AMARELO, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão AMARELO (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão AMARELO coletadas com SUCESSO.", "x_amarelo", "y_amarelo")

        # COLETAR BALÃO AZUL
        colect_points("Balão Azul","5 - Coletar Balão cor AZUL, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão AZUL (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão AZUL coletadas com SUCESSO.", "x_azul", "y_azul")

        # COLETAR BALÃO VERMELHO
        colect_points("Balão Vermelho","7 - Coletar Balão cor VERMELHO, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão VERMELHO (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão VERMELHO coletadas com SUCESSO.", "x_vermelho", "y_vermelho")

        # COLETAR BALÃO BRANCO
        colect_points("Balão Branco","8 - Coletar Balão cor BRANCO, siga os passos CORRETAMENTE:\n\n1. Aperte OK;\n2. Posicione o mouse sobre o balão BRANCO (NÃO clique);\n3. Com o mouse em cima, aperte F12","Coordenadas do balão BRANCO coletadas com SUCESSO.", "x_branco", "y_branco")

        quest = messagebox.askquestion("Confirmar","Coordenadas coletadas com sucesso.\nCaso ache que algo dê errado, aperte YES para coletar novamente, e NO para prosseguir.")
        if quest == 'Yes':
            register_points()
        else:
            messagebox.showinfo("Sucesso","Suas coordenadas foram coletadas e armazenadas com sucesso.\n\nCaso não esteja funcionando corretamente, colete novamente.")





#CSS---------------------------
#Botões
tam_btn = 15
fundo_btn = "#fff"
cor_btn = "#000"
cor_bd_btn = "#00dd9b"
tam_bd_btn = 119
hei_bd_btn = 31


inicial.title("Aplicador de Cursos - DPH")
inicial.geometry("300x400")
inicial.configure(background="#fff")

Label(inicial, text="Aplicador de Cursos - DPH",background="#fff", foreground="#000", anchor=N).place(x='75',y='10',width='140',height='20')
Label(inicial, text="Primeiro acesso? - Registre os pontos:",background="#fff", foreground="#000", anchor=N).place(x='50',y='90',width='200',height='20')

btn_border = Frame(inicial, highlightbackground = cor_bd_btn, highlightthickness = 2, bd=0, width=tam_bd_btn,height=hei_bd_btn).place(x='93', y='118')
btn_point=Button(btn_border, text='Registrar', command=register_points, background=fundo_btn, foreground=cor_btn, width=tam_btn).place(x='95', y='120')


Label(inicial, text="Caso já tenha o registro:",background="#fff", foreground="#000", anchor=N).place(x='50',y='220',width='200',height='20')
btn_border1 = Frame(inicial, highlightbackground = cor_bd_btn, highlightthickness = 2, bd=0, width=tam_bd_btn,height=hei_bd_btn).place(x='93', y='248')
btn_run=Button(btn_border1, text='Iniciar', command=register_points, background=fundo_btn, foreground=cor_btn, width=tam_btn).place(x='95', y='250')


Label(inicial, text="Desenvolvido por: Juzse, o mais lindo - 2023",background="#fff", foreground="#000", anchor=N).place(x='30',y='350',width='250',height='20')

#messagebox.showinfo("Bem-vindo(a)","Bem-vindo(a) ao Aplicador de Cursos Automátido - DPH\n\nSe estiver acessando pela primeira vez, deve registrar os pontos na tela, clicando no botão -Registrar-\n\nCaso já tenha registrado, basta apertar em -Iniciar-")



inicial.mainloop()




