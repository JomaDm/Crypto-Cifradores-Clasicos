from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from vigenere import VigenereCipher
from aff_cipher import AffineCipher


class GUI():

    HEIGHT = 300
    WIDTH = 550
    background_color = "#23262E"
    white = "#fff"
    select_color = "#7A5FEE"
    show_inputs = False
    last_option = 0
    window = None
    frame = None
    cipher = None
    selected = False
    option_cipher = 0

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
        # print("Option:", option, "Selected:", self.selected)
        if(option == 1):
            self.cipher = VigenereCipher()
        elif(option == 2):
            self.cipher = AffineCipher()
        if(option != 0 and not self.selected):
            self.generateFunctionWidgets()
            self.selected = True
        self.last_option = option
        self.option_cipher = option

    def selectButton_function(self, option):
        self.destroyDynamicWidgets()
        if(option == 1):
            # Encrypt
            self.generateEncryptWidgets()

        elif(option == 2):
            self.generateDecryptWidgets()
            # Decrypt

        self.last_option = option

    def setInputText(self, input_entry, text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)

    def destroyDynamicWidgets(self):
        self.path_message = ""
        self.plaintext = ""
        for i in self.dynamic_widgets:
            i.destroy()

    def generateFunctionWidgets(self):
        self.destroyDynamicWidgets()
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
        # print(option)
        if(option == 0):
            self.cipher.setAlfabeto('EN')
        elif(option == 1):
            self.cipher.setAlfabeto('ES')

    def generateKey_functionVig(self, input_widget):
        # print("V")
        key = self.cipher.generateKey()
        print(key)
        if(key != None):
            self.setInputText(input_widget, key)
        else:
            messagebox.showinfo(
                message="Alphabet not especified", title="Error"
            )

    def generateKey_functionAff(self, input_corr, input_mult):
        # print("A")
        keys = self.cipher.generateKey()
        print(keys)

        if(keys != None):
            print(keys)
            self.setInputText(input_mult, str(keys[0]))
            self.setInputText(input_corr, str(keys[1]))
        else:
            messagebox.showinfo(
                message="Alphabet not especified", title="Error"
            )

    def selectText(self):
        self.pathFile()
        self.plaintext = self.cipher.readFile(self.path_message)

    def encryptWidgetsAff(self):
        self.destroyDynamicWidgets()
        self.addSpaceWidget()
        comboboxAlfabeto = ttk.Combobox(self.frame, state="readonly")
        comboboxAlfabeto['values'] = ['English', 'Spanish']
        comboboxAlfabeto.current(0)
        self.set_alphabet(None, 0)
        comboboxAlfabeto.pack()
        comboboxAlfabeto.bind(
            "<<ComboboxSelected>>", lambda event: self.set_alphabet(event, comboboxAlfabeto.current()))
        self.dynamic_widgets.append(comboboxAlfabeto)

        label_key_a = Label(self.frame,
                            text="Key shifter",
                            fg=self.white,
                            bg=self.background_color,
                            font=("Arial", 14)
                            )
        label_key_a.pack()
        self.dynamic_widgets.append(label_key_a)

        input_key_corr = Entry(self.frame)
        input_key_corr.pack()
        self.dynamic_widgets.append(input_key_corr)

        self.addSpaceWidget()

        label_key_b = Label(self.frame,
                            text="Key multiplicative",
                            fg=self.white,
                            bg=self.background_color,
                            font=("Arial", 14)
                            )
        label_key_b.pack()
        self.dynamic_widgets.append(label_key_b)

        input_key_mult = Entry(self.frame)
        input_key_mult.pack()
        self.dynamic_widgets.append(input_key_mult)

        self.addSpaceWidget()

        generateKeyBtn = Button(self.frame,
                                text="generate",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.generateKey_functionAff(
                                    input_key_corr, input_key_mult
                                )
                                )
        generateKeyBtn.pack()
        self.dynamic_widgets.append(generateKeyBtn)

        self.addSpaceWidget()

        File = Button(self.frame,
                      text="Message File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.selectText()
                      )
        File.pack()
        self.dynamic_widgets.append(File)

        self.addSpaceWidget()

        EncryptBtn = Button(self.frame,
                            text="Encrypt",
                            bd=0,
                            fg=self.white,
                            bg=self.select_color,
                            font=("Arial", 12),
                            command=lambda: self.encrypt(
                                [int(input_key_mult.get()), int(input_key_corr.get())])
                            )
        EncryptBtn.pack()
        self.dynamic_widgets.append(EncryptBtn)

        self.addSpaceWidget()

    def encryptWidgetsVig(self):
        self.destroyDynamicWidgets()
        self.addSpaceWidget()
        comboboxAlfabeto = ttk.Combobox(self.frame, state="readonly")
        comboboxAlfabeto['values'] = ['English', 'Spanish']
        comboboxAlfabeto.current(0)
        self.set_alphabet(None, 0)
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

        self.addSpaceWidget()

        File = Button(self.frame,
                      text="Message File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.selectText()
                      )
        File.pack()
        self.dynamic_widgets.append(File)

        self.addSpaceWidget()

        EncryptBtn = Button(self.frame,
                            text="Encrypt",
                            bd=0,
                            fg=self.white,
                            bg=self.select_color,
                            font=("Arial", 12),
                            command=lambda: self.encrypt(input_key.get())
                            )
        EncryptBtn.pack()
        self.dynamic_widgets.append(EncryptBtn)

        self.addSpaceWidget()

    def generateEncryptWidgets(self):
        self.destroyDynamicWidgets()
        print(self.option_cipher)
        self.addSpaceWidget()
        if(self.option_cipher == 1):
            self.encryptWidgetsVig()
        elif(self.option_cipher == 2):
            self.encryptWidgetsAff()

    def decryptWidgetsVig(self):
        self.destroyDynamicWidgets()
        self.addSpaceWidget()
        comboboxAlfabeto = ttk.Combobox(self.frame, state="readonly")
        comboboxAlfabeto['values'] = ['English', 'Spanish']
        comboboxAlfabeto.current(0)
        self.set_alphabet(None, 0)
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

        File = Button(self.frame,
                      text="Encrypted File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.selectText()
                      )
        File.pack()
        self.dynamic_widgets.append(File)

        self.addSpaceWidget()

        EncryptBtn = Button(self.frame,
                            text="Decrypt",
                            bd=0,
                            fg=self.white,
                            bg=self.select_color,
                            font=("Arial", 12),
                            command=lambda: self.decrypt(
                                input_key.get(), self.path_message)
                            )
        EncryptBtn.pack()
        self.dynamic_widgets.append(EncryptBtn)

        self.addSpaceWidget()

    def decryptWidgetsAff(self):
        self.destroyDynamicWidgets()
        self.addSpaceWidget()
        comboboxAlfabeto = ttk.Combobox(self.frame, state="readonly")
        comboboxAlfabeto['values'] = ['English', 'Spanish']
        comboboxAlfabeto.current(0)
        self.set_alphabet(None, 0)
        comboboxAlfabeto.pack()
        comboboxAlfabeto.bind(
            "<<ComboboxSelected>>", lambda event: self.set_alphabet(event, comboboxAlfabeto.current()))
        self.dynamic_widgets.append(comboboxAlfabeto)

        label_key_a = Label(self.frame,
                            text="Key shifter",
                            fg=self.white,
                            bg=self.background_color,
                            font=("Arial", 14)
                            )
        label_key_a.pack()
        self.dynamic_widgets.append(label_key_a)

        input_key_corr = Entry(self.frame)
        input_key_corr.pack()
        self.dynamic_widgets.append(input_key_corr)

        self.addSpaceWidget()

        label_key_b = Label(self.frame,
                            text="Key multiplicative",
                            fg=self.white,
                            bg=self.background_color,
                            font=("Arial", 14)
                            )
        label_key_b.pack()
        self.dynamic_widgets.append(label_key_b)

        input_key_mult = Entry(self.frame)
        input_key_mult.pack()
        self.dynamic_widgets.append(input_key_mult)

        self.addSpaceWidget()

        File = Button(self.frame,
                      text="Encrypted File",
                      bd=0,
                      fg=self.white,
                      bg=self.select_color,
                      font=("Arial", 12),
                      command=lambda: self.selectText()
                      )
        File.pack()
        self.dynamic_widgets.append(File)

        self.addSpaceWidget()

        EncryptBtn = Button(self.frame,
                            text="Decrypt",
                            bd=0,
                            fg=self.white,
                            bg=self.select_color,
                            font=("Arial", 12),
                            command=lambda: self.decrypt(
                                [int(input_key_mult.get()), int(input_key_corr.get())], self.path_message)
                            )
        EncryptBtn.pack()
        self.dynamic_widgets.append(EncryptBtn)

        self.addSpaceWidget()

    def generateDecryptWidgets(self):
        self.destroyDynamicWidgets()
        print(self.option_cipher)
        self.addSpaceWidget()
        if(self.option_cipher == 1):
            self.decryptWidgetsVig()
        elif(self.option_cipher == 2):
            self.decryptWidgetsAff()

    def pathFile(self):
        self.path_message = filedialog.askopenfilename()
        self.choose_file = True
        print("Archivo seleccionado")

    def encrypt(self, keys):
        encrypted = self.cipher.encrypt(keys, self.plaintext)
        if(encrypted != None):
            file_name = "message_encrypted"
            if self.option_cipher == 1:
                file_name += ".vig"
            elif self.option_cipher == 2:
                file_name += ".aff"
            self.cipher.writeFile(encrypted, file=file_name)
        else:
            messagebox.showinfo(
                message="Error with the key", title="Error"
            )

    # TODO: decifrar

    def decrypt(self, key, path):
        decrypted = self.cipher.decrypt(key, self.cipher.readFile(path))
        file_name = "message_decrypted"
        if self.option_cipher == 1:
            file_name += ".vig"
        elif self.option_cipher == 2:
            file_name += ".aff"
        self.cipher.writeFile(decrypted, file=file_name)


if __name__ == "__main__":
    gui = GUI()
    gui.run()
