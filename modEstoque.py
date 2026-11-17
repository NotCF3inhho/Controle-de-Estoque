import json, os, sys,datetime
def limpa():
    os.system("cls")
def limpaQntd(quantidade):
    for i in range(quantidade):
        sys.stdout.write("\33[A\33[2K")
    sys.stdout.flush()
def valueTestInt(mensagem: str) :
    y = 0
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            
            if y == 0:
                limpaQntd(1)
                print("Valor Inválido, tente novamente.")
                y+=1
            elif y != 0:
                limpaQntd(2)
                print("Valor Inválido, tente novamente.")
def valueTestFloat(mensagem: str) :
    y = 0
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            
            if y == 0:
                limpaQntd(1)
                print("Valor Inválido, tente novamente.")
                y+=1
            elif y != 0:
                limpaQntd(2)
                print("Valor Inválido, tente novamente.")
def cadastroProdutos(produtos):
    limpa()
    print(" ==== Cadastro de Produtos ====")
    id = max([p['id'] for p in produtos], default=0) + 1
    nome = input("Nome do Produto : ")
    qntdEstoque = valueTestInt("Quantidade em Estoque : ")
    precoCompra = valueTestFloat("Valor de Compra (Fornecedor): R$")
    precoVenda = valueTestFloat("Valor de Venda (Cliente): R$")
    novoProduto = {
        "id":id,
        "nome":nome,
        "qntdEstoque":qntdEstoque,
        "precoCompra":precoCompra,
        "precoVenda":precoVenda,
        
    }
    return produtos.append(novoProduto)
    
    
def menu():
    limpa()
    print(" ==== Monitoramento Estoque e Vendas ==== ")
    print()
    print("<1> Cadastrar Produto\n<2> Listar Produtos\n<3> Buscar por Produto\n<4> Movimentar Estoque\n<5> Remover Produto\n<6> Relatório do Inventário\n<0> Salvar e Sair")
    print()
    return valueTestInt("Escolha uma opção --> ")

def buscarProduto(produtos):
    limpa()
    print(" ===== Pesquisar por Produto ===== ")
    print("<1> Pesquisa por Id\n<2> Pesquisa por Nome")
    caso = valueTestInt("Escolha uma opção --> ")
    match caso:
        case 1:
            limpa()
            x=0
            print(" ===== Pesquisar por Produto ===== ")
            id = int(input("Digite o Id : "))
            print()
            for i in produtos:
                if i['id']==id:
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Quantidade em Estoque : {i["qntdEstoque"]}")
                    print(f"Preço de Compra : {i["precoCompra"]:.2f}")
                    print(f"Preço de Venda : {i["precoVenda"]:.2f}")
                    x+=1
            if x == 0:
                print("Nenhum produto encontrado.")
        case 2:
            limpa()
            x=0
            print(" ===== Pesquisar por Produto ===== ")
            nome = input("Digite o Nome : ")
            print()
            for i in produtos:
                if nome.strip().lower() in i['nome'].lower():
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Quantidade em Estoque : {i["qntdEstoque"]}")
                    print(f"Preço de Compra : {i["precoCompra"]:.2f}")
                    print(f"Preço de Venda : {i["precoVenda"]:.2f}")
                    x+=2
            if x == 0:
                print("Nenhum produto encontrado.")
        case _:
            limpa()
            print("Opção Incorreta...")
        
    print()
    t= input("press any key...")  
def movimentarEstoque(produtos):
    limpa()
    print(" ===== Movimentar Estoque  ===== ")
    print("Escolha o Produto")
    print("<1> Pesquisa por Id\n<2> Pesquisa por Nome")
    caso = valueTestInt("Escolha uma opção --> ")
    match caso:
        case 1: # > Pesquisa por ID
            limpa()
            x=0
            print(" ===== Movimentação de Estoque ===== ")
            print()
            print(" >>> Pesquisar por Produto")
            id = valueTestInt("Insira o ID do produto : ")
            for i in produtos:
                if i['id']==id:
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Estoque Atual: {i["qntdEstoque"]}")
                    x+=1
            if x == 0:
                return print("Nenhum produto encontrado.")
            tempo = input("press any key...")
            limpa()
            print(" ===== Movimentar Estoque  ===== ")
            caso = valueTestInt("Escolha uma das opções: \n<1> Adicionar Estoque\n<2> Retirar Estoque\n")
            match caso:
                case 1:
                    limpa()
                    print(" ===== Movimentar Estoque  ===== ")
                    print()
                    for i in produtos:
                        if id == i['id']:
                            print(f"Estoque Atual : {i['qntdEstoque']}")           
                            while True:
                                print("ADICIONAR ESTOQUE...")
                                qntdAdicionar = valueTestInt("Quantidade para Adicionar : ")
                                if qntdAdicionar>0:
                                    i['qntdEstoque']+=qntdAdicionar
                                    break
                                else:
                                    print("Valor Inválido.")
                                    continue
                case 2:
                    limpa()
                    print(" ===== Movimentar Estoque  ===== ")
                    print()
                    for i in produtos:
                        if id == i['id']:
                            print(f"Estoque Atual : {i['qntdEstoque']}")           
                            while True:
                                print("RETIRAR ESTOQUE...")
                                qntdAdicionar = valueTestInt("Quantidade para Retirar : ")
                                if qntdAdicionar>0:
                                    i['qntdEstoque']-=qntdAdicionar
                                    if i['qntdEstoque'] < 0:
                                        i['qntdEstoque'] = 0
                                    break
                                else:
                                    print("Valor Inválido.")
                                    continue
                        
                case _:
                    print("Opção Incorreta...")
            
        case 2: ## > Pesquisa por Produto
            limpa()
            x=0
            print(" ===== Movimentação de Estoque ===== ")
            print()
            print(" >>> Pesquisar por Produto")
            nome = input("Digite o Nome : ")
            print()
            for i in produtos:
                if nome.strip().lower() in i['nome'].lower():
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Estoque Atual : {i["qntdEstoque"]}")
                    x+=1
            if x == 0:
                return print("Nenhum produto encontrado.")
            tempo = input("press any key...")
            limpa()
            print(" ===== Movimentar Estoque  ===== ")
            caso = valueTestInt("Escolha uma das opções: \n<1> Adicionar Estoque\n<2> Retirar Estoque\n")
            match caso:
                case 1:
                    limpa()
                    print(" ===== Movimentar Estoque  ===== ")
                    print()
                    for i in produtos:
                        if nome.strip().lower() in i['nome'].lower():
                            print(f"Estoque Atual : {i['qntdEstoque']}")           
                            while True:
                                print("ADICIONAR ESTOQUE...")
                                qntdAdicionar = valueTestInt("Quantidade para Adicionar : ")
                                if qntdAdicionar>0:
                                    i['qntdEstoque']+=qntdAdicionar
                                    break
                                else:
                                    print("Valor Inválido.")
                                    continue
                case 2:
                    limpa()
                    print(" ===== Movimentar Estoque  ===== ")
                    print()
                    for i in produtos:
                        if nome.strip().lower() in i['nome'].lower():
                            print(f"Estoque Atual : {i['qntdEstoque']}")           
                            while True:
                                print("RETIRAR ESTOQUE...")
                                qntdAdicionar = valueTestInt("Quantidade para Retirar : ")
                                if qntdAdicionar>0:
                                    i['qntdEstoque']-=qntdAdicionar
                                    if i['qntdEstoque'] < 0:
                                        i['qntdEstoque'] = 0
                                    break
                                else:
                                    print("Valor Inválido.")
                                    continue
                        
                case _:
                    print("Opção Incorreta...")

    print()
    t= input("press any key...")
