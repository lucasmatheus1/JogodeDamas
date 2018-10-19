matriz = []
ordem_matriz = 8
pontuaçao_jog1 = 0
pontuaçao_jog2 = 0
cont_cap_dama = 0
lista_capturar_dama = []
captura_consecutiva=[]
jogada_não_permitida=[]
jogada_impossivel=[]
def Tabuleiro(matriz):
    for i in range(ordem_matriz):
        if i <= (ordem_matriz // 3):
            if i % 2 != 0:
                matriz.append(['x', '-', 'x', '-', 'x', '-', 'x', '-'])
            else:
                matriz.append(['-', 'x', '-', 'x', '-', 'x', '-', 'x'])
        elif i == (ordem_matriz // 2) or i == ((ordem_matriz // 2) - 1):
            matriz.append(['-', '-', '-', '-', '-', '-', '-', '-'])
        else:
            if i % 2 != 0:
                matriz.append(['o', '-', 'o', '-', 'o', '-', 'o', '-'])
            else:
                matriz.append(['-', 'o', '-', 'o', '-', 'o', '-', 'o'])
    return matriz
def Imprimir_tabuleiro():
    print (" ",0,1,2,3,4,5,6,7)
    for i in range(ordem_matriz):  # Imprime o Tabuleiro.
        print (i , end=" ")
        for j in range(ordem_matriz):
            print(tabuleiro[i][j], end=' ')
        print()

    return
tabuleiro = Tabuleiro(matriz)
def Entrada_tratada_linha(numero_linha):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7']
    while True:
        if numero_linha in numeros:
            numero_linha = (numero_linha)
            break
        else:
            print('Linha inválida')
            numero_linha = input('Informe a linha de escolha: ')
    return numero_linha
def Entrada_tratada_coluna(numero_coluna):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7']
    while True:
        if numero_coluna in numeros:
            numero_coluna = (numero_coluna)
            break
        else:
            print('Coluna inválida')
            numero_coluna = input('Informe a coluna de escolha: ')
    return numero_coluna
def Entrada_de_formações(linha_atual,coluna_atual,linha_desejada,coluna_desejada):
    entrada=[]
    while tabuleiro[linha_atual][coluna_atual] != peça_da_vez and tabuleiro[linha_atual][
        coluna_atual] != peça_dama:  # Se peça for diferente da peça da vez, emite mensagem de erro
        Imprimir_tabuleiro()
        print('Escolha ' + str(peça_da_vez) + ' por favor! ')
        linha_atual = input('Informe a linha de escolha: ')
        linha_atual = Entrada_tratada_linha(linha_atual)
        while linha_atual.isdigit() == False:
            print('Apenas números! Por favor.')
            linha_atual = input('Informe a linha de escolha: ')
            linha_atual = Entrada_tratada_linha(linha_atual)

        coluna_atual = input('Informe a coluna de escolha: ')
        coluna_atual = Entrada_tratada_coluna(coluna_atual)
        while coluna_atual.isdigit() == False:
            print('Apenas números! Por favor.')
            coluna_atual = input('Informe a coluna de escolha: ')
            coluna_atual = Entrada_tratada_coluna(coluna_atual)

        linha_desejada = input('Informe a linha desejada: ')
        linha_desejada = Linha_desejada(linha_desejada)
        while linha_desejada.isdigit() == False:
            print('Apenas números! Por favor.')
            linha_desejada = input('Informe a linha desejada: ')
            linha_desejada = Linha_desejada(linha_desejada)

        coluna_desejada = input('Informe a coluna desejada: ')
        coluna_desejada = Coluna_desejada(coluna_desejada)
        while coluna_desejada.isdigit() == False:
            print('Apenas números! Por favor.')
            coluna_desejada = input('Informe a coluna desejada: ')
            coluna_desejada = Coluna_desejada(coluna_desejada)

        linha_atual, linha_desejada = int(linha_atual), int(linha_desejada)
        coluna_atual, coluna_desejada = int(coluna_atual), int(coluna_desejada)
    entrada.append(linha_atual)
    entrada.append(coluna_atual)
    entrada.append(linha_desejada)
    entrada.append(coluna_desejada)
    return entrada
def Linha_desejada(linha):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7']
    while True:
        if linha in numeros:
            linha = (linha)
            break
        else:
            print('Linha inválida')
            linha = input('Informe a linha desejada: ')
    return linha
def Coluna_desejada(coluna):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7']
    while True:
        if coluna in numeros:
            coluna = (coluna)
            break
        else:
            print('Coluna inválida')
            coluna = input('Informe a coluna desejada: ')
    return coluna
def Captura_obrigatoria(vez):
    linha_obrigatoria_jogador = []
    coluna_obrigatoria_jogador = []
    lin_col_obr = []
    if vez % 2 == 0:  # Se for par, quem mexe é o primeiro jogador.
        peça_da_vez = 'x'
        peça_espera = 'o'
    else:
        peça_da_vez = 'o'
        peça_espera = 'x'

    for i in range(len((tabuleiro))):

        if i == 1 or i == 0:
            for j in range(len((tabuleiro)[i])):
                if j == 0 or j == 1:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i + 1][j + 1] == peça_espera or (tabuleiro)[i + 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

                elif j == 6 or j == 7:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i + 1][j - 1] == peça_espera or (tabuleiro)[i + 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

                elif j == 2 or j == 3 or j == 4 or j == 5:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i + 1][j + 1] == peça_espera or (tabuleiro)[i + 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i + 1][j - 1] == peça_espera or (tabuleiro)[i + 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

        elif i == 7 or i == 6:
            for j in range(len((tabuleiro)[i])):

                if j == 0 or j == 1:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j + 1] == peça_espera or (tabuleiro)[i - 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

                elif j == 6 or j == 7:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j - 1] == peça_espera or (tabuleiro)[i - 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)


                elif j == 2 or j == 3 or j == 4 or j == 5:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j + 1] == peça_espera or (tabuleiro)[i - 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i - 1][j - 1] == peça_espera or (tabuleiro)[i - 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

        elif i == 2 or i == 3 or i == 4 or i == 5:
            for j in range(len((tabuleiro)[i])):

                if j == 7 or j == 6:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j - 1] == peça_espera or (tabuleiro)[i - 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i + 1][j - 1] == peça_espera or (tabuleiro)[i + 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                if j == 0 or j == 1:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j + 1] == peça_espera or (tabuleiro)[i - 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i + 1][j + 1] == peça_espera or (tabuleiro)[i + 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)


                elif j == 2 or j == 3 or j == 4 or j == 5:
                    if (tabuleiro)[i][j] == peça_da_vez:
                        if (tabuleiro)[i - 1][j - 1] == peça_espera or (tabuleiro)[i - 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i + 1][j - 1] == peça_espera or (tabuleiro)[i + 1][j - 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j - 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i - 1][j + 1] == peça_espera or (tabuleiro)[i - 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i - 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)
                        if (tabuleiro)[i + 1][j + 1] == peça_espera or (tabuleiro)[i + 1][j + 1] == peça_espera_dama:
                            if (tabuleiro)[i + 2][j + 2] == '-':
                                linha_obrigatoria_jogador.append(i)
                                coluna_obrigatoria_jogador.append(j)

    lin_col_obr.append(linha_obrigatoria_jogador)
    lin_col_obr.append(coluna_obrigatoria_jogador)

    return lin_col_obr
