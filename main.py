import obras

myObras = obras.readDataset("obras.csv")
menu = 1
print("------------------------------------------")
print("ANÁLISE DE BASE DE DADOS DE OBRAS MUSICAIS")
print("------------------------------------------")
menu = int(input("""
1 - Listar Base de Dados
2 - Número de Obras da Base de Dados
3 - Lista das Obras Ordenada Alfabeticamente
4 - Lista das Obras Ordenada por Ano
5 - Lista dos Compositores Presentes na Base de Dados
6 - Distribuição das Obras por Período
7 - Distribuição das Obras por Ano
8 - Distribuição das Obras por Compositor
9 - Visualização de Gráficos
0 - Sair
Opção: """))

while menu != 0:
    
    if menu == 1:
        lista = obras.listarObras(myObras)
        print(lista)
    elif menu == 2:
        contagem = obras.contaObras(myObras)
        print("-----------------------------------------------")
        print(" A base de dados contém ",contagem," obras inseridas.")
        print("-----------------------------------------------","\n")
    elif menu == 3:
        listatitano = obras.TitAno(myObras)
        print(listatitano)
    elif menu == 4:
        listaanotit = obras.AnoTit(myObras)
        print(listaanotit)
    elif menu == 5:
        lComp = obras.listarCompositores(myObras)
        print(lComp)
    elif menu == 6:
        obras.tabelarDistribuicao(obras.distObrasPeriodo(myObras))   
    elif menu == 7:
        obras.tabelarDistribuicao(obras.distObrasAno(myObras))        
    elif menu == 8:
        obras.tabelarDistribuicao(obras.distObrasComp(myObras))            
    elif menu == 9:
        obras.desenharGrafico(myObras)                        

    print("------------------------------------------")
    print("ANÁLISE DE BASE DE DADOS DE OBRAS MUSICAIS")
    print("------------------------------------------")    
    menu = int(input("""
1 - Listar Base de Dados
2 - Número de Obras da Base de Dados
3 - Lista das Obras Ordenada Alfabeticamente
4 - Lista das Obras Ordenada por Ano
5 - Lista dos Compositores Presentes na Base de Dados
6 - Distribuição das Obras por Período
7 - Distribuição das Obras por Ano
8 - Distribuição das Obras por Compositor
9 - Visualização de Gráficos
0 - Sair
Opção: """))

print("Aplicação encerrada. Obrigado pela sua utilização.")
    