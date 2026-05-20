# =============================================================================
# TITANIC - REGRESSÃO LOGÍSTICA (Implementação Manual)
# =============================================================================
# IDEIA GERAL:
# Este programa tenta prever se um passageiro sobreviveu ou não.
#
# Saída esperada:
# 0 = não sobreviveu
# 1 = sobreviveu
#
# O modelo usado aqui é Regressão Logística.
# Ela aplica a função Sigmoid sobre o resultado da combinação linear.
#
# Exemplo simplificado:
# z  = 0.2 + 0.5*sexo - 0.3*classe     <- combinação linear (igual antes)
# ŷ  = sigmoid(z) = 1 / (1 + e^-z)     <- NOVO: aplica sigmoid
#
# A função Sigmoid "espreme" qualquer número real para o intervalo (0, 1):
# sigmoid(-5)  ≈ 0.007
# sigmoid( 0)  = 0.500
# sigmoid(+5)  ≈ 0.993
#
# Assim a saída SEMPRE representa uma probabilidade entre 0 e 1.
# Isso resolve o problema da Regressão Linear que gerava valores
# como -0.1 ou 1.3, impossíveis de interpretar como probabilidade.
#
# ─────────────────────────────────────────────────────────────────
# GUIA DE MUDANÇAS (em relação ao titanic_treino_comentado.py):
# ─────────────────────────────────────────────────────────────────
# Busque por ">>> MUDANÇA" para encontrar cada ponto alterado.
# O código antigo da Regressão Linear está comentado logo abaixo
# de cada mudança, para facilitar a comparação.
#
# Resumo das 6 mudanças:
#   1. import math                          (seção IMPORTAÇÕES)
#   2. ARQUIVO_PESOS com nome diferente     (seção CONFIGURAÇÕES)
#   3. Nova função sigmoid(z)               (seção 3)
#   4. prever_logistica usa sigmoid         (seção 3)
#   5. calcular_cross_entropy no lugar de calcular_mse (seção 3)
#   6. treinar usa prever_logistica + imprime Cross-Entropy (seção 4)
#   7. avaliar usa prever_logistica + remove aviso fora de [0,1] (seção 5)
#   8. exibir_pesos mostra sigmoid na fórmula (seção 6)
#   9. salvar_modelo salva tipo logistica   (seção 7)
# =============================================================================


# =============================================================================
# IMPORTAÇÕES
# =============================================================================

import csv
# Importa a biblioteca para ler arquivos CSV.
# CSV é um tipo de arquivo em tabela, como se fosse uma planilha simples.

import json
# Importa a biblioteca para salvar dados em formato JSON.

# >>> MUDANÇA 1: import math — adicionado
# Antes (Regressão Linear): esta linha não existia.
import math
# Importa funções matemáticas.
# Aqui vamos usar math.exp para calcular e^x (exponencial),
# necessária dentro da função Sigmoid.

import os
# Importa ferramentas do sistema operacional.
# Aqui vamos usar para verificar se arquivos existem.


# =============================================================================
# CONFIGURAÇÕES
# =============================================================================

ARQUIVO_TREINO   = "train.csv"
# Arquivo com dados de treino.
# Ele possui a coluna Survived, que é a resposta correta.

ARQUIVO_TESTE    = "test.csv"
# Arquivo com dados de teste.
# Ele não possui a resposta correta.

ARQUIVO_GABARITO = "gender_submission.csv"
# Arquivo com as respostas corretas do conjunto de teste.

# >>> MUDANÇA 2: nome do arquivo de pesos — alterado
# Antes (Regressão Linear):
# ARQUIVO_PESOS = "modelo_pesos.json"
ARQUIVO_PESOS    = "modelo_pesos_logistica.json"
# Nome diferente para não sobrescrever o modelo de Regressão Linear.


# =============================================================================
# HIPERPARÂMETROS
# =============================================================================

TAXA_APRENDIZADO = 0.1
# Define o tamanho do passo na atualização dos pesos.
#
# Exemplo:
# se um peso vale 0.50 e o ajuste calculado é 0.10:
# novo_peso = 0.50 - 0.1*0.10 = 0.49
#
# Quanto maior a taxa, maior o passo.