def Capturar(linha_atual, coluna_atual, linha_desejada, coluna_desejada):
    lista_capturar = []
    if linha_desejada != (linha_atual + 2) or linha_desejada != (
        linha_atual - 2):
        if coluna_desejada != (coluna_atual + 2) or coluna_desejada != (coluna_atual - 2):
            if linha_atual == (ordem_matriz - (ordem_matriz - 1)) or linha_atual == (ordem_matriz - ordem_matriz):
                if coluna_atual == (ordem_matriz - (ordem_matriz - 1)) or coluna_atual == (ordem_matriz - ordem_matriz):
                    if (tabuleiro[linha_atual + 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1]==peça_espera_dama) and (
                                        linha_atual + 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual + 1] = '-'
                elif coluna_atual == (ordem_matriz - 1) or coluna_atual == (ordem_matriz - 2):
                    if (tabuleiro[linha_atual + 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1]==peça_espera_dama) and (
                                        linha_atual + 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual - 1] = '-'
                else:
                    if (tabuleiro[linha_atual + 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1]==peça_espera_dama) and (
                                linha_atual + 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual + 1] = '-'
                    elif (tabuleiro[linha_atual + 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1]==peça_espera_dama) and (
                                linha_atual + 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual - 1] = '-'
            elif linha_atual == (ordem_matriz - 1) or linha_atual == (ordem_matriz - 2):
                if coluna_atual == (ordem_matriz - (ordem_matriz - 1)) or coluna_atual == (ordem_matriz - ordem_matriz):
                    if (tabuleiro[linha_atual - 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1]==peça_espera_dama) and (
                                        linha_atual - 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual + 1] = '-'
                elif coluna_atual == (ordem_matriz - 1) or coluna_atual == (ordem_matriz - 2):
                    if (tabuleiro[linha_atual - 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1]==peça_espera_dama) and (
                                        linha_atual - 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual - 1] = '-'
                else:
                    if (tabuleiro[linha_atual - 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1]==peça_espera_dama) and (
                                linha_atual - 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual + 1] = '-'
                    elif (tabuleiro[linha_atual - 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1]==peça_espera_dama) and (
                                linha_atual - 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual - 1] = '-'
            else:
                if coluna_atual == (ordem_matriz - (ordem_matriz - 1)) or coluna_atual == (ordem_matriz - ordem_matriz):
                    if (tabuleiro[linha_atual - 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1]==peça_espera_dama) and (
                                        linha_atual - 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual + 1] = '-'
                    elif (tabuleiro[linha_atual + 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1]==peça_espera_dama) and (
                                        linha_atual + 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual + 1] = '-'
                elif coluna_atual == (ordem_matriz - 1) or coluna_atual == (ordem_matriz - 2):
                    if (tabuleiro[linha_atual - 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1]==peça_espera_dama) and (
                                        linha_atual - 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual - 1] = '-'
                    elif (tabuleiro[linha_atual + 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1]==peça_espera_dama) and (
                                        linha_atual + 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual - 1] = '-'
                else:
                    if (tabuleiro[linha_atual + 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1]==peça_espera_dama) and (
                                linha_atual + 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual + 1] = '-'
                    elif (tabuleiro[linha_atual - 1][coluna_atual + 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1]==peça_espera_dama) and (
                                linha_atual - 2 == linha_desejada and coluna_atual + 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual+2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual + 1] = '-'

                    elif (tabuleiro[linha_atual - 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1]==peça_espera_dama) and (
                                linha_atual - 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual-2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual - 1][coluna_atual - 1] = '-'
                    elif (tabuleiro[linha_atual + 1][coluna_atual - 1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1]==peça_espera_dama) and (
                                linha_atual + 2 == linha_desejada and coluna_atual - 2 == coluna_desejada) and tabuleiro[linha_atual+2][coluna_atual-2] == '-':
                        lista_capturar.append('capturar')
                        tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                        tabuleiro[linha_atual][coluna_atual] = '-'
                        tabuleiro[linha_atual + 1][coluna_atual - 1] = '-'

    return lista_capturar
