frase = 'Curso em Vídeo Python'
print(frase[3]) # FAZ IMPRIRMIR SOMENTE A 4 LETRA.
print(frase[3:13]) # FAZ IMPRIMIR DA 4 LETRA ATÉ A 12 LETRA.
print(frase[:13]) # FAZ IMPRIMIR DO INICIO ATÉ O 12 LETRA.
print(frase[13:]) # FAZ IMPRIMIR DA 13 ATÉ O FINAL.
print(frase[3:13:2]) # FAZ IMPRIMIR DA 4 LETRA ATÉ A 12 LETRA COM SALTO 2 EM 2.
print(frase[3::2]) # FAZ IMPRIMIR DA 4 LETRA ATÉ O FINAL COM SALTO DE 2 EM 2.
print(frase[::2]) # FAZ IMPRIMIR DO INICO ATÉ O FINAL COM SALTO DE 2 EM 2.
print(frase.count('o')) # FAZ A CONTAGEM DE QUANTOS 'o' (minusculo) tem na variavel frase.
print(frase.count('O')) # FAZ A CONTAGEM DE QUANTOS 'O' (Maiusculo) tem na variavel frase.
print(frase.upper().count('O')) # O UPPER FAZ JOGAR A VARIAVEL FRASE PARA MAIUSCULO E COUNT FAZ A CONTAGEM DE QUANTOS 'O'(Maiusculo) tem na variavel frase.
print(len(frase)) # LEN SERVE PARA VER QUAL É O TAMANHO DA FRASE, SE COLOCAR ESPAÇOS NA VARIAVEL COMO: frase = '  Curso em Video Python  ', AUMENTA NA CONTAGEM.
print(len(frase.strip())) # O .strip SERVE PARA REMOVER OS ESPAÇOS INDESEJADOS NO COMEÇO E FINAL DA FRASE
print(frase.replace('Python', 'Android')) # REPLACE FAZ A TROCA DA FRASE, PYTHON POR ANDROID.
print('Curso' in frase) # in MANDAR VER SE A PALAVRA 'CURSO' ESTÁ DENTRO DA FRASE.
print(frase.find('Curso')) # .find MANDAR VER EM QUAL EM QUAL POSIÇÃO COMEÇA A FRASE.
print(frase.lower().find('vídeo')) # O .lower FEZ A FRASE FICAR EM MINUSCULO E o .find fez ver em qual posição começa a frase vídeo.
print(frase.split()) # CRIA UMA LISTA COM SEPARADOR DE ESPAÇOS
dividido = frase.split() # CRIEI UM OBJETO CHAMADO DIVIDIDO QUE RECEBE FRASE E FORMA UMA LISTA SEPARADO DOS ESPAÇOS. 
print(dividido[0]) # MANDEI IMPRIMIR SOMENTE O PRIMEIRO ITEM DA LISTA QUE É 0
print(dividido[1]) # MANDEI IMPRIMIR SOMENTE O SEGUNDO ITEM DA LISTA QUE É 1
print(dividido[2]) # MANDEI IMPRIMIR SOMENTE O TERCEIRO ITEM DA LISTA QUE É 2
print(dividido[3]) # MANDEI IMPRIMIR SOMENTE O QUARTO ITEM DA LISTA QUE É 3
print(dividido[2][3]) # MANDEI IMPRIMIR SOMENTE A LETRA QUE ESTA NA POSIÇÃO 3 DO ITEM 2.
print("""asdawdasdawdasdawdasdawdasdawdawdasdawdasdawdasdadw
      asdaw2dasdawdasdawdawsdasdwdawdasdawdawdasdawdawdasda
      awdasdawdasdawdasdawdasdawdasdawdasdawdasdawdawdasdaw""") # AS 3 ASPAS FAZ IMPRIMIR O TEXTO TODO EM VARIAS LINHAS.