def apagarProduto(produtos):
    limpa()
    print(" ===== Remover Produto =====")
    print("< Escolha o produto que deseja deletar >")
    caso = valueTestInt("<1> Buscar por ID\n<2> Buscar por nome\n > ")
    
    match caso:
        case 1:
            encotrado = False
            limpa()
            print(" ===== Remover Produto =====")
            id = valueTestInt("ID do produto : ")
            for i in produtos:
                if i['id'] == id:
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Quantidade em Estoque : {i["qntdEstoque"]}")
                    print(f"Preço de Compra : {i["precoCompra"]:.2f}")
                    print(f"Preço de Venda : {i["precoVenda"]:.2f}")
                    print()
            caso = valueTestInt("Deseja apagar o produto acima?\n<1> Sim\n<2> Não\n > ")
            encotrado = True
            print()
            match caso:
                case 1:
                    limpa()
                    produtos.remove(i)
                    print(f"'{i['nome']} removido com sucesso.'")
                case 2:
                    limpa()
                case _:
                    print("Opção Inválido.")
            if not encotrado:
                limpa()
                print("Nenhum produto encontrado.")
                t= input("press any key...")
        case 2:
            encotrado = False
            limpa()
            print(" ===== Remover Produto =====")
            nome = input("Nome do produto : ")
            for i in produtos:
                if nome.strip().lower() in i['nome'].lower():
                    print(f"Id : {i["id"]}")
                    print(f"Nome : {i["nome"]}")
                    print(f"Quantidade em Estoque : {i["qntdEstoque"]}")
                    print(f"Preço de Compra : {i["precoCompra"]:.2f}")
                    print(f"Preço de Venda : {i["precoVenda"]:.2f}")
                    print()
            caso = valueTestInt("Deseja apagar o produto acima?\n<1> Sim\n<2> Não\n > ")
            encotrado = True
            print()
            match caso:
                case 1:
                    limpa()
                    produtos.remove(i)
                    print(f"'{i['nome']} removido com sucesso.'")
                case 2:
                    limpa()
                case _:
                    print("Opção Inválido.")
            if not encotrado:
                limpa
                print("Nenhum produto encontrado.")
                t= input("press any key...")
def relatorioInventorio(produtos):
    limpa()
    valorInvestido = 0
    valorLucro = 0
    for i in produtos:
        valorInvestido+=i['precoCompra'] * i['qntdEstoque']
        valorLucro+=i['precoVenda'] * i['qntdEstoque']
    lucroTotal = valorLucro - valorInvestido
    relatorio = []
    horaAgora = datetime.datetime.now()
    horaFormatada = horaAgora.strftime("%d/%m/%Y - %H:%M")
    novoRelatorio = {
        "hora" : horaFormatada,
        "valorInvestido" : valorInvestido,
        "valorLucro" : valorLucro,
        "LucroTotal" : lucroTotal
    }
    relatorio.append(novoRelatorio)
    with open("relatorios.txt", "w") as relatorios:
        json.dump(relatorio, relatorios, ensure_ascii=False)
    print(" ===== Relatório de Inventário =====")
    print()
    print(f"Valor de Investimento : R${valorInvestido:.2f}")
    print(f"Valor de Lucro : R${valorLucro:.2f}")
    print(f"Lucro Total : R${lucroTotal:.2f}")
    print()
    print("'relatorios.txt' salvo.")
    t = input("press any key.")
            
