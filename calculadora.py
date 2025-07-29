import customtkinter as ctk # Importa a biblioteca CustomTkinter para criar a interface gráfica.
from tkinter import * # Importa todas as funcionalidades do Tkinter (base do CustomTkinter).
from tkinter import messagebox # Importa o módulo messagebox para exibir caixas de diálogo.


# Define a aparência padrão da interface customtkinter. ('light', 'dark', 'system')
ctk.set_appearance_mode("dark")


# Criação da janela.
janela = ctk.CTk()

# Lista contendo os botões da calculadora.
botoes = ["C", "%", "/",
          "7", "8", "9","*",
          "4", "5", "6", "-",
          "1", "2", "3", "+",
          "0", ".", "="]

 

# Esta classe gerencia a construção e a lógica da calculadora,
# incluindo a criação da interface, botões e manipulação de eventos.
class application():

    def __init__(self):
        """
        Inicializa a aplicação da calculadora, configurando a janela,
        a entrada de texto e os botões.
        """
        self.window = janela
        self.tela()
        self.entrada()
        self.buttons()
        self.window.mainloop() # Faz com que a janela fique aberta em um loop.


    def click_button(self, button):
        """
         Processa o clique nos botões da calculadora.
        Gerencia a lógica de limpar, calcular e exibir erros.

        Args:
        button (str): O texto do botão que foi clicado.
        """
        text = button

        if text == "C":
            self.entrada.delete(0, END)

        elif text == "=":
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, END)
                self.entrada.insert(END, str(resultado))

            except SyntaxError:
                messagebox.showerror(self.window, message="Sintaxe Incorreta!")
            except ZeroDivisionError:
                messagebox.showerror(self.window, message="Divisão por zero!")


        else:
            self.entrada.insert(END, text)



    def tela(self):
        """ Configurações de titulo, tamanho (geometria) e define que a janela não possa ser esticada na horizontal e vertical."""
        self.window.title("Calculadora simples")
        self.window.geometry("350x450")
        self.window.resizable(False, False)


    def entrada(self):
        """ Define a entrada da interface gráfica responsável por exibir os valores inseridos pelo usuário e o resultado final."""
        self.entrada = ctk.CTkEntry(master=self.window, font=("Helvetica", 30), width= 350, height=60)
        self.entrada.grid(row=0, column=0, columnspan=4, sticky=W)


    def buttons(self):
        """
        Cria e posiciona os botões da calculadora na interface gráfica.
        Define o layout dos botões com base na lista 'botoes'.
        """

        self.linha = 1
        self.coluna = 0    
        for button in botoes:
            if button == "C" or button == "0":
                self.button = ctk.CTkButton(master=self.window, text= button, font=("Helvetica", 25), width=175, height=76, command=lambda x=button: self.click_button(x))
                self.button.grid(row=self.linha, column=self.coluna, columnspan=2, sticky=W, padx=1, pady=1)
                self.coluna += 2

            else:
                self.button = ctk.CTkButton(master=self.window, text=button, font=("Helvetica", 25), width=87, height=76, command=lambda x=button: self.click_button(x))
                self.button.grid(row=self.linha, column=self.coluna, sticky=W, padx=1, pady=1)
                self.coluna += 1

            if self.coluna > 3:
                self.coluna = 0
                self.linha += 1
    



if __name__ == '__main__':

# Garante que a aplicação seja executada apenas quando o script é iniciado diretamente.
    application()