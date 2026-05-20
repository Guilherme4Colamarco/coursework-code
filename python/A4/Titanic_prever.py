# =============================================================================
# TITANIC - PREVISÃO INDIVIDUAL COM MODELO TREINADO
# =============================================================================
# PRÉ-REQUISITO: execute titanic_treino.py primeiro (gera modelo_pesos.json)
#
# COMO USAR:
#   1. Edite a variável PASSAGEIRO abaixo com os dados da pessoa
#   2. Execute: python titanic_prever.py
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
import os

# =============================================================================
# ▼▼▼  EDITE AQUI OS DADOS DO PASSAGEIRO  ▼▼▼
# =============================================================================

PASSAGEIRO = [3, 0, 20, 0, 0, 7.25, 2]   # [pclass, sex, age, sibsp, parch, fare, embarked]

# =============================================================================
# ▲▲▲  FIM DA EDIÇÃO  ▲▲▲
# =============================================================================

ARQUIVO_PESOS = "modelo_pesos.json"

# =============================================================================
# PARÂMETROS USADOS NO TREINO (apenas para referência didática)
#   η (taxa aprendizado) : 0.1
#   Épocas               : 5000
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
    IMPORTANTE: sempre usar os mins/maxs salvos no modelo_pesos.json.
    """
    x_norm = []
    for j in range(len(x)):
        intervalo = maxs[j] - mins[j]
        x_norm.append((x[j] - mins[j]) / intervalo if intervalo != 0 else 0.0)
    return x_norm


def prever_linear(x_norm, pesos):
    """
    ŷ = w0 + w1*x1 + ... + wn*xn
    """
    resultado = pesos[0]
    for j in range(len(x_norm)):
        resultado += pesos[j + 1] * x_norm[j]
    return resultado


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

    # Passo 2: produto peso × valor
    print(f"\n  PASSO 2 — Multiplicação peso × valor normalizado:")
    print(f"  {'Atributo':<14} {'Peso (w)':>12} {'x norm':>10}  {'w × x':>12}")
    print("-"*68)
    acumulado = pesos[0]
    print(f"  {'bias (w0)':<14} {pesos[0]:>12.6f} {'—':>10}  {pesos[0]:>12.6f}  (bias)")
    for j, nome in enumerate(nomes):
        contrib = pesos[j + 1] * x_norm[j]
        acumulado += contrib
        print(f"  {nome:<14} {pesos[j+1]:>12.6f} {x_norm[j]:>10.6f}  {contrib:>12.6f}")

    # Passo 3: soma
    print("-"*68)
    print(f"  {'SOMA (ŷ)':<14} {'':>12} {'':>10}  {acumulado:>12.6f}")
    print("="*68)


def mostrar_resultado(pred, nomes, pesos, x_norm):
    """
    Interpreta o resultado e mostra os alertas pedagógicos sobre
    as limitações da Regressão Linear.
    """
    pct = pred * 100

    print("\n" + "="*68)
    print("  RESULTADO")
    print("="*68)
    print(f"\n  Valor bruto do modelo (ŷ) : {pred:.6f}")
    print(f"  Em percentual             : {pct:.2f}%")

    # Alertas para valores fora de [0,1]
    print()
    if pred < 0:
        print(f"  ⚠️  RESULTADO NEGATIVO ({pct:.2f}%)!")
        print("      Probabilidade negativa não existe na matemática.")
        print("      Isso ocorre porque a Regressão Linear não tem restrição")
        print("      de saída — a reta pode assumir qualquer valor real.")
        decisao = "NÃO sobreviveria  (classificado como 0)"
    elif pred > 1:
        print(f"  ⚠️  RESULTADO MAIOR QUE 100% ({pct:.2f}%)!")
        print("      Probabilidade acima de 1 não existe na matemática.")
        print("      Mesma razão: a Regressão Linear não está restrita a [0,1].")
        decisao = "Sobreviveria  (classificado como 1)"
    else:
        print(f"  ✅ Resultado dentro do intervalo [0,1]: {pct:.2f}%")
        decisao = "Sobreviveria  (≥ 50%)" if pred >= 0.5 else "NÃO sobreviveria  (< 50%)"

    print(f"\n  🎯 Decisão (limiar = 0.5) : {decisao}")

    print("="*68)


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def main():
    print("\n" + "="*68)
    print("  TITANIC — PREVISÃO INDIVIDUAL")
    print("="*68)

    if not os.path.exists(ARQUIVO_PESOS):
        print(f"\n  ❌ '{ARQUIVO_PESOS}' não encontrado.")
        print("  ▶️  Execute primeiro: python titanic_treino.py\n")
        return

    modelo  = carregar_modelo(ARQUIVO_PESOS)
    pesos   = modelo['pesos']
    mins    = modelo['normalizacao']['mins']
    maxs    = modelo['normalizacao']['maxs']
    nomes   = modelo['nomes_features']

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

    # Calcular
    x_norm = normalizar_passageiro(PASSAGEIRO, mins, maxs)
    mostrar_calculo_detalhado(PASSAGEIRO, x_norm, pesos, nomes, mins, maxs)

    pred = prever_linear(x_norm, pesos)
    mostrar_resultado(pred, nomes, pesos, x_norm)

    print("\n  Dica: altere PASSAGEIRO no topo do arquivo e execute de novo!\n")


if __name__ == "__main__":
    main()
