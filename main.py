class Conta:
    def __init__(self, titular, saldo):
        self.Titular = titular
        self.Saldo = saldo
        
    def informacao(self):
        print(f"\nVoce tem o saldo de: {self.Saldo}")
        
    def transferir(self, valor, conta_destino):
        self.Saldo -= valor
        conta_destino.Saldo += valor
        print(f"\033[32mTransferência de R${valor} concluída!\033[0m\n")
        
professor = Conta("Washington", 19822)
aluno = Conta("Gazzoli", 1211)

repeticao = "s"
while repeticao =="s":
    while True:
        print("---Sistema de Transferência Bancária---\n")
        print("Antes de começar, informe quem você é de acordo com a tabela a baixo:")
        print(" p - professor")
        print(" e - estudante")
        opcao = input("Digite a letra que corresponde com voce: ").lower()
        if opcao in ["p", "e"]:
            ""
        else:
            print("\033[31mÉ nescessário que voce insira uma opçao válida.\033[0m")


        if opcao == "p":
            professor.informacao()
            try:
                valor = float(input("Insira o valor que voce deseja transferir para o Estudante: "))
                if valor <= professor.Saldo:
                    professor.transferir(valor, aluno)
                    break
                else:
                    print("\nSaldo \033[1minsuficiente\033[0m, pobre (tente com um valor menor).")
                    break
            except ValueError:
                print("\033[31mDigite apenas números.\033[0m")
    
        elif opcao == "e":
            aluno.informacao()
            try:
                valor = float(input("Insira o valor que voce deseja transferir para Professor: "))
                if valor <= aluno.Saldo:
                    aluno.transferir(valor, professor)
                    break
                else:
                    print("\nSaldo \033[1minsuficiente\033[0m, pobre (tente com um valor menor).")
                    break
            except ValueError:
                print("\033[31mDigite apenas números.\033[0m")
    repeticao = input("\nDeseja realizar outra transferencia ? (s/n)\n").lower()
print(f"Obrigado por usar nosso sistema bancario")