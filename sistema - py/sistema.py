def menu(): 
    menu = """
    =============== MENU =============== 
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [NC] Nova conta
    [LC] Listar contas
    [NU] Novo usuário
    [Q] Sair

    =>"""
    return input(menu)

def depositar (saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}"
        print("Depósito realizado com sucesso!")
    else:
       print ("Falha na operação. O valor informado é inválido!")
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print ("Falha na operação. Você não tem saldo suficiênte!")   
    elif excedeu_limite:
         print ("Falha na operação. O valor do saque excede o limite!")
    elif excedeu_saques:
         print ("Falha na operação. Número máximo de saques excedidos!")
    elif valor > 0:
        saldo -= valor 
        extrato += f"saque: R$ {valor:.2f}"
        numero_saques += 1
        print ("Saque realizado com sucesso!")
    else:
        print ("Falha na operação. O valor informado é inválido!")
    return saldo, extrato 

def exibir_extrato (saldo, /, *, extrato):
    print ("===================================")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"Saldo: R$ {saldo:.2f}")

def criar_usuario (usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,"endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print ("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas (contas):
    for conta in contas:
        linha = f"""
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
     opcao = menu()

     if    opcao == "D":
              valor = float(input("Informe o valor do depósito: "))

              saldo, extrato = depositar(saldo, valor, extrato)

     elif  opcao == "S":
             valor = float(input("Informe o valor do saque: "))

             saldo, extrato = sacar(
             saldo = saldo,
             valor = valor,
             extrato = extrato,
             limite = limite,
             numero_saques = numero_saques,
             limite_saques = LIMITE_SAQUES,
             )
     elif  opcao == "E":
             exibir_extrato(saldo, EXTRATO=extrato)
     
     elif opcao == "NU":
             criar_usuario(usuarios)

     elif opcao == "NC":
             numero_conta = len(contas) + 1
             conta = criar_conta (AGENCIA, numero_conta, usuarios)
          
     if conta:
             contas.append(conta)

     elif opcao == "LC":
              listas_contas(contas)      

     elif opcao == "Q":
             break 
        
     else:
          print("Operação inválida, por favor selecione novamente a opção desejada.")


     main()
         
