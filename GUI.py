from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from vigenere import VigenereCipher
from aff_cipher import AffineCipher


class GUI():

    HEIGHT = 300
    WIDTH = 500
    background_color = "#23262E"
    white = "#fff"
    select_color = "#7A5FEE"
    show_inputs = False
    last_option = 0
    window = None
    frame = None
    cipher = None
    selected = False

    path_message = ""
    plaintext = ""

    choose_file = False

    dynamic_widgets = []

    def __init__(self):
        self.window = Tk()
        self.window.title("Practice 1.Cipher")
        self.window.geometry(str(self.HEIGHT)+'x'+str(self.WIDTH))
        self.window.resizable(0, 0)

        self.frame = Frame(self.window,
                           background=self.background_color
                           )
        self.frame.pack(fill="both",
                        expand=True
                        )

        self.label_opt = Label(self.frame,
                               text="Choose your cipher:",
                               fg=self.white,
                               bg=self.background_color,
                               font=("Arial", 14)
                               )
        self.label_opt.pack()

        option_cipher = IntVar()

        self.radioButton3 = Radiobutton(self.frame,
                                        text="Vegenère",
                                        variable=option_cipher,
                                        value=1,
                                        bg=self.background_color,
                                        selectcolor=self.select_color,
                                        fg=self.white,
                                        font=("Arial", 12)
                                        )
        self.radioButton3.pack()

        self.radioButton4 = Radiobutton(self.frame,
                                        text="Affine",
                                        variable=option_cipher,
                                        value=2,
                                        bg=self.background_color,
                                        selectcolor=self.select_color,
                                        fg=self.white,
                                        font=("Arial", 12)
                                        )
        self.radioButton4.pack()

        self.selectButtonCipher = Button(self.frame,
                                         text="select",
                                         bd=0,
                                         fg=self.white,
                                         bg=self.select_color,
                                         font=("Arial", 12),
                                         command=lambda: self.selectButton_Cipher(
                                             option_cipher.get())
                                         )
        self.selectButtonCipher.pack()

    def run(self):
        self.window.mainloop()

    def selectButton_Cipher(self, option):
        self.destroyDynamicWidgets()
        # print(option)
        if(option != 0 and not self.selected):
            if(option == 1):
                self.cipher = VigenereCipher()
            elif(option == 2):
                self.cipher = AffineCipher()

            print("Option:", option, "Selected:", self.selected)
            self.generateFunctionWidgets()
            self.selected = True
        self.last_option = option

    def selectButton_function(self, option):
        if(option == 1):
            # Encrypt
            self.generateEncryptWidgets(option)

        elif(option == 2):
            self.generateDecryptWidgets(option)
            # Decrypt

        self.last_option = option

    def setInputText(self, input_entry, text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)

    def destroyDynamicWidgets(self):
        for i in self.dynamic_widgets:
            i.destroy()

    def generateFunctionWidgets(self):
        # self.destroyDynamicWidgets()
        label_space = Label(self.frame,
                            text="",
                            bg=self.background_color
                            )
        label_space.pack()
        # self.dynamic_widgets.append(label_space)

        option_action = IntVar()

        radioButtonEncrypt = Radiobutton(self.frame,
                                         text="Encrypt",
                                         variable=option_action,
                                         value=1,
                                         bg=self.background_color,
                                         selectcolor=self.select_color,
                                         fg=self.white,
                                         font=("Arial", 12)
                                         )
        radioButtonEncrypt.pack()
        # self.dynamic_widgets.append(radioButtonEncrypt)

        radioButtonDecrypt = Radiobutton(self.frame,
                                         text="Decrypt",
                                         variable=option_action,
                                         value=2,
                                         bg=self.background_color,
                                         selectcolor=self.select_color,
                                         fg=self.white,
                                         font=("Arial", 12)
                                         )
        radioButtonDecrypt.pack()
        # self.dynamic_widgets.append(radioButtonDecrypt)

        selectButtonFunction = Button(self.frame,
                                      text="select",
                                      bd=0,
                                      fg=self.white,
                                      bg=self.select_color,
                                      font=("Arial", 12),
                                      command=lambda: self.selectButton_function(
                                          option_action.get())
                                      )
        selectButtonFunction.pack()

        # self.dynamic_widgets.append(selectButtonFunction)

    def addSpaceWidget(self):
        label_space = Label(self.frame,
                            text="",
                            bg=self.background_color
                            )
        label_space.pack()
        self.dynamic_widgets.append(label_space)

    def set_alphabet(self, evnt, option):
        print(option)
        if(option == 0):
            self.cipher.setAlfabeto('EN')
        elif(option == 1):
            self.cipher.setAlfabeto('ES')

    def generateKey_functionVig(self, input_widget):

        key = self.cipher.generateKey()
        if(key != None):
            self.setInputText(input_widget, key)
        else:
            messagebox.showinfo(
                message="Alphabet not especified", title="Error"
            )

    def selectPlainText(self):
        self.plaintext = self.cipher.readFile(self.path_message)

    def encryptWidgetsVig(self):
        comboboxAlfabeto = ttk.Combobox(self.frame, state="readonly")
        comboboxAlfabeto['values'] = ['English', 'Spanish']
        comboboxAlfabeto.pack()
        comboboxAlfabeto.bind(
            "<<ComboboxSelected>>", lambda event: self.set_alphabet(event, comboboxAlfabeto.current()))
        self.dynamic_widgets.append(comboboxAlfabeto)

        label_key = Label(self.frame,
                          text="Key",
                          fg=self.white,
                          bg=self.background_color,
                          font=("Arial", 14)
                          )
        label_key.pack()
        self.dynamic_widgets.append(label_key)

        input_key = Entry(self.frame)
        input_key.pack()
        self.dynamic_widgets.append(input_key)

        self.addSpaceWidget()

        generateKeyBtn = Button(self.frame,
                                text="generate",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.generateKey_functionVig(
                                    input_key
                                )
                                )
        generateKeyBtn.pack()
        self.dynamic_widgets.append(generateKeyBtn)

        File = Button(self.frame,
                      text="File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.selectPlainText()
                      )
        File.pack()
        self.dynamic_widgets.append(File)

    def generateEncryptWidgets(self, option):
        self.destroyDynamicWidgets()

        self.addSpaceWidget()
        if(option == 1):
            self.encryptWidgetsVig()
        elif(option == 2):
            pass

    # TODO: Input para llave y seleccion de archivo

    def generateDecryptWidgets(self, option):
        self.destroyDynamicWidgets()
        self.addSpaceWidget()

        chooseKeysBtn = Button(self.frame,
                               text="Key",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial", 12),
                               command=lambda: self.pathKeyDecrypt()
                               )
        chooseKeysBtn.pack()
        self.dynamic_widgets.append(chooseKeysBtn)

        self.addSpaceWidget()

        EncryptedfileBtn = Button(self.frame,
                                  text="Encrypted File",
                                  bd=0,
                                  fg=self.white,
                                  bg=self.select_color,
                                  font=("Arial", 12),
                                  command=lambda: self.pathFileDecrypt()
                                  )
        EncryptedfileBtn.pack()
        self.dynamic_widgets.append(EncryptedfileBtn)

        self.addSpaceWidget()

        encryptButton = Button(self.frame,
                               height=1,
                               text="Decrypt",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial", 12),
                               command=lambda: self.decrypt()
                               )
        encryptButton.pack()
        self.dynamic_widgets.append(encryptButton)

    # ? Metodo sin usar?
    def pathKeyDecrypt(self):
        self.path_key = filedialog.askopenfilename()
        self.choose_key = True
        print("Archivo seleccionado")

    # ? Metodo sin usar?
    def pathFileDecrypt(self):
        self.path_file_to_Decrypt = filedialog.askopenfilename()
        self.choose_fileD = True
        print("Archivo seleccionado")

    # ? Metodo sin usar?
    """ def generateEncryptWigets(self):
        self.destroyDynamicWidgets()
        label_space = Label(self.frame,
                            text="",
                            bg=self.background_color
                            )
        label_space.pack()
        self.dynamic_widgets.append(label_space)

        generateKeysBtn = Button(self.frame,
                                 text="Generate Keys",
                                 bd=0,
                                 fg=self.white,
                                 bg=self.select_color,
                                 font=("Arial", 12),
                                 command=lambda: self.generateKeysFunction()
                                 )
        generateKeysBtn.pack()
        self.dynamic_widgets.append(generateKeysBtn)

        label_space = Label(self.frame,
                            text="",
                            bg=self.background_color
                            )
        label_space.pack()
        self.dynamic_widgets.append(label_space)

        File = Button(self.frame,
                      text="File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.pathFileEncrypt()
                      )
        File.pack()
        self.dynamic_widgets.append(File)
        label_space = Label(self.frame,
                            text="",
                            bg=self.background_color
                            )
        label_space.pack()
        self.dynamic_widgets.append(label_space)
        encryptButton = Button(self.frame,
                               height=1,
                               text="Encrypt",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial", 12),
                               command=lambda: self.encrypt()
                               )
        encryptButton.pack()
        self.dynamic_widgets.append(encryptButton) """

    # ? Metodo sin usar?
    def pathFileEncrypt(self):
        self.path_encrypt = filedialog.askopenfilename()
        self.choose_file = True
        print("Archivo seleccionado")

    # TODO: Cambiar cifrado y decifrado según el cifrador escogido
    def generateKeysFunction(self):
        pass

    def pathFile(self):
        self.path_message = filedialog.askopenfilename()
        self.choose_file = True
        print("Archivo seleccionado")

    # TODO: cifrar
    def encrypt(self):

        pass
    # TODO: decifrar

    def decrypt(self):

        pass


if __name__ == "__main__":
    gui = GUI()
    gui.run()
