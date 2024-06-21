from pathlib import Path
from PIL import ImageTk, Image
from tkinter import Tk, Canvas, Button, PhotoImage, Label, IntVar
from tigrinho import robozinho, FailSafeException
from pyautogui import FailSafeException
from time import sleep
from utils import abrirLinkSelenium, tratarLista, checarFailsafe
from inicializadorUsuario import inicializarUsuario


continuar_loop = False
lancadas = 0
sem_boleto = []
processo_bloqueado = []
processo_errado = []
XML_ilegivel = []
nao_lancadas = []


def ativarRobozinho():
    global continuar_loop, lancadas, qtd_lancadas, qtd_sem_boleto, qtd_processo_bloqueado, qtd_processo_errado, qtd_XML_ilegivel, qtd_nao_lancadas
    global sem_boleto, processo_bloqueado, processo_errado, XML_ilegivel, nao_lancadas

    try:
        s_boleto, proc_bloqueado, proc_errado, xml_ilegivel, n_lancadas, abortar = robozinho()
        if abortar == False:
            lancadas += 1
            qtd_lancadas.set(lancadas)
            
        sem_boleto = tratarLista(sem_boleto, s_boleto)
        processo_bloqueado = tratarLista(processo_bloqueado, proc_bloqueado)
        processo_errado = tratarLista(processo_errado, proc_errado)
        XML_ilegivel = tratarLista(XML_ilegivel, xml_ilegivel)
        nao_lancadas = tratarLista(nao_lancadas, n_lancadas)

        qtd_sem_boleto.set(len(sem_boleto))
        qtd_processo_bloqueado.set(len(processo_bloqueado))
        qtd_processo_errado.set(len(processo_errado))
        qtd_XML_ilegivel.set(len(XML_ilegivel))
        qtd_nao_lancadas.set(len(nao_lancadas))
        checarFailsafe()

    except FailSafeException:
        continuar_loop = False
        raise FailSafeException
    

