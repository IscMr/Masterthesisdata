# Procurar palavras corpus.
# Inicializa o corpus
a = open("<Inserir o caminho do arquivo em formato CoNLL-U>",
         'r', encoding='utf8').readlines()
tratado = []
for linha in a:
    tratado.append(linha.split('\t'))

# Lista de palavras buscadas
w_list = ['não', 'jamais', 'nada', 'nem', 'nenhum',
          'ninguém', 'nunca', 'sem', 'sequer', 'tampouco', 'exceto', 'menos', 'fora', "exclusive", "excluso", 'afora', 'salvo', 'senão', 'tirante', 'excepto']

dicf = {}
negasent = 0
totalsent = 0


for linha in tratado:
    try:
        if '# text' in linha[0]:
            # Contagem do total de sentenças
            snt = linha[0]
            totalsent = totalsent+1
            # Contador para a contagem de sentenças em que ao menos uma das palavras aparecem
            for nega in w_list:
                if nega in linha[0].lower().split(' '):
                    negasent = negasent+1
                    break
    except:
        0
    # Extração dos dados
    for palavra in w_list:
        try:
            if palavra == linha[2]:
                if palavra in dicf:
                    if linha[3] in dicf[linha[2]]:
                        if linha[5] in dicf[linha[2]][linha[3]]:
                            if linha[7] in dicf[linha[2]][linha[3]][linha[5]]:
                                dicf[linha[2]][linha[3]][linha[5]][linha[7]
                                                                   ][0] = dicf[linha[2]][linha[3]][linha[5]][linha[7]][0]+1
                                dicf[linha[2]][linha[3]][linha[5]
                                                         ][linha[7]].append(str(snt))

                            if linha[7] not in dicf[linha[2]][linha[3]][linha[5]]:
                                dicf[linha[2]][linha[3]
                                               ][linha[5]][linha[7]] = [1]
                                dicf[linha[2]][linha[3]][linha[5]
                                                         ][linha[7]].append(str(snt))

                        if linha[5] not in dicf[linha[2]][linha[3]]:
                            dicf[linha[2]][linha[3][linha[5]]] = {}
                            dicf[linha[2]][linha[3]][linha[5]][linha[7]] = [1]
                            dicf[linha[2]][linha[3]][linha[5]
                                                     ][linha[7]].append(str(snt))

                    if linha[3] not in dicf[linha[2]]:
                        dicf[linha[2]][linha[3]] = {}
                        dicf[linha[2]][linha[3]][linha[5]] = {}
                        dicf[linha[2]][linha[3]][linha[5]][linha[7]] = [1]
                        dicf[linha[2]][linha[3]][linha[5]
                                                 ][linha[7]].append(str(snt))

                if palavra not in dicf:
                    dicf[linha[2]] = {}
                    dicf[linha[2]][linha[3]] = {}
                    dicf[linha[2]][linha[3]][linha[5]] = {}
                    dicf[linha[2]][linha[3]][linha[5]][linha[7]] = [1]
                    dicf[linha[2]][linha[3]][linha[5]
                                             ][linha[7]].append(str(snt))
        except:
            0

# Impressão dos resultados

for lema in dicf:
    saida = open("<Inserir o caminho de saída>\\saida_" +
                 str(lema)+".txt", 'w', encoding='utf8')
    for pos in dicf[lema]:
        for feature in dicf[lema][pos]:
            for dprel in dicf[lema][pos][feature]:
                saida.write('lema')
                saida.write('\t')
                saida.write('pos')
                saida.write('\t')
                saida.write('feature')
                saida.write('\t')
                saida.write('dprel')
                saida.write('\t')
                saida.write('ocorrências')
                saida.write('\n')
                saida.write(str(lema))
                saida.write('\t')
                saida.write(str(pos))
                saida.write('\t')
                saida.write(str(feature))
                saida.write('\t')
                saida.write(str(dprel))
                saida.write('\t')
                saida.write(str(dicf[lema][pos][feature][dprel][0]))
                saida.write('\n')
                for elemento in dicf[lema][pos][feature][dprel]:
                    if type(elemento) is not int:
                        saida.write(str(elemento))
                        saida.write('\n')
    saida.close()