def Mover(linha_atual, coluna_atual, linha_desejada, coluna_desejada, vez, cap_obrg,pontuação_jog1,pontuaçao_jog2):
    if pontuaçao_jog2 ==1 or pontuaçao_jog1==1:
        if coluna_atual == (ordem_matriz-1):
            if vez%2 == 0:
                if (tabuleiro[linha_atual+1][coluna_atual-1] == peça_da_vez or tabuleiro[linha_atual+1][coluna_atual-1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1] == peça_espera_dama or tabuleiro[linha_atual+1][coluna_atual-1] == peça_dama)  and (tabuleiro[linha_atual+2][coluna_atual-2] == peça_da_vez or tabuleiro[linha_atual+2][coluna_atual-2] == peça_espera or tabuleiro[linha_atual+2][coluna_atual-2] == peça_espera_dama or tabuleiro[linha_atual+2][coluna_atual-2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
            else:
                if (tabuleiro[linha_atual-1][coluna_atual-1] == peça_da_vez or tabuleiro[linha_atual-1][coluna_atual-1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1] == peça_espera_dama or tabuleiro[linha_atual-1][coluna_atual-1] == peça_dama)  and (tabuleiro[linha_atual-2][coluna_atual-2] == peça_da_vez or tabuleiro[linha_atual-2][coluna_atual-2] == peça_espera or tabuleiro[linha_atual-2][coluna_atual-2] == peça_espera_dama or tabuleiro[linha_atual-2][coluna_atual-2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
        elif coluna_atual == (ordem_matriz-ordem_matriz):
            if vez%2 == 0:
                if (tabuleiro[linha_atual+1][coluna_atual+1] == peça_da_vez or tabuleiro[linha_atual+1][coluna_atual+1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1] == peça_espera_dama or tabuleiro[linha_atual+1][coluna_atual+1] == peça_dama)  and (tabuleiro[linha_atual+2][coluna_atual+2] == peça_da_vez or tabuleiro[linha_atual+2][coluna_atual+2] == peça_espera or tabuleiro[linha_atual+2][coluna_atual+2] == peça_espera_dama or tabuleiro[linha_atual+2][coluna_atual+2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
            else:
                if (tabuleiro[linha_atual-1][coluna_atual+1] == peça_da_vez or tabuleiro[linha_atual-1][coluna_atual+1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1] == peça_espera_dama or tabuleiro[linha_atual-1][coluna_atual+1] == peça_dama)  and (tabuleiro[linha_atual-2][coluna_atual+2] == peça_da_vez or tabuleiro[linha_atual-2][coluna_atual+2] == peça_espera or tabuleiro[linha_atual-2][coluna_atual+2] == peça_espera_dama or tabuleiro[linha_atual-2][coluna_atual+2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
        else:
            if vez%2 == 0:
                if (tabuleiro[linha_atual+1][coluna_atual+1] == peça_da_vez or tabuleiro[linha_atual+1][coluna_atual+1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual+1] == peça_espera_dama or tabuleiro[linha_atual+1][coluna_atual+1] == peça_dama)  and (tabuleiro[linha_atual+2][coluna_atual+2] == peça_da_vez or tabuleiro[linha_atual+2][coluna_atual+2] == peça_espera or tabuleiro[linha_atual+2][coluna_atual+2] == peça_espera_dama or tabuleiro[linha_atual+2][coluna_atual+2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
                elif (tabuleiro[linha_atual+1][coluna_atual-1] == peça_da_vez or tabuleiro[linha_atual+1][coluna_atual-1] == peça_espera or tabuleiro[linha_atual+1][coluna_atual-1] == peça_espera_dama or tabuleiro[linha_atual+1][coluna_atual-1] == peça_dama)  and (tabuleiro[linha_atual+2][coluna_atual-2] == peça_da_vez or tabuleiro[linha_atual+2][coluna_atual-2] == peça_espera or tabuleiro[linha_atual+2][coluna_atual-2] == peça_espera_dama or tabuleiro[linha_atual+2][coluna_atual-2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
            else:
                if (tabuleiro[linha_atual-1][coluna_atual+1] == peça_da_vez or tabuleiro[linha_atual-1][coluna_atual+1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual+1] == peça_espera_dama or tabuleiro[linha_atual-1][coluna_atual+1] == peça_dama)  and (tabuleiro[linha_atual-2][coluna_atual+2] == peça_da_vez or tabuleiro[linha_atual-2][coluna_atual+2] == peça_espera or tabuleiro[linha_atual-2][coluna_atual+2] == peça_espera_dama or tabuleiro[linha_atual-2][coluna_atual+2] == peça_dama):
                    jogada_impossivel.append('Impossivel')
                elif (tabuleiro[linha_atual-1][coluna_atual-1] == peça_da_vez or tabuleiro[linha_atual-1][coluna_atual-1] == peça_espera or tabuleiro[linha_atual-1][coluna_atual-1] == peça_espera_dama or tabuleiro[linha_atual-1][coluna_atual-1] == peça_dama)  and (tabuleiro[linha_atual-2][coluna_atual-2] == peça_da_vez or tabuleiro[linha_atual-2][coluna_atual-2] == peça_espera or tabuleiro[linha_atual-2][coluna_atual-2] == peça_espera_dama or tabuleiro[linha_atual-2][coluna_atual-2] == peça_dama):
                    jogada_impossivel.append('Impossivel')

    lista_vez = []
    if tabuleiro[linha_desejada][coluna_desejada] == '-' and lista_capturar == []:
        if len(cap_obrg[0]) == 0:
            if linha_desejada == (linha_atual + 1) or linha_desejada == (linha_atual - 1):
                if coluna_desejada == (coluna_atual + 1) or coluna_desejada == (coluna_atual - 1):
                    if vez % 2 == 0:
                        if linha_atual < linha_desejada and cap_obrg_dama == [[],[]]:
                            tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                            tabuleiro[linha_atual][coluna_atual] = '-'
                        else:
                            print('Jogada não permitida')
                            lista_vez.append('nao move')
                    else:
                        if linha_atual > linha_desejada and cap_obrg_dama == [[],[]]:
                            tabuleiro[linha_desejada][coluna_desejada] = peça_da_vez
                            tabuleiro[linha_atual][coluna_atual] = '-'
                        else:
                            print('Jogada não permitida')
                            lista_vez.append('nao move')
                else:
                    print('Jogada não permitida')
                    lista_vez.append('nao move')
            else:
                print('Jogada não permitida')
                lista_vez.append('nao move')

        else:
            print('Jogada não permitida')
            lista_vez.append('nao move')

    elif tabuleiro[linha_desejada][coluna_desejada] != '-' and lista_capturar == []:
        print('Jogada não permitida')
        lista_vez.append('nao move')
        if abs(linha_desejada - linha_atual) > 1:
            lista_vez.append('nao move')

    return lista_vez
def Verificar_dama():
    for i in range(len((tabuleiro))):
        if i == 0:
            for j in range(8):
                if tabuleiro[i][j] == 'o':
                    tabuleiro[i][j] = 'O'
        elif i == 7:
            for j in range(8):
                if tabuleiro[i][j] == 'x':
                    tabuleiro[i][j] = 'X'
    return tabuleiro
def Dama_principal_descendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada):
    porta = []
    for i in range(linha_atual + 1, linha_desejada):
        for j in range(coluna_atual + 1, coluna_desejada):
            porta.append(tabuleiro[i][j])

    matriz_dama = []
    para_divisao = abs((linha_atual + 1) - linha_desejada)
    for i in range(para_divisao):
        matriz_dama.append([])

    cont = 0
    cont_de_ordem = -1

    for i in porta:
        cont_de_ordem += 1
        if cont_de_ordem == para_divisao:
            cont += 1
            cont_de_ordem = 0
        matriz_dama[cont].append(i)

    matriz_diagonais = []

    for i in range(para_divisao):
        for j in range(para_divisao):
            if i == j:
                matriz_diagonais.append(matriz_dama[i][j])

    return matriz_diagonais
def Dama_secundaria_descendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada):
    porta = []
    lista_lins_cols = []
    lista_lins_cols.append(linha_atual)
    lista_lins_cols.append(coluna_desejada)
    lista_lins_cols.append(linha_desejada)
    lista_lins_cols.append(coluna_atual)

    for i in range(lista_lins_cols[0] + 1, lista_lins_cols[2]):
        for j in range(lista_lins_cols[1] + 1, lista_lins_cols[3]):
            porta.append(tabuleiro[i][j])

    matriz_dama = []
    para_divisao = abs((lista_lins_cols[0] + 1) - lista_lins_cols[2])
    for i in range(para_divisao):
        matriz_dama.append([])

    cont = 0
    cont_de_ordem = -1
    # isso é para adicionar itens nas listas, igual a entrada da questao matriz de permutação
    for i in porta:
        cont_de_ordem += 1
        if cont_de_ordem == para_divisao:
            cont += 1
            cont_de_ordem = 0
        matriz_dama[cont].append(i)

    matriz_diagonais = []

    for i in range(para_divisao):
        for j in range(para_divisao):
            if (i + j == (para_divisao - 1)):
                matriz_diagonais.append(matriz_dama[i][j])

    return matriz_diagonais
def Dama_secundaria_ascendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada):
    porta = []
    lista_lins_cols = []
    lista_lins_cols.append(linha_desejada)
    lista_lins_cols.append(coluna_atual)
    lista_lins_cols.append(linha_atual)
    lista_lins_cols.append(coluna_desejada)

    for i in range(lista_lins_cols[0] + 1, lista_lins_cols[2]):
        for j in range(lista_lins_cols[1] + 1, lista_lins_cols[3]):
            porta.append(tabuleiro[i][j])

    matriz_dama = []
    para_divisao = abs((lista_lins_cols[0] + 1) - lista_lins_cols[2])
    for i in range(para_divisao):
        matriz_dama.append([])

    cont = 0
    cont_de_ordem = -1
    # isso é para adicionar itens nas listas, igual a entrada da questao matriz de permutação
    for i in porta:
        cont_de_ordem += 1
        if cont_de_ordem == para_divisao:
            cont += 1
            cont_de_ordem = 0
        matriz_dama[cont].append(i)

    matriz_diagonais = []

    for i in range(para_divisao):
        for j in range(para_divisao):
            if (i + j == (para_divisao - 1)):
                matriz_diagonais.append(matriz_dama[i][j])

    matriz_diagonais = matriz_diagonais[::-1]

    return matriz_diagonais
def Dama_principal_ascendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada):
    porta = []
    lista_lins_cols = []
    lista_lins_cols.append(linha_desejada)
    lista_lins_cols.append(coluna_desejada)
    lista_lins_cols.append(linha_atual)
    lista_lins_cols.append(coluna_atual)

    for i in range(lista_lins_cols[0] + 1, lista_lins_cols[2]):
        for j in range(lista_lins_cols[1] + 1, lista_lins_cols[3]):
            porta.append(tabuleiro[i][j])

    matriz_dama = []
    para_divisao = abs((lista_lins_cols[0] + 1) - lista_lins_cols[2])
    for i in range(para_divisao):
        matriz_dama.append([])

    cont = 0
    cont_de_ordem = -1
    # isso é para adicionar itens nas listas, igual a entrada da questao matriz de permutação
    for i in porta:
        cont_de_ordem += 1
        if cont_de_ordem == para_divisao:
            cont += 1
            cont_de_ordem = 0
        matriz_dama[cont].append(i)

    matriz_diagonais = []

    for i in range(para_divisao):
        for j in range(para_divisao):
            if i == j:
                matriz_diagonais.append(matriz_dama[i][j])

    matriz_diagonais = matriz_diagonais[::-1]

    return matriz_diagonais
def Dama_percorre(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama):
    lista_obri_dama = [[],[]]
    principal_subindo = Principal_subindo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama)
    if principal_subindo!=[[],[]]:
        lista_obri_dama[0].append(principal_subindo[0][0])
        lista_obri_dama[1].append(principal_subindo[1][0])
    principal_descendo = Principal_descendo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama)
    if principal_descendo!=[[],[]]:
        lista_obri_dama[0].append(principal_descendo[0][0])
        lista_obri_dama[1].append(principal_descendo[1][0])
    secundaria_subindo = Secundaria_subindo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama)
    if secundaria_subindo!=[[],[]]:
        lista_obri_dama[0].append(secundaria_subindo[0][0])
        lista_obri_dama[1].append(secundaria_subindo[1][0])
    secundaria_descendo = Secundaria_descendo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama)
    if secundaria_descendo!=[[],[]]:
        lista_obri_dama[0].append(secundaria_descendo[0][0])
        lista_obri_dama[1].append(secundaria_descendo[1][0])

    return lista_obri_dama
def Principal_subindo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama):
    sair = 0
    dama_capturar = [[], []]
    while (linha_atual >= 0 and linha_atual <= 7) or (coluna_atual >= 0 and coluna_atual <= 7):
        tabuleiro[linha_atual][coluna_atual]
        linha_atual -= 1
        coluna_atual -= 1
        if linha_atual < 0 or coluna_atual < 0:
            break
        else:

            if tabuleiro[linha_atual][coluna_atual] == peça_espera or tabuleiro[linha_atual][coluna_atual] == peça_espera_dama:
                if sair == 0:
                    sair += 1
                    linha_atual -= 1
                    coluna_atual -= 1
                    if linha_atual < 0 or coluna_atual < 0:
                        break
                    else:
                        if tabuleiro[linha_atual][coluna_atual] == '-':
                            dama_capturar[0].append(linha_atual)
                            dama_capturar[1].append(coluna_atual)

                        else:
                            break
                else:
                    break
            elif tabuleiro[linha_atual][coluna_atual] == peça_da_vez or tabuleiro[linha_atual][coluna_atual]== peça_dama:
                break
    return dama_capturar
def Principal_descendo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama):
    sair = 0
    dama_capturar = [[], []]
    while (linha_atual >= 0 and linha_atual <= 7) or (coluna_atual >= 0 and coluna_atual <= 7):
        tabuleiro[linha_atual][coluna_atual]
        linha_atual += 1
        coluna_atual += 1
        if linha_atual > 7 or coluna_atual > 7:
            break

        else:

            if tabuleiro[linha_atual][coluna_atual] == peça_espera or tabuleiro[linha_atual][coluna_atual] == peça_espera_dama:
                if sair == 0:
                    linha_atual += 1
                    coluna_atual += 1

                    if linha_atual > 7 or coluna_atual > 7:
                        break
                    else:
                        if tabuleiro[linha_atual][coluna_atual] == '-':
                            dama_capturar[0].append(linha_atual)
                            dama_capturar[1].append(coluna_atual)
                        else:
                            break
                else:
                    break
            elif tabuleiro[linha_atual][coluna_atual] == peça_da_vez or tabuleiro[linha_atual][coluna_atual]==peça_dama:
                break
    return dama_capturar
def Secundaria_subindo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama):
    sair = 0
    dama_capturar = [[], []]
    while (linha_atual>= 0 and linha_atual <= 7) or (coluna_atual >= 0 and coluna_atual <= 7):
        tabuleiro[linha_atual][coluna_atual]
        linha_atual -= 1
        coluna_atual += 1
        if linha_atual < 0 or coluna_atual > 7:
            break
        else:
            if tabuleiro[linha_atual][coluna_atual] == peça_espera or tabuleiro[linha_atual][coluna_atual] == peça_espera_dama:
                if sair == 0:
                    sair += 1
                    linha_atual -= 1
                    coluna_atual += 1
                    if linha_atual < 0 or coluna_atual > 7:
                        break
                    else:
                        if tabuleiro[linha_atual][coluna_atual] == '-':
                            dama_capturar[0].append(linha_atual)
                            dama_capturar[1].append(coluna_atual)
                        else:
                            break
                else:
                    break
            elif tabuleiro[linha_atual][coluna_atual] == peça_da_vez or tabuleiro[linha_atual][coluna_atual]==peça_dama:
                break
    return dama_capturar
def Secundaria_descendo(linha_atual, coluna_atual, peça_da_vez, peça_espera, peça_dama,peça_espera_dama):
    sair = 0
    dama_capturar = [[], []]
    while (linha_atual >= 0 and linha_atual <= 7) or (coluna_atual >= 0 and coluna_atual <= 7):
        tabuleiro[linha_atual][coluna_atual]
        linha_atual += 1
        coluna_atual -= 1
        if linha_atual > 7 or coluna_atual < 0:
            break
        else:

            if tabuleiro[linha_atual][coluna_atual] == peça_espera or tabuleiro[linha_atual][coluna_atual] == peça_espera_dama:
                if sair == 0:
                    sair += 1
                    linha_atual += 1
                    coluna_atual -= 1
                    if linha_atual > 7 or coluna_atual < 0:
                        break
                    else:
                        if tabuleiro[linha_atual][coluna_atual] == '-':
                            dama_capturar[0].append(linha_atual)
                            dama_capturar[1].append(coluna_atual)
                        else:
                            break
                else:
                    break
            elif tabuleiro[linha_atual][coluna_atual] == peça_da_vez or tabuleiro[linha_atual][coluna_atual]==peça_dama:
                break
    return dama_capturar
def Captura_obrigatoria_dama(vez):
    lin_col_dama_obr = [[],[]]

    if vez % 2 == 0:  # Se for par, quem mexe é o primeiro jogador.
        peça_da_vez = 'x'
        peça_espera = 'o'
        peça_dama = 'X'
        peça_espera_dama='O'
    else:
        peça_da_vez = 'o'
        peça_espera = 'x'
        peça_dama = 'O'
        peça_espera_dama='X'

    for i in range(len((tabuleiro))):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == peça_dama:
                dama_percorre = Dama_percorre(i, j, peça_da_vez, peça_espera, peça_dama, peça_espera_dama)
                if dama_percorre!=[[],[]]:
                    lin_col_dama_obr[0].append(i)
                    lin_col_dama_obr[1].append(j)

    return lin_col_dama_obr
def Captura_mover_dama(linha_atual, coluna_atual, linha_desejada, coluna_desejada, vez):
    lista_dama = []

    if linha_desejada > linha_atual and coluna_desejada > coluna_atual:
        lista_dama = Dama_principal_descendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada)
    elif linha_desejada < linha_atual and coluna_desejada < coluna_atual:
        lista_dama = Dama_principal_ascendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada)
    elif linha_desejada > linha_atual and coluna_desejada < coluna_atual:
        lista_dama = Dama_secundaria_descendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada)
    elif linha_desejada < linha_atual and coluna_desejada > coluna_atual:
        lista_dama = Dama_secundaria_ascendente(linha_atual, coluna_atual, linha_desejada, coluna_desejada)
    cont_cap_dama = 0
    for i in range(len(lista_dama)):
        if lista_dama[i] == peça_espera:
            cont_cap_dama += 1
            posicao = i + 1
    if cont_cap_dama > 1:
        print('Jogada não permitida')
        vez += 1
    elif cont_cap_dama == 1:
        if linha_desejada > linha_atual and coluna_desejada > coluna_atual:
            lista_capturar_dama.append('capturar dama')
            tabuleiro[linha_atual + posicao][coluna_atual + posicao] = '-'
            tabuleiro[linha_atual][coluna_atual] = '-'
            tabuleiro[linha_desejada][coluna_desejada] = peça_dama
            dama_capturar = Captura_obrigatoria_dama(vez)
            print(dama_capturar)
            dama_percorre=Dama_percorre(linha_desejada,coluna_desejada,peça_da_vez,peça_espera,peça_dama,peça_espera_dama)
            if dama_percorre != [[],[]]:
                captura_consecutiva.append('consecutiva')
        elif linha_desejada < linha_atual and coluna_desejada < coluna_atual:
            lista_capturar_dama.append('capturar dama')
            tabuleiro[linha_atual - posicao][coluna_atual - posicao] = '-'
            tabuleiro[linha_atual][coluna_atual] = '-'
            tabuleiro[linha_desejada][coluna_desejada] = peça_dama
            dama_capturar = Captura_obrigatoria_dama(vez)
            print(dama_capturar)
            dama_percorre = Dama_percorre(linha_desejada, coluna_desejada, peça_da_vez, peça_espera, peça_dama,
                                          peça_espera_dama)
            if dama_percorre != [[],[]]:
                captura_consecutiva.append('consecutiva')
        elif linha_desejada > linha_atual and coluna_desejada < coluna_atual:
            lista_capturar_dama.append('capturar dama')
            tabuleiro[linha_atual + posicao][coluna_atual - posicao] = '-'
            tabuleiro[linha_atual][coluna_atual] = '-'
            tabuleiro[linha_desejada][coluna_desejada] = peça_dama
            dama_capturar = Captura_obrigatoria_dama(vez)
            print(dama_capturar)

            dama_percorre = Dama_percorre(linha_desejada, coluna_desejada, peça_da_vez, peça_espera, peça_dama,
                                          peça_espera_dama)
            if dama_percorre != [[],[]]:
                captura_consecutiva.append('consecutiva')

        elif linha_desejada < linha_atual and coluna_desejada > coluna_atual:
            lista_capturar_dama.append('capturar dama')
            tabuleiro[linha_atual - posicao][coluna_atual + posicao] = '-'
            tabuleiro[linha_atual][coluna_atual] = '-'
            tabuleiro[linha_desejada][coluna_desejada] = peça_dama
            dama_capturar = Captura_obrigatoria_dama(vez)
            print(dama_capturar)
            dama_percorre = Dama_percorre(linha_desejada, coluna_desejada, peça_da_vez, peça_espera, peça_dama,
                                          peça_espera_dama)
            if dama_percorre != [[],[]]:
                captura_consecutiva.append('consecutiva')
    elif cont_cap_dama == 0:

        if cap_obrg == [[], []]:
            lista_capturar_dama.append('mover dama')
            tabuleiro[linha_atual][coluna_atual] = '-'
            tabuleiro[linha_desejada][coluna_desejada] = peça_dama
        else:
            print ('Jogada não permitida')
            jogada_não_permitida.append('não')
    return
