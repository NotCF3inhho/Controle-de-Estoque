import json, os, sys, datetime

import modEstoque as md
try:
    with open("monitoramento.json", "r") as read:
        produtos = json.load(read)
    print("'monitoramento.json' carregado.")
except FileNotFoundError:
    print("'monitoramento.json' não encontrado.")
    produtos = []
caso=1
while caso!=0:
    md.limpa()
    caso = md.menu()
    match caso:
        case 1:
            md.cadastroProdutos(produtos)
        case 2: 
            if len(produtos)==0:
                md.limpa()
                print("Nenhum Produto Cadastrado.")
                t = input("Press any key...")
            else:
                md.limpa()
                print(f"{"ID":<10}{"NOME DO PRODUTO":<22}{"VALOR DE COMPRA":<22}{"VALOR DE VENDA":<22}{"ESTOQUE":<22}")
                for i in produtos:
                    print(f"{i["id"]:<10}{i["nome"]:<22}{i["precoCompra"]:<22.2f}{i["precoVenda"]:<22.2f}{i["qntdEstoque"]:<22}")
                print()
                tempo = input("press any key...")
        case 3:
            md.limpa()
            x = md.buscarProduto(produtos)
        case 4:
            md.limpa()
            print()
            md.movimentarEstoque(produtos)
        case 5:
            md.limpa()
            md.apagarProduto(produtos)
        case 6:
            md.relatorioInventorio(produtos)

        case 0:
            with open("monitoramento.json","w") as pp:
                json.dump(produtos, pp, ensure_ascii=False, indent=4)
            print("'monitoramento.json' salvo")
            print("saiu.")
            

        case _:
            print("Opção inválida, tente novamente")
            print()
            continue

       