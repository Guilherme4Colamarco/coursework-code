from pathlib import Path

import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression


# Usa backend não interativo para permitir execução no terminal.
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def main():
    # Base de dados do enunciado.
    x = np.array([1, 2, 3, 4, 5], dtype=float).reshape(-1, 1)
    y = np.array([2, 4, 5, 4, 5], dtype=float)

    modelo = LinearRegression()
    modelo.fit(x, y)

    predicoes = modelo.predict(x)
    previsao_6 = float(modelo.predict(np.array([[6.0]]))[0])

    coeficiente = float(modelo.coef_[0])
    intercepto = float(modelo.intercept_)
    mse = float(np.mean((y - predicoes) ** 2))
    r2 = float(modelo.score(x, y))

    print("=== Regressao Linear ===")
    print(f"Equacao ajustada: y = {intercepto:.4f} + {coeficiente:.4f}x")
    print(f"Previsao para investimento 6: {previsao_6:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")
    print()
    print("Comparacao entre dados reais e previstos:")
    for xi, yi, yhat in zip(x.ravel(), y, predicoes):
        erro = yi - yhat
        print(f"X={xi:.0f} | real={yi:.1f} | previsto={yhat:.4f} | erro={erro:+.4f}")

    # Gera o grafico com os pontos observados e a reta ajustada.
    x_linha = np.linspace(x.min(), 6, 100).reshape(-1, 1)
    y_linha = modelo.predict(x_linha)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="#0f766e", s=70, label="Dados reais")
    plt.plot(x_linha, y_linha, color="#b45309", linewidth=2.5, label="Reta de regressao")
    plt.scatter([6], [previsao_6], color="#111827", marker="x", s=90, label="Previsao para X=6")
    plt.title("Regressao Linear - Investimento em publicidade x Vendas")
    plt.xlabel("Investimento em publicidade")
    plt.ylabel("Vendas")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()

    saida = Path(__file__).with_name("grafico_regressao.png")
    plt.savefig(saida, dpi=160)
    plt.close()

    print()
    print(f"Grafico salvo em: {saida}")
    print()
    print("Interpretacao:")
    print("- O modelo captura a tendencia geral de crescimento, mas nao ajusta perfeitamente todos os pontos.")
    print("- Se o investimento aumentar, a previsao sobe de forma linear, dentro do comportamento observado.")
    print("- Como a base de dados e pequena, o modelo serve bem como exemplo, mas e fraco para decisoes reais sem mais dados.")


if __name__ == "__main__":
    main()
