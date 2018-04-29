import serial
porta = "COM6"
conexao = serial.Serial(porta, 9600)

cores = ["Preto", "Marrom", "Vermelho",
         "Laranja","Amarelo", "Verde", "Azul", "Roxo", "Cinza", "Branco", "Prata", "Ouro"]
while True:
    leituraSerial = conexao.readline()#leitura da serial
    vitas = leituraSerial.split()
    valueFinal = float(vitas[5])
    if(("K" in vitas) == True):
        a = int(valueFinal)*1000
    else:
        a = int(valueFinal)
    string = str(a)
    anel2 = cores[int(string[1])]
    anel1 = cores[int(string[0])]
    anel3 = cores[len(string)-2]

    if(("K" in vitas) == True):
        print("Valor do resistor: " + valueFinal + " K Ohms")
    else:
        print("Valor do resistor: ", valueFinal," Ohms")
    print("As cores do resistor: " + anel1, anel2, anel3)
    del vitas[:]#para não sobrecarregar a variavel 
