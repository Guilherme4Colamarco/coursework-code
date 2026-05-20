# =============================================================================
# TITANIC - PREVISÃO INDIVIDUAL COM MODELO LOGÍSTICO TREINADO
# =============================================================================
# PRÉ-REQUISITO: execute titanic_treino_logistica_comentado.py primeiro
#                (gera modelo_pesos_logistica.json)
#
# COMO USAR:
#   1. Edite a variável PASSAGEIRO abaixo com os dados da pessoa
#   2. Execute: python titanic_prever_logistica.py
#
# FORMATO DO ARRAY:
#   [pclass, sex, age, sibsp, parch, fare, embarked]
#
#   pclass   → Classe do bilhete : 1=Primeira, 2=Segunda, 3=Terceira
#   sex      → Sexo              : 0=Masculino, 1=Feminino
#   age      → Idade em anos     : ex. 25.0
#   sibsp    → Irmãos/cônjuge    : ex. 1
#   parch    → Pais/filhos       : ex. 0
#   fare     → Tarifa (libras)   : ex. 7.25
#   embarked → Porto             : 0=Cherbourg, 1=Queenstown, 2=Southampton
#
# SUGESTÕES PARA TESTAR (do filme):
#   Rose  → [1, 1, 17, 1, 1, 100.0, 0]   (1ª classe, feminino, jovem, cara)
#   Jack  → [3, 0, 20,  0, 0,   7.25, 2]  (3ª classe, masculino, barato)
# =============================================================================

import json
import math
import os

# =============================================================================
# ▼▼▼  EDITE AQUI OS DADOS DO PASSAGEIRO  ▼▼▼
# =============================================================================

PASSAGEIRO = [3, 0, 20, 0, 0, 7.25, 2]   # [pclass, sex, age, sibsp, parch, fare, embarked]

# =============================================================================
# ▲▲▲  FIM DA EDIÇÃO  ▲▲▲
# =============================================================================

ARQUIVO_PESOS = "modelo_pesos_logistica.json"

# =============================================================================
# PARÂMETROS USADOS NO TREINO (apenas para referência didática)
#   η (taxa aprendizado) : 0.1
#   Épocas               : 5000
#   Loss                 : Binary Cross-Entropy
# =============================================================================


# =============================================================================
# FUNÇÕES
# =============================================================================

def carregar_modelo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)


def normalizar_passageiro(x, mins, maxs):
    """
    Aplica exatamente a mesma normalização Min-Max do treinamento.
    IMPORTANTE: sempre usar os mins/maxs salvos no modelo_pesos_logistica.json.
    """
    x_norm = []
    for j in range(len(x)):
        intervalo = maxs[j] - mins[j]
        x_norm.append((x[j] - mins[j]) / intervalo if intervalo != 0 else 0.0)
    return x_norm


def sigmoid(z):
    """
    σ(z) = 1 / (1 + e^-z)

    Transforma qualquer número real em um valor entre 0 e 1.
    Usamos duas formas equivalentes para evitar overflow numérico.
    """
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    else:
        e = math.exp(z)
        return e / (1.0 + e)


def prever_logistica(x_norm, pesos):
    """
    z  = w0 + w1*x1 + ... + wn*xn   (combinação linear)
    ŷ  = sigmoid(z)                   (ativa com sigmoid)
    """
    z = pesos[0]
    for j in range(len(x_norm)):
        z += pesos[j + 1] * x_norm[j]
    return sigmoid(z)