EPOCAS = 5000
# Quantas vezes o algoritmo passa pelos dados inteiros.

IMPRIMIR_A_CADA = 500
# A cada 500 épocas, mostra o erro na tela.


# =============================================================================
# 1. FUNÇÕES AUXILIARES
# (sem mudanças — idênticas à Regressão Linear)
# =============================================================================

def calcular_mediana(valores):
    # "def" cria uma função.
    # Função é um bloco de código reutilizável.
    #
    # Esta função recebe uma lista de números e devolve a mediana.
    #
    # Exemplo:
    # [10, 30, 20] -> ordenado fica [10, 20, 30]
    # mediana = 20
    #
    # Exemplo com quantidade par:
    # [10, 20, 30, 40]
    # mediana = (20 + 30) / 2 = 25

    ordenados = sorted(valores)
    # Ordena os valores do menor para o maior.

    n = len(ordenados)
    # Conta quantos elementos existem na lista.

    return (ordenados[n//2 - 1] + ordenados[n//2]) / 2 if n % 2 == 0 else ordenados[n//2]
    # Se n for par:
    # pega os dois do meio e faz a média.
    #
    # Se n for ímpar:
    # pega o valor do meio.
    #
    # "return" devolve o resultado da função.


def preprocessar_linha(r, mediana_age, mediana_fare):
    # Esta função pega UMA linha do CSV e transforma em números.
    #
    # "r" é um dicionário com dados da linha.
    #
    # Exemplo de r:
    # {
    #   'Pclass': '3',
    #   'Sex': 'male',
    #   'Age': '22',
    #   'SibSp': '1',
    #   'Parch': '0',
    #   'Fare': '7.25',
    #   'Embarked': 'S'
    # }
    #
    # O objetivo é transformar isso em uma lista numérica:
    # [3.0, 0.0, 22.0, 1.0, 0.0, 7.25, 2.0]

    mapa_sex = {'male': 0.0, 'female': 1.0}
    # Transforma sexo em número.
    #
    # Exemplo:
    # male   -> 0.0
    # female -> 1.0

    mapa_embarked = {'C': 0.0, 'Q': 1.0, 'S': 2.0, '': 2.0}
    # Transforma porto de embarque em número.
    #
    # Exemplo:
    # C -> 0.0
    # Q -> 1.0
    # S -> 2.0
    # vazio -> 2.0

    return [
        float(r['Pclass']),
        # Converte a classe em número decimal.
        # Exemplo: '3' -> 3.0

        mapa_sex.get(r['Sex'].strip().lower(), 0.0),
        # Pega o sexo, tira espaços, deixa minúsculo
        # e procura no dicionário.
        #
        # Exemplo:
        # ' Male ' -> 'male' -> 0.0

        float(r['Age']) if r['Age'].strip() != '' else mediana_age,
        # Se a idade estiver preenchida, converte.
        # Se estiver vazia, usa a mediana.
        #
        # Exemplo:
        # Age = '' -> usa mediana_age

        float(r['SibSp']),
        # Número de irmãos/cônjuges a bordo.

        float(r['Parch']),
        # Número de pais/filhos a bordo.

        float(r['Fare']) if r['Fare'].strip() != '' else mediana_fare,
        # Se a tarifa estiver vazia, usa a mediana da tarifa.

        mapa_embarked.get(r['Embarked'].strip(), 2.0),
        # Converte porto de embarque em número.
    ]


def carregar_treino(caminho):
    # Lê o arquivo de treino e retorna:
    # X = lista de entradas
    # y = lista de respostas corretas
    # med_age = mediana da idade
    # med_fare = mediana da tarifa

    registros = list(csv.DictReader(open(caminho, encoding='utf-8')))
    # Lê o CSV inteiro como uma lista de dicionários.
    #
    # Exemplo:
    # registros[0]['Age']
    # registros[0]['Survived']

    med_age = calcular_mediana([float(r['Age']) for r in registros if r['Age'].strip() != ''])
    # Cria uma lista só com as idades preenchidas e calcula a mediana.
    #
    # Exemplo:
    # idades válidas = [22, 38, 26, 35, ...]
    # mediana = valor central

    med_fare = calcular_mediana([float(r['Fare']) for r in registros if r['Fare'].strip() != ''])
    # Faz a mesma coisa para Fare.

    X, y = [], []
    # Cria duas listas vazias.
    #
    # X vai guardar as features
    # y vai guardar as respostas

    for r in registros:
        # "for" repete o bloco para cada linha.

        try:
            # "try" tenta executar este trecho.
            # Se der erro, vai para o "except".

            X.append(preprocessar_linha(r, med_age, med_fare))
            # Converte a linha para números e adiciona em X.

            y.append(float(r['Survived']))
            # Pega a resposta correta da linha.
            #
            # Exemplo:
            # '0' -> 0.0
            # '1' -> 1.0

        except (ValueError, KeyError):
            # Se der erro de valor ou coluna ausente, ignora a linha.
            continue

    return X, y, med_age, med_fare
    # Devolve tudo pronto.


def carregar_teste(caminho_teste, caminho_gabarito, med_age, med_fare):
    # Lê o conjunto de teste e também as respostas corretas.
    #
    # O test.csv não tem Survived.
    # Então usamos o gabarito para comparar depois.

    gabarito = {}
    # Cria um dicionário vazio.

    with open(caminho_gabarito, encoding='utf-8') as f:
        for linha in csv.DictReader(f):
            gabarito[linha['PassengerId'].strip()] = float(linha['Survived'])
    # Monta um dicionário assim:
    # gabarito['892'] = 0.0
    # gabarito['893'] = 1.0

    X_teste, y_real, ids = [], [], []
    # X_teste = entradas do teste
    # y_real  = respostas corretas
    # ids     = ids dos passageiros

    with open(caminho_teste, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            pid = r['PassengerId'].strip()
            # Pega o id do passageiro.

            if pid not in gabarito:
                continue
            # Se não existir no gabarito, pula.

            try:
                X_teste.append(preprocessar_linha(r, med_age, med_fare))
                # Converte a linha do teste em números.

                y_real.append(gabarito[pid])
                # Guarda a resposta correta.

                ids.append(pid)
                # Guarda o id.

            except (ValueError, KeyError):
                continue
            # Se houver erro na linha, pula.

    return X_teste, y_real, ids


# =============================================================================
# 2. NORMALIZAÇÃO
# (sem mudanças — idêntica à Regressão Linear)
# =============================================================================

def calcular_params_normalizacao(X):
    # Calcula o menor e o maior valor de cada coluna.
    #
    # Isso é importante para a normalização Min-Max.

    n_f = len(X[0])
    # Descobre quantas features existem em cada linha.

    mins = [min(linha[j] for linha in X) for j in range(n_f)]
    # Para cada coluna, pega o menor valor.

    maxs = [max(linha[j] for linha in X) for j in range(n_f)]
    # Para cada coluna, pega o maior valor.

    return mins, maxs


def normalizar(X, mins, maxs):
    # Aplica a normalização Min-Max:
    #
    # x_normalizado = (x - min) / (max - min)
    #
    # Exemplo:
    # se idade mínima = 0.42
    # se idade máxima = 80
    # se idade = 20
    #
    # idade_normalizada = (20 - 0.42) / (80 - 0.42)

    X_norm = []
    # Lista vazia para guardar o resultado.

    for linha in X:
        X_norm.append([
            (linha[j] - mins[j]) / (maxs[j] - mins[j]) if (maxs[j] - mins[j]) != 0 else 0.0
            for j in range(len(linha))
        ])
        # Faz a normalização para cada coluna.
        #
        # Se max == min, coloca 0.0 para evitar divisão por zero.

    return X_norm


# =============================================================================
# 3. MODELO DE REGRESSÃO LOGÍSTICA
# =============================================================================
# >>> MUDANÇA 3, 4 e 5 estão nesta seção.
#
# Na Regressão Linear, a seção 3 tinha apenas:
#   - prever_linear(x, pesos)     -> devolvia z diretamente
#   - calcular_mse(X, y, pesos)   -> media dos erros quadráticos
#
# Na Regressão Logística, esta seção passa a ter:
#   - sigmoid(z)                          -> NOVA função
#   - prever_logistica(x, pesos)          -> chama sigmoid no final
#   - calcular_cross_entropy(X, y, pesos) -> nova função de perda
# =============================================================================

# >>> MUDANÇA 3: função sigmoid — NOVA (não existia na Regressão Linear)
def sigmoid(z):
    # A função Sigmoid transforma qualquer número real em um valor entre 0 e 1.
    #
    # Fórmula:
    # sigmoid(z) = 1 / (1 + e^-z)
    #
    # Exemplos:
    # sigmoid(-10) ≈ 0.0000454  (quase 0)
    # sigmoid( -2) ≈ 0.119
    # sigmoid(  0) = 0.500
    # sigmoid( +2) ≈ 0.881
    # sigmoid(+10) ≈ 0.9999546  (quase 1)
    #
    # Por que isso é útil?
    # A Regressão Linear pode gerar z = -0.5 ou z = 1.8.
    # Depois de sigmoid: sigmoid(-0.5) ≈ 0.38, sigmoid(1.8) ≈ 0.86.
    # O resultado SEMPRE fica entre 0 e 1.

    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
        # Cálculo padrão para z não-negativo.
        # math.exp(-z) = e^-z
        #
        # Exemplo: z = 2
        # e^-2 ≈ 0.135
        # 1 / (1 + 0.135) ≈ 0.881

    else:
        e = math.exp(z)
        return e / (1.0 + e)
        # Para z negativo, usamos esta forma equivalente para evitar overflow.
        #
        # Se z = -500, e^500 seria um número gigantesco que estoura a memória.
        # Mas e^-500 ≈ 0, então e^-500 / (1 + e^-500) ≈ 0, que é correto.
        #
        # Forma equivalente matematicamente:
        # 1/(1 + e^-z) = e^z / (e^z + 1)


# >>> MUDANÇA 4: prever_logistica — substitui prever_linear
# Antes (Regressão Linear):
# def prever_linear(x, pesos):
#     resultado = pesos[0]
#     for j in range(len(x)):
#         resultado += pesos[j + 1] * x[j]
#     return resultado          # <- devolvia z diretamente, sem sigmoid
def prever_logistica(x, pesos):
    # Calcula a previsão usando a fórmula:
    #
    # z  = w0 + w1*x1 + w2*x2 + ... + wn*xn  <- combinação linear (igual antes)
    # ŷ  = sigmoid(z)                          <- NOVA etapa
    #
    # Exemplo pequeno:
    # pesos = [0.2, 0.5, -0.3]
    # x = [1.0, 0.4]
    #
    # z  = 0.2 + 0.5*1.0 + (-0.3)*0.4
    # z  = 0.2 + 0.5 - 0.12 = 0.58
    # ŷ  = sigmoid(0.58) ≈ 0.641
    #
    # Na Regressão Linear a saída seria 0.58 diretamente.
    # Na Regressão Logística a saída é sigmoid(0.58) ≈ 0.641.

    z = pesos[0]
    # Começa com o bias.
    # O bias é o primeiro peso, uma espécie de valor inicial.

    for j in range(len(x)):
        z += pesos[j + 1] * x[j]
        # Soma cada termo:
        # peso da coluna * valor da coluna

    return sigmoid(z)
    # >>> MUDANÇA 4 (ponto exato): aplica sigmoid sobre z antes de retornar.
    # Antes (Regressão Linear): return resultado
    # Agora (Regressão Logística): return sigmoid(z)


# >>> MUDANÇA 5: calcular_cross_entropy — substitui calcular_mse
# Antes (Regressão Linear):
# def calcular_mse(X, y, pesos):
#     n = len(y)
#     return sum((prever_linear(X[i], pesos) - y[i]) ** 2 for i in range(n)) / n
def calcular_cross_entropy(X, y, pesos):
    # Cross-Entropy (Entropia Cruzada) é a função de perda usada em
    # Regressão Logística no lugar do MSE.
    #
    # Por que não usar MSE aqui?
    # Com sigmoid, o MSE cria uma superfície de erro com vários "vales".
    # O gradiente descendente pode ficar preso nesses vales.
    # A Cross-Entropy com sigmoid tem uma superfície convexa (um único vale),
    # o que garante que o gradiente sempre aponta para o mínimo global.
    #
    # Fórmula:
    # CE = -(1/n) * Σ [ y * log(ŷ) + (1 - y) * log(1 - ŷ) ]
    #
    # Interpretação:
    # - Se y = 1 (sobreviveu) e ŷ ≈ 1: log(1) ≈ 0  → perda pequena ✅
    # - Se y = 1 (sobreviveu) e ŷ ≈ 0: log(0) → -∞ → perda enorme ❌
    # - Se y = 0 (não sobreviveu) e ŷ ≈ 0: log(1) ≈ 0 → perda pequena ✅
    # - Se y = 0 (não sobreviveu) e ŷ ≈ 1: log(0) → -∞ → perda enorme ❌

    n = len(y)
    # Quantidade de exemplos.

    eps = 1e-15
    # Valor mínimo para evitar log(0), que seria infinito.
    # Se ŷ for exatamente 0 ou 1, log quebraria.
    # Então limitamos: ŷ nunca será menor que eps nem maior que 1-eps.

    total = 0.0
    # Acumulador da soma.

    for i in range(n):
        y_hat = prever_logistica(X[i], pesos)
        # Calcula a previsão já com sigmoid aplicado.
        # y_hat estará sempre entre 0 e 1.

        y_hat = max(eps, min(1.0 - eps, y_hat))
        # Limita y_hat para evitar log(0).
        #
        # Exemplo:
        # y_hat = 0.0 → vira 0.000000000000001
        # y_hat = 1.0 → vira 0.999999999999999

        total += y[i] * math.log(y_hat) + (1.0 - y[i]) * math.log(1.0 - y_hat)
        # Acumula o valor da fórmula para este exemplo.
        #
        # Exemplo quando y=1 e y_hat=0.9:
        # 1 * log(0.9) + (1-1) * log(0.1)
        # = log(0.9) + 0
        # ≈ -0.105
        #
        # Exemplo quando y=0 e y_hat=0.1:
        # 0 * log(0.1) + (1-0) * log(0.9)
        # = 0 + log(0.9)
        # ≈ -0.105

    return -total / n
    # Divide pela quantidade de exemplos e inverte o sinal.
    # O sinal negativo transforma os valores negativos do log em positivos,
    # porque queremos minimizar a perda (número positivo).


# =============================================================================
# 4. TREINAMENTO
# =============================================================================
# >>> MUDANÇA 6: dois pontos alterados dentro de treinar()
#
# CURIOSIDADE MATEMÁTICA:
# A fórmula do gradiente é IDÊNTICA à da Regressão Linear!
#
# Regressão Linear  (MSE):         gradiente = (ŷ - y)   onde ŷ = z
# Regressão Logística (Cross-Ent): gradiente = (ŷ - y)   onde ŷ = sigmoid(z)
#
# Isso não é coincidência. A derivada da Cross-Entropy com sigmoid
# se simplifica algebricamente para (ŷ - y), tornando a implementação
# quase idêntica. Só o significado de ŷ muda.
# =============================================================================

def treinar(X, y, taxa, epocas, imprimir_a_cada):
    # Treina o modelo usando Gradiente Descendente.
    #
    # Ideia simples:
    # 1. Faz previsões (agora com sigmoid)
    # 2. Mede o erro (agora com Cross-Entropy)
    # 3. Ajusta os pesos para errar menos
    # 4. Repete muitas vezes

    n = len(y)
    # Número de exemplos.

    n_features = len(X[0])
    # Número de colunas/features.

    pesos = [0.0] * (n_features + 1)
    # Cria os pesos todos zerados.
    #
    # Exemplo se houver 3 features:
    # pesos = [0.0, 0.0, 0.0, 0.0]
    #         bias  w1   w2   w3

    for epoca in range(epocas):
        # Repete por várias épocas.

        grads = [0.0] * (n_features + 1)
        # Lista para acumular os gradientes.

        for i in range(n):
            # Percorre cada exemplo do treino.

            # >>> MUDANÇA 6a (ponto exato): troca prever_linear por prever_logistica
            # Antes (Regressão Linear):
            # erro = prever_linear(X[i], pesos) - y[i]
            erro = prever_logistica(X[i], pesos) - y[i]
            # Calcula o erro da previsão.
            #
            # Exemplo:
            # ŷ = sigmoid(0.58) ≈ 0.641
            # y = 1.0
            # erro = 0.641 - 1.0 = -0.359
            #
            # A fórmula do erro é a MESMA da Regressão Linear.
            # A diferença é que agora ŷ já passou pela sigmoid.

            grads[0] += erro
            # Acumula o gradiente do bias.

            for j in range(n_features):
                grads[j + 1] += erro * X[i][j]
                # Acumula o gradiente do peso j.
                #
                # Exemplo:
                # erro = -0.359
                # x[j] = 0.8
                # contribuição = -0.287

        for j in range(len(pesos)):
            pesos[j] -= taxa * grads[j] / n
            # Atualiza cada peso.
            #
            # Exemplo:
            # peso atual = 0.50
            # gradiente médio = 0.20
            # taxa = 0.1
            # novo peso = 0.50 - 0.1*0.20 = 0.48

        if (epoca + 1) % imprimir_a_cada == 0 or epoca == 0:
            # >>> MUDANÇA 6b (ponto exato): troca calcular_mse por calcular_cross_entropy
            # Antes (Regressão Linear):
            # mse = calcular_mse(X, y, pesos)
            # print(f"  Época {epoca + 1:5d}/{epocas} | MSE = {mse:.6f}")
            ce = calcular_cross_entropy(X, y, pesos)
            print(f"  Época {epoca + 1:5d}/{epocas} | Cross-Entropy = {ce:.6f}")
            # Mostra a perda do modelo durante o treino.
            # Cross-Entropy tende a diminuir ao longo das épocas.

    return pesos
    # Retorna os pesos aprendidos.


# =============================================================================
# 5. AVALIAÇÃO
# =============================================================================
# >>> MUDANÇA 7: dois pontos alterados dentro de avaliar()
#
# Na Regressão Linear, havia um contador de previsões "fora de [0,1]"
# porque a saída podia gerar valores como -0.1 ou 1.3.
#
# Na Regressão Logística isso não existe mais: a sigmoid GARANTE
# que toda previsão esteja dentro de (0, 1).
# Por isso removemos o contador e o aviso de limitação.
# =============================================================================

def avaliar(X, y, pesos, titulo, limiar=0.5):
    # Esta função mede o desempenho do modelo.
    #
    # A saída do sigmoid é um número entre 0 e 1.
    # Usamos um limiar para decidir a classe:
    # se previsão >= 0.5 -> classe 1 (sobreviveu)
    # se previsão < 0.5  -> classe 0 (não sobreviveu)

    n = len(y)

    corretos = 0
    # Número de previsões certas.

    # >>> MUDANÇA 7a (ponto exato): removida a variável "invalidos"
    # Antes (Regressão Linear):
    # corretos = invalidos = 0
    # invalidos contava previsões menores que 0 ou maiores que 1.
    # Agora isso não é necessário: sigmoid sempre produz valores em (0,1).

    vp = vn = fp = fn = 0
    # vp = verdadeiro positivo
    # vn = verdadeiro negativo
    # fp = falso positivo
    # fn = falso negativo

    for i in range(n):
        # >>> MUDANÇA 7b (ponto exato): troca prever_linear por prever_logistica
        # Antes (Regressão Linear):
        # pred = prever_linear(X[i], pesos)
        pred = prever_logistica(X[i], pesos)
        # pred sempre estará entre 0 e 1 graças à sigmoid.

        classe = 1 if pred >= limiar else 0
        # Converte em classe.
        #
        # Exemplo:
        # pred = 0.7 -> classe = 1
        # pred = 0.2 -> classe = 0

        real = int(y[i])
        # Valor correto.

        if classe == real:
            corretos += 1
            # Conta acerto.

        # >>> MUDANÇA 7c (ponto exato): removido o bloco "if pred < 0 or pred > 1"
        # Antes (Regressão Linear):
        # if pred < 0 or pred > 1:
        #     invalidos += 1

        if real == 1 and classe == 1:
            vp += 1
        elif real == 0 and classe == 0:
            vn += 1
        elif real == 0 and classe == 1:
            fp += 1
        else:
            fn += 1
        # Atualiza a matriz de confusão.

    acuracia = corretos / n * 100
    # Percentual de acertos.

    # >>> MUDANÇA 7d (ponto exato): removidas as linhas de aviso de limitação
    # Antes (Regressão Linear):
    # pct_inv = invalidos / n * 100
    # print(f"  Previsões fora de [0,1]: {invalidos} ({pct_inv:.1f}%)")
    # print(f"  ⚠️  Esses {invalidos} casos ilustram a limitação da Regressão Linear.")

    print(f"\n  {'─'*56}")
    print(f"  {titulo}")
    print(f"  {'─'*56}")
    print(f"  Passageiros avaliados : {n}")
    print(f"  Acurácia (limiar 0.5) : {acuracia:.2f}%")
    print(f"  ✅ Sigmoid garante que todas as saídas estão entre 0 e 1.")
    print(f"\n  Matriz de Confusão:")
    print(f"               Previsto 0   Previsto 1")
    print(f"  Real 0          {vn:5d}        {fp:5d}    (não sobreviveu)")
    print(f"  Real 1          {fn:5d}        {vp:5d}    (sobreviveu)")
    print(f"  {'─'*56}")

    return acuracia


# =============================================================================
# 6. EXIBIR PESOS
# =============================================================================
# >>> MUDANÇA 8: fórmula exibida mostra a sigmoid

def exibir_pesos(pesos, nomes):
    # Mostra os pesos aprendidos pelo modelo.

    print("\n" + "="*62)
    print("  PESOS DO MODELO — para cálculo manual")
    print("="*62)
    print(f"  {'Atributo':<24} {'Peso':>12}  Interpretação")
    print("-"*62)

    print(f"  {'w0  (bias)':<24} {pesos[0]:>12.6f}")
    # Mostra o bias.

    for i, nome in enumerate(nomes):
        # enumerate dá:
        # i = índice
        # nome = valor da lista

        direcao = "↑ favorece sobrevivência" if pesos[i+1] > 0 else "↓ reduz sobrevivência"
        # Se o peso for positivo, aumenta z, logo sigmoid(z) sobe.
        # Se for negativo, diminui z, logo sigmoid(z) desce.

        print(f"  {'w'+str(i+1)+'  ('+nome+')':<24} {pesos[i+1]:>12.6f}  {direcao}")

    print("="*62)

    # >>> MUDANÇA 8 (ponto exato): fórmula agora mostra z separado de sigmoid(z)
    # Antes (Regressão Linear):
    # print(f"  FÓRMULA COMPLETA:")
    # print(f"  ŷ = {pesos[0]:.6f}")
    # for i, nome in enumerate(nomes):
    #     sinal = "+" if pesos[i+1] >= 0 else "-"
    #     print(f"    {sinal} {abs(pesos[i+1]):.6f} × {nome}  (normalizado)")
    # print()
    # print("  NOTA: ... modelo_pesos.json.")

    print("\n  FÓRMULA COMPLETA:")
    print(f"  z  = {pesos[0]:.6f}")
    # Mostra o início da combinação linear (igual antes).

    for i, nome in enumerate(nomes):
        sinal = "+" if pesos[i+1] >= 0 else "-"
        print(f"    {sinal} {abs(pesos[i+1]):.6f} × {nome}  (normalizado)")
        # Exemplo:
        # + 0.123456 × sex
        # - 0.654321 × age

    print(f"  ŷ  = sigmoid(z) = 1 / (1 + e^-z)")
    # Nova linha: mostra que a saída final passa pela sigmoid.

    print()
    print("  NOTA: as features devem estar normalizadas (Min-Max) antes de")
    print("  substituir na fórmula. Os parâmetros estão em modelo_pesos_logistica.json.")
    print("="*62)


# =============================================================================
# 7. SALVAR MODELO
# =============================================================================
# >>> MUDANÇA 9: campo "tipo" alterado

def salvar_modelo(pesos, mins, maxs, nomes, med_age, med_fare, caminho):
    # Salva as informações do modelo em JSON.

    modelo = {
        # >>> MUDANÇA 9 (ponto exato): tipo alterado de "regressao_linear" para "regressao_logistica"
        # Antes (Regressão Linear):
        # "tipo": "regressao_linear",
        "tipo": "regressao_logistica",

        "nomes_features": nomes,
        "pesos": pesos,
        "normalizacao": {"mins": mins, "maxs": maxs},
        "imputacao": {"mediana_age": med_age, "mediana_fare": med_fare}
    }
    # Cria um dicionário com tudo que será salvo.

    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(modelo, f, indent=2, ensure_ascii=False)
        # Salva o dicionário no arquivo JSON.

    print(f"\n  ✅ Modelo salvo em: {caminho}")


# =============================================================================
# 8. FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    # "main" é a função principal.
    # Ela organiza a execução do programa.

    print("\n" + "="*62)
    print("  TITANIC — REGRESSÃO LOGÍSTICA (Implementação Manual)")
    print("="*62)

    nomes = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
    # Lista com os nomes das colunas usadas como entrada.

    for arq in [ARQUIVO_TREINO, ARQUIVO_TESTE, ARQUIVO_GABARITO]:
        if not os.path.exists(arq):
            print(f"\n  ❌ Arquivo '{arq}' não encontrado!")
            print("  📥 Baixe em: https://www.kaggle.com/c/titanic/data")
            return
    # Verifica se os arquivos necessários existem.

    print(f"\n  📂 Carregando '{ARQUIVO_TREINO}'...")
    X_tr, y_tr, med_age, med_fare = carregar_treino(ARQUIVO_TREINO)
    print(f"  ✅ {len(y_tr)} registros de treino.")
    # Carrega os dados de treino.

    print(f"\n  📂 Carregando '{ARQUIVO_TESTE}' + '{ARQUIVO_GABARITO}'...")
    X_te, y_te, ids = carregar_teste(ARQUIVO_TESTE, ARQUIVO_GABARITO, med_age, med_fare)
    print(f"  ✅ {len(y_te)} registros de teste com gabarito real.")
    # Carrega os dados de teste e o gabarito.

    print("\n  📐 Normalizando (Min-Max, referência = treino)...")
    mins, maxs = calcular_params_normalizacao(X_tr)
    # Calcula min e max usando treino.

    X_tr_norm = normalizar(X_tr, mins, maxs)
    # Normaliza os dados de treino.

    X_te_norm = normalizar(X_te, mins, maxs)
    # Normaliza os dados de teste com os mesmos parâmetros.

    print(f"\n  🏋️  Treinando por {EPOCAS} épocas (η={TAXA_APRENDIZADO})...")
    print("-"*62)
    pesos = treinar(X_tr_norm, y_tr, TAXA_APRENDIZADO, EPOCAS, IMPRIMIR_A_CADA)
    # Treina o modelo.

    ac_tr = avaliar(X_tr_norm, y_tr, pesos, "TREINO  — train.csv")
    # Mede desempenho no treino.

    ac_te = avaliar(X_te_norm, y_te, pesos, "TESTE   — test.csv  (gabarito: gender_submission.csv)")
    # Mede desempenho no teste.

    print(f"\n  📊 Resumo:")
    print(f"     Acurácia no TREINO : {ac_tr:.2f}%")
    print(f"     Acurácia no TESTE  : {ac_te:.2f}%")

    dif = ac_tr - ac_te
    # Diferença entre treino e teste.

    if dif > 5:
        print(f"     ⚠️  Diferença de {dif:.1f}% → possível overfitting.")
    else:
        print(f"     ✅ Diferença de {dif:.1f}% → modelo generalizando bem.")
    # Se treino estiver muito melhor que teste, pode ser overfitting.

    exibir_pesos(pesos, nomes)
    # Mostra os pesos.

    salvar_modelo(pesos, mins, maxs, nomes, med_age, med_fare, ARQUIVO_PESOS)
    # Salva o modelo.

    print("\n  ▶️  Execute titanic_prever_logistica.py para prever passageiros individuais.\n")


# =============================================================================
# INÍCIO DO PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Esta condição verifica se o arquivo foi executado diretamente.
    # Se foi, chama a função principal.

    main()