def abrirGui():
    global qtd_lancadas, qtd_sem_boleto, qtd_processo_bloqueado, qtd_processo_errado, qtd_XML_ilegivel, qtd_nao_lancadas

    def rodarRobozinho():
        ativarRobozinho()
        if continuar_loop:
            window.after(1, rodarRobozinho())
            checarFailsafe()

    def comecar_loop():
        global continuar_loop
        continuar_loop = True
        rodarRobozinho()

    def responderAoClique(funcao):
        sleep(1)
        window.iconify()
        try:
            funcao()
            checarFailsafe()
        except FailSafeException:
            raise FailSafeException


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Usuario\Desktop\mark4\Imagens")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    cor_fundo = "#FFFFFF"
    window = Tk()

    robozinhoIcon = r"C:\Users\Usuario\Desktop\mark4\Imagens\robozinho.ico"
    window.iconbitmap(robozinhoIcon)
    window.geometry("788x478+390+110")
    window.title("Automação Entrada de DANFE")
    window.configure(bg = cor_fundo)

    qtd_sem_boleto = IntVar()
    qtd_processo_bloqueado = IntVar()
    qtd_processo_errado = IntVar()
    qtd_XML_ilegivel = IntVar()
    qtd_nao_lancadas = IntVar()
    qtd_lancadas = IntVar()

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 478,
        width = 788,
        bd = 0,
        highlightthickness = 0,
        relief="solid",
    )
    canvas.place(x = 0, y = 0)

    canvas = Canvas(
        window,
        bg = "#E7E7E7",
        height = 292,
        width = 788,
        bd = 0,
        highlightthickness = 0,
        relief="solid",
    )
    canvas.place(x = 0, y = 186)

    label_1_imagem = PhotoImage(
        file=relative_to_assets("imagem_lancadas.png"))
    label_1 = Label(
        window,
        image=label_1_imagem,
        )
    label_1.place(
        x=45,
        y=250,
        width=138.0,
        height=55.0
    )

    label_sub_1 = Label(
        window,
        textvariable=qtd_lancadas,
        font=("Malgun Gothic", 17, "bold"),
        fg="#207C00",
        anchor="center",
        justify="center",
        bg="#ffffff",
        relief="groove"
        )
    
    label_sub_1.place(
        x=45,
        y=306,
        width=138.0,
        height=40.0
    )

    label_2_imagem = PhotoImage(
        file=relative_to_assets("imagem_nao_lancadas.png"))
    label_2 = Label(
        window,
        image=label_2_imagem,
        )
    label_2.place(
        x=183,
        y=250,
        width=138.0,
        height=55.0
    )

    label_sub_2 = Label(
        window,
        textvariable=qtd_nao_lancadas,
        font=("Malgun Gothic", 17, "bold"),
        fg="#D30000",
        anchor="center",
        justify="center",
        bg="#ffffff",
        relief="groove"
        )
    label_sub_2.place(
        x=183,
        y=306,
        width=138.0,
        height=40.0
    )

    label_3_imagem = PhotoImage(
        file=relative_to_assets("imagem_sem_boleto.png"))
    label_3 = Label(
        window,
        image=label_3_imagem,
        )
    label_3.place(
        x=321,
        y=250,
        width=138.0,
        height=55.0
    )

    label_sub_3 = Label(
        window,
        textvariable=qtd_sem_boleto,
        font=("Malgun Gothic", 17, "bold"),
        fg="#000000",
        anchor="center",
        justify="center",
        bg="#ffffff",
        relief="groove"
        )
    label_sub_3.place(
        x=321,
        y=306,
        width=138.0,
        height=40.0
    )

    label_4_imagem = PhotoImage(
        file=relative_to_assets("imagem_processo_bloqueado.png"))
    label_4 = Label(
        window,
        image=label_4_imagem,
        )
    label_4.place(
        x=459,
        y=250,
        width=138.0,
        height=55.0
    )

    label_sub_4 = Label(
        window,
        textvariable=qtd_processo_bloqueado,
        font=("Malgun Gothic", 17, "bold"),
        fg="#000000",
        anchor="center",
        justify="center",
        bg="#ffffff",
        relief="groove"
        )
    label_sub_4.place(
        x=459,
        y=306,
        width=138.0,
        height=40.0
    )

    label_5_imagem = PhotoImage(
        file=relative_to_assets("imagem_processo_errado.png"))
    label_5 = Label(
        window,
        image=label_5_imagem,
        )
    label_5.place(
        x=597,
        y=250,
        width=146.0,
        height=55.0
    )

    label_sub_5 = Label(
        window,
        textvariable=qtd_processo_errado,
        font=("Malgun Gothic", 17, "bold"),
        fg="#000000",
        anchor="center",
        justify="center",
        bg="#ffffff",
        relief="groove"
        )
    label_sub_5.place(
        x=597,
        y=306,
        width=147.0,
        height=40.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("inicializarUsuario.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=5,
        highlightthickness=0,
        command=lambda: responderAoClique(inicializarUsuario), 
        relief="raised",
        cursor="hand2"
    )
    button_1.place(
        x=50.0,
        y=70.0,
        width=261.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("botaoPlay.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=3,
        highlightthickness=0,
        bd=3,
        command=lambda: responderAoClique(comecar_loop),
        relief="solid",
        cursor="hand2"
    )
    button_2.place(
        x=101.0,
        y=155.0,
        width=590,
        height=60
    )

    button_image_3 = PhotoImage(
    file=relative_to_assets("semBoleto.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=5,
        highlightthickness=0,
        command=lambda: abrirLinkSelenium(sem_boleto),
        relief="groove",
        cursor="hand2"
    )
    button_3.place(
        x=28,
        y=397.99999999999994,
        width=145.0,
        height=33.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("processoBloqueado.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=5,
        highlightthickness=0,
        command=lambda: abrirLinkSelenium(processo_bloqueado),
        relief="groove",
        cursor="hand2"
    )
    button_4.place(
        x=203,
        y=397.99999999999994,
        width=189.0,
        height=33.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("XMLIndecifravel.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=5,
        highlightthickness=0,
        command=lambda: abrirLinkSelenium(XML_ilegivel),
        relief="groove",
        cursor="hand2"
    )
    button_5.place(
        x=422,
        y=397.99999999999994,
        width=165.0,
        height=33.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("processoErrado.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=5, 
        highlightthickness=0,
        command=lambda: abrirLinkSelenium(processo_errado),
        relief="groove",
        cursor="hand2"
    )
    button_6.place(
        x=617,
        y=397.99999999999994,
        width=143.0,
        height=33.0
    )

    canvas.create_rectangle(
        14.999999999999886,
        21.000000000000057,
        767.9999999999999,
        406.00000000000006,
        fill="#ffffff",
        outline="")

    primeira_logo = r"C:\Users\Usuario\Desktop\mark4\Imagens\eqs_engenharia_logo.png"
    imagem_logo_direita = ImageTk.PhotoImage(Image.open(primeira_logo)) 
    label_logo_direita = Label(window, image=imagem_logo_direita, bg=cor_fundo)
    label_logo_direita.image = imagem_logo_direita
    label_logo_direita.place(x=590, y=20)


    segunda_logo = r"C:\Users\Usuario\Desktop\mark4\Imagens\LogoEQS.png"
    imagem_logo_esquerda = ImageTk.PhotoImage(Image.open(segunda_logo)) 
    label_logo_esquerda = Label(window, image=imagem_logo_esquerda, bg=cor_fundo)
    label_logo_esquerda.image = imagem_logo_esquerda
    label_logo_esquerda.place(x=340, y=5)

    window.resizable(False, False)
    window.mainloop()