def mostrar_calculo_detalhado(x_raw, x_norm, pesos, nomes, mins, maxs):
    """
    Exibe o cálculo passo a passo para o aluno acompanhar com papel e caneta.
    """
    print("\n" + "="*68)
    print("  CÁLCULO DETALHADO (passo a passo)")
    print("="*68)

    # Passo 1: normalização
    print("\n  PASSO 1 — Normalização Min-Max de cada atributo:")
    print(f"  {'Atributo':<14} {'Original':>10} {'Min':>8} {'Max':>8}  Fórmula → {'Normalizado':>11}")
    print("-"*68)
    for j, nome in enumerate(nomes):
        intervalo = maxs[j] - mins[j]
        norma = (x_raw[j] - mins[j]) / intervalo if intervalo != 0 else 0.0
        formula = f"({x_raw[j]:.2f}-{mins[j]:.2f})/{intervalo:.2f}"
        print(f"  {nome:<14} {x_raw[j]:>10.4f} {mins[j]:>8.4f} {maxs[j]:>8.4f}  {formula:<18} {norma:>11.6f}")

    # Passo 2: produto peso × valor e soma → z
    print(f"\n  PASSO 2 — Multiplicação peso × valor normalizado (soma = z):")
    print(f"  {'Atributo':<14} {'Peso (w)':>12} {'x norm':>10}  {'w × x':>12}")
    print("-"*68)
    z = pesos[0]
    print(f"  {'bias (w0)':<14} {pesos[0]:>12.6f} {'—':>10}  {pesos[0]:>12.6f}  (bias)")
    for j, nome in enumerate(nomes):
        contrib = pesos[j + 1] * x_norm[j]
        z += contrib
        print(f"  {nome:<14} {pesos[j+1]:>12.6f} {x_norm[j]:>10.6f}  {contrib:>12.6f}")
    print("-"*68)
    print(f"  {'SOMA (z)':<14} {'':>12} {'':>10}  {z:>12.6f}")

    # Passo 3: sigmoid
    y_hat = sigmoid(z)
    print(f"\n  PASSO 3 — Aplicar Sigmoid sobre z:")
    print(f"")
    print(f"         1                    1")
    print(f"  σ = ─────────  =  ─────────────────  =  {y_hat:.6f}  ({y_hat*100:.2f}%)")
    print(f"      1 + e^(-{z:.4f})     1 + {math.exp(-z) if z >= 0 else 1/math.exp(z):.4f}")
    print(f"")
    print("="*68)


def mostrar_resultado(pred):
    """
    Interpreta o resultado da Regressão Logística.
    A sigmoid garante que pred sempre estará entre 0 e 1.
    """
    pct = pred * 100

    print("\n" + "="*68)
    print("  RESULTADO")
    print("="*68)
    print(f"\n  Probabilidade de sobrevivência (ŷ) : {pred:.6f}  ({pct:.2f}%)")
    print(f"  ✅ Valor sempre entre 0 e 1 graças à função Sigmoid.")

    if pred >= 0.5:
        decisao = "Sobreviveria"
        barra = "█" * int(pct / 5)
        restante = "░" * (20 - int(pct / 5))
    else:
        decisao = "NÃO sobreviveria"
        barra = "█" * int(pct / 5)
        restante = "░" * (20 - int(pct / 5))

    print(f"\n  Probabilidade : [{barra}{restante}] {pct:.1f}%")
    print(f"  🎯 Decisão (limiar = 0.5) : {decisao}")
    print("="*68)


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def main():
    print("\n" + "="*68)
    print("  TITANIC — PREVISÃO INDIVIDUAL (Regressão Logística)")
    print("="*68)

    if not os.path.exists(ARQUIVO_PESOS):
        print(f"\n  ❌ '{ARQUIVO_PESOS}' não encontrado.")
        print("  ▶️  Execute primeiro: python titanic_treino_logistica_comentado.py\n")
        return

    modelo = carregar_modelo(ARQUIVO_PESOS)
    pesos  = modelo['pesos']
    mins   = modelo['normalizacao']['mins']
    maxs   = modelo['normalizacao']['maxs']
    nomes  = modelo['nomes_features']

    if len(PASSAGEIRO) != len(nomes):
        print(f"\n  ❌ PASSAGEIRO tem {len(PASSAGEIRO)} valores; esperado {len(nomes)}.")
        print(f"     Formato: {nomes}\n")
        return

    # Exibir dados
    legivel = {
        'pclass': 'Classe (1/2/3)', 'sex': 'Sexo (0=M, 1=F)',
        'age': 'Idade', 'sibsp': 'Irmãos/Cônjuge',
        'parch': 'Pais/Filhos', 'fare': 'Tarifa (£)',
        'embarked': 'Embarque (0=C,1=Q,2=S)'
    }
    print("\n  DADOS DO PASSAGEIRO:")
    for i, nome in enumerate(nomes):
        print(f"    {legivel.get(nome, nome):<24}: {PASSAGEIRO[i]}")

    # Calcular e exibir
    x_norm = normalizar_passageiro(PASSAGEIRO, mins, maxs)
    mostrar_calculo_detalhado(PASSAGEIRO, x_norm, pesos, nomes, mins, maxs)

    pred = prever_logistica(x_norm, pesos)
    mostrar_resultado(pred)

    print("\n  Dica: altere PASSAGEIRO no topo do arquivo e execute de novo!\n")


if __name__ == "__main__":
    main()