def Pontuaçao(pontuaçao_jog1, pontuaçao_jog2):
    lista_pontuaçao = []
    pontuaçao_jog1 = 0
    pontuaçao_jog2 = 0

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 'x' or tabuleiro[i][j] == 'X':
                pontuaçao_jog1+=1
            elif tabuleiro[i][j] == 'o' or tabuleiro[i][j] == 'O':
                pontuaçao_jog2+=1

    lista_pontuaçao.append(pontuaçao_jog1)
    lista_pontuaçao.append(pontuaçao_jog2)
    return lista_pontuaçao



#Código
vez = 0
cont_sel_dama = 0
while True:
    if vez % 2 == 0:  # Se for par, quem mexe é o primeiro jogador.
        numero_jogador = 1
        peça_da_vez = 'x'
        peça_espera = 'o'
        peça_dama = 'X'
        peça_espera_dama = 'O'
    else:
        numero_jogador = 2
        peça_da_vez = 'o'
        peça_espera = 'x'
        peça_dama = 'O'
        peça_espera_dama = 'X'

    cap_obrg = Captura_obrigatoria(vez)
    cap_obrg_dama = Captura_obrigatoria_dama(vez)
    Imprimir_tabuleiro()

    print('Vez do jogador' + str(numero_jogador)+', sua peça é' + " " +str(peça_da_vez))
    linha_atual = input('Informe a linha de escolha: ')
    linha_atual = Entrada_tratada_linha(linha_atual)
    while linha_atual.isdigit() == False:
        print('Apenas números! Por favor.')
        linha_atual = input('Informe a linha de escolha: ')
        linha_atual = Entrada_tratada_linha(linha_atual)

    coluna_atual = input('Informe a coluna de escolha: ')
    coluna_atual = Entrada_tratada_coluna(coluna_atual)
    while coluna_atual.isdigit() == False:
        print('Apenas números! Por favor.')
        coluna_atual = input('Informe a coluna de escolha: ')
        coluna_atual = Entrada_tratada_coluna(coluna_atual)

    linha_desejada = input('Informe a linha desejada: ')
    linha_desejada = Linha_desejada(linha_desejada)
    while linha_desejada.isdigit() == False:
        print('Apenas números! Por favor.')
        linha_desejada = input('Informe a linha desejada: ')
        linha_desejada = Linha_desejada(linha_desejada)

    coluna_desejada = input('Informe a coluna desejada: ')
    coluna_desejada = Coluna_desejada(coluna_desejada)
    while coluna_desejada.isdigit() == False:
        print('Apenas números! Por favor.')
        coluna_desejada = input('Informe a coluna desejada: ')
        coluna_desejada = Coluna_desejada(coluna_desejada)

    linha_atual, linha_desejada = int(linha_atual), int(linha_desejada)
    coluna_atual, coluna_desejada = int(coluna_atual), int(coluna_desejada)
    cap_obrg_dama=Captura_obrigatoria_dama(vez)

    entradas=Entrada_de_formações(linha_atual,coluna_atual,linha_desejada,coluna_desejada)
    linha_atual=entradas[0]
    coluna_atual=entradas[1]
    linha_desejada=entradas[2]
    coluna_desejada=entradas[3]


    if tabuleiro[linha_atual][coluna_atual] == peça_dama:

        while abs(linha_atual-linha_desejada) != abs(coluna_atual-coluna_desejada):
            print('Jogada nao permitida')
            Imprimir_tabuleiro()
            print('Vez do jogador' + str(numero_jogador))
            linha_atual = input('Informe a linha de escolha: ')
            linha_atual = Entrada_tratada_linha(linha_atual)
            while linha_atual.isdigit() == False:
                print('Apenas números! Por favor.')
                linha_atual = input('Informe a linha de escolha: ')
                linha_atual = Entrada_tratada_linha(linha_atual)

            coluna_atual = input('Informe a coluna de escolha: ')
            coluna_atual = Entrada_tratada_coluna(coluna_atual)
            while coluna_atual.isdigit() == False:
                print('Apenas números! Por favor.')
                coluna_atual = input('Informe a coluna de escolha: ')
                coluna_atual = Entrada_tratada_coluna(coluna_atual)

            linha_desejada = input('Informe a linha desejada: ')
            linha_desejada = Linha_desejada(linha_desejada)
            while linha_desejada.isdigit() == False:
                print('Apenas números! Por favor.')
                linha_desejada = input('Informe a linha desejada: ')
                linha_desejada = Linha_desejada(linha_desejada)

            coluna_desejada = input('Informe a coluna desejada: ')
            coluna_desejada = Coluna_desejada(coluna_desejada)
            while coluna_desejada.isdigit() == False:
                print('Apenas números! Por favor.')
                coluna_desejada = input('Informe a coluna desejada: ')
                coluna_desejada = Coluna_desejada(coluna_desejada)

            linha_atual, linha_desejada = int(linha_atual), int(linha_desejada)
            coluna_atual, coluna_desejada = int(coluna_atual), int(coluna_desejada)

            if abs(linha_atual-linha_desejada) != abs(coluna_atual-coluna_desejada):
                break

        if cap_obrg_dama !=[[],[]]:  # Verifica se linha atual e coluna atual estão iguais a lista de captura obrigatoria
            while (((linha_atual not in cap_obrg_dama[0]) and (coluna_atual not in cap_obrg_dama[1]))) or ((
                        (linha_atual in cap_obrg_dama[0]) and (coluna_atual not in cap_obrg_dama[1]))) or ((
                        (linha_atual not in cap_obrg_dama[0]) and (coluna_atual in cap_obrg_dama[1]))):
                print('Jogada nao permitida')
                Imprimir_tabuleiro()
                print('Vez do jogador' + str(numero_jogador))
                entradas=Entrada_de_formações(linha_atual,coluna_atual,linha_desejada,coluna_desejada)
                linha_atual=entradas[0]
                coluna_atual=entradas[1]
                linha_desejada=entradas[2]
                coluna_desejada=entradas[3]

                if (linha_atual in cap_obrg_dama[0]) and (coluna_atual in cap_obrg_dama[1]):
                    break

        captura_mover_dama = Captura_mover_dama(linha_atual, coluna_atual, linha_desejada, coluna_desejada, vez)
        if 'consecutiva' in captura_consecutiva:
            vez+=1
        if 'não' in jogada_não_permitida:
            vez+=1

        lista_capturar_dama = []
        captura_consecutiva=[]
        jogada_não_permitida=[]
    else:
        entradas=Entrada_de_formações(linha_atual,coluna_atual,linha_desejada,coluna_desejada)
        linha_atual=entradas[0]
        coluna_atual=entradas[1]
        linha_desejada=entradas[2]
        coluna_desejada=entradas[3]
        if len(cap_obrg[0]) > 0:  # Verifica se linha atual e coluna atual estão iguais a lista de captura obrigatoria
            while (((linha_atual not in cap_obrg[0]) and (coluna_atual not in cap_obrg[1]))) or ((
                        (linha_atual in cap_obrg[0]) and (coluna_atual not in cap_obrg[1]))) or ((
                        (linha_atual not in cap_obrg[0]) and (coluna_atual in cap_obrg[1]))):
                print('Jogada nao permitida')
                Imprimir_tabuleiro()
                print('Vez do jogador' + str(numero_jogador))
                linha_atual = input('Informe a linha de escolha: ')
                linha_atual = Entrada_tratada_linha(linha_atual)
                while linha_atual.isdigit() == False:
                    print('Apenas números! Por favor.')
                    linha_atual = input('Informe a linha de escolha: ')
                    linha_atual = Entrada_tratada_linha(linha_atual)

                coluna_atual = input('Informe a coluna de escolha: ')
                coluna_atual = Entrada_tratada_coluna(coluna_atual)
                while coluna_atual.isdigit() == False:
                    print('Apenas números! Por favor.')
                    coluna_atual = input('Informe a coluna de escolha: ')
                    coluna_atual = Entrada_tratada_coluna(coluna_atual)

                linha_desejada = input('Informe a linha desejada: ')
                linha_desejada = Linha_desejada(linha_desejada)
                while linha_desejada.isdigit() == False:
                    print('Apenas números! Por favor.')
                    linha_desejada = input('Informe a linha desejada: ')
                    linha_desejada = Linha_desejada(linha_desejada)

                coluna_desejada = input('Informe a coluna desejada: ')
                coluna_desejada = Coluna_desejada(coluna_desejada)
                while coluna_desejada.isdigit() == False:
                    print('Apenas números! Por favor.')
                    coluna_desejada = input('Informe a coluna desejada: ')
                    coluna_desejada = Coluna_desejada(coluna_desejada)

                linha_atual, linha_desejada = int(linha_atual), int(linha_desejada)
                coluna_atual, coluna_desejada = int(coluna_atual), int(coluna_desejada)

                if (linha_atual == cap_obrg[0][0] and tabuleiro[linha_desejada - 1][
                        coluna_desejada - 1] == peça_espera) or (
                        linha_atual == cap_obrg[0][0] and tabuleiro[linha_desejada - 1][
                        coluna_desejada + 1] == peça_espera) or (
                        linha_atual == cap_obrg[0][0] and tabuleiro[linha_desejada + 1][
                        coluna_desejada - 1] == peça_espera) or (
                        linha_atual == cap_obrg[0][0] and tabuleiro[linha_desejada + 1][
                        coluna_desejada + 1] == peça_espera) and coluna_atual == cap_obrg[1][0]:
                    break

        # capturar
        lista_capturar = Capturar(linha_atual, coluna_atual, linha_desejada, coluna_desejada)
        captura_consecutiva =Captura_obrigatoria(vez)
        cap_obrg_dama = Captura_obrigatoria_dama(vez)
        Verificar_dama()

        if len(captura_consecutiva[0]) > 0 and (
            (linha_desejada in captura_consecutiva[0]) and (coluna_desejada in captura_consecutiva[1])):
            vez += 1
        pontuaçao = Pontuaçao(pontuaçao_jog1, pontuaçao_jog2)
        pontuaçao_jog1 = pontuaçao[0]
        pontuaçao_jog2 = pontuaçao[1]
        # mover
        if len(lista_capturar) > 1:
            vez += 1
        else:
            mover = Mover(linha_atual, coluna_atual, linha_desejada, coluna_desejada, vez, cap_obrg,pontuaçao_jog1,pontuaçao_jog2 )

            if 'nao move' in mover:
                vez += 1
        Verificar_dama()

    pontuaçao = Pontuaçao(pontuaçao_jog1, pontuaçao_jog2)
    pontuaçao_jog1 = pontuaçao[0]
    print('Jogador 1: Faltam ' + str(pontuaçao_jog1)+ " peças")
    pontuaçao_jog2 = pontuaçao[1]
    print('Jogador 2: Faltam ' + str(pontuaçao_jog2)+ " peças")
    if 'Impossivel' in jogada_impossivel:
        if pontuaçao_jog1>pontuaçao_jog2:
            Imprimir_tabuleiro()
            print('Jogador 1 foi o vencedor')
            break
        elif pontuaçao_jog2>pontuaçao_jog1:
            Imprimir_tabuleiro()
            print('Jogador 2 foi o vencedor')
            break
    jogada_impossivel=[]
    if pontuaçao_jog1 == 0:
        Imprimir_tabuleiro()
        print('Jogador 2 foi o vencedor')
        break
    elif pontuaçao_jog2 == 0:
        Imprimir_tabuleiro()
        print('Jogador 1 foi o vencedor')
        break
    elif pontuaçao_jog1 == 1 and pontuaçao_jog2 == 1:
        Imprimir_tabuleiro()
        print('Empate')
    vez += 1
