import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyqrcode

def createqr(data): #Def que cria o qrCode
    qr = pyqrcode.create(data)
    qr.png("qr.png", scale=6)
    print('Código QR criado com sucesso!')

def input_window():
    root = tk.Tk()
    root.geometry("600x400") #Escolhe o tamanho da Janela
    root.title("QRCode Creator") #Título da janela

    label = ttk.Label(root, text="Paste URL:") #Texto acima do input
    label.pack(pady=15,side="top") #Configuração do texto

    input_entry = ttk.Entry(root, width=40) #Input de link para criar o qrCode
    input_entry.pack(pady=20,side="top") #Configuração do input

    def onSubmit(): #Def para quando apertar o botão de submit
        data = input_entry.get() #Pega o link colocado no input e coloca na variavel data
        createqr(data) #Usa a def "createqr" com argumento data para criar o qrcode
        tkinter.messagebox.showinfo("Success", "The QR code was created with ease!") #Mostra uma mensagem dizendo que foi um sucesso a criação
        input_entry.delete(0, tk.END)

    submit_button = ttk.Button(root, text="Submit", command=onSubmit, width=25, cursor='tcross') #Botão de submit
    submit_button.pack(pady=25,side="bottom") #Configuração do botão de submit

    root.mainloop() #Loop para não fechar a janela

if __name__ == "__main__":
    input_window()
