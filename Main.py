import math
import matplotlib.pyplot as plt


def obter_entrada_valida():
    """Lê e valida os dados fornecidos pelo usuário."""
    while True:
        try:
            v0 = float(input("Digite a velocidade inicial (m/s) [deve ser > 0]: "))
            if v0 > 0:
                break
            print("Erro: A velocidade inicial deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número válido.")

    while True:
        try:
            angulo = float(input("Digite o ângulo de lançamento (em graus) [entre 0 e 90]: "))
            if 0 <= angulo <= 90:
                break
            print("Erro: O ângulo deve estar entre 0° e 90°.")
        except ValueError:
            print("Erro: Digite um número válido.")

    return v0, angulo


def simular_e_plotar_lancamento(v0, angulo_graus, gravidade=9.81, dt=0.01):
    """Simula a trajetória, exibe resumo e plota o gráfico do lançamento."""
    angulo_rad = math.radians(angulo_graus)

    # Decomposição da velocidade
    v_x = v0 * math.cos(angulo_rad)
    v_y = v0 * math.sin(angulo_rad)

    # Altura máxima teórica
    altura_max_teorica = math.pow(v_y, 2) / (2 * gravidade)

    t = 0.0
    x = 0.0
    y = 0.0

    # Listas para armazenar as coordenadas de cada instante
    posicoes_x = []
    posicoes_y = []

    # Laço de repetição armazenando as posições no tempo
    while y >= 0:
        posicoes_x.append(x)
        posicoes_y.append(y)

        t += dt
        x = v_x * t
        y = (v_y * t) - (0.5 * gravidade * math.pow(t, 2))

    # Garante que o último ponto atinja o solo exatamente em y = 0
    if len(posicoes_y) > 0 and posicoes_y[-1] != 0:
        posicoes_x.append(x)
        posicoes_y.append(0.0)

    # Exibe resumo numérico no terminal
    print("\n" + "=" * 50)
    print("📊 RESUMO DO LANÇAMENTO:")
    print(f" • Alcance Horizontal Final: {posicoes_x[-1]:.2f} metros")
    print(f" • Tempo Total de Voo:       {t:.2f} segundos")
    print(f" • Altura Máxima Teórica:    {altura_max_teorica:.2f} metros")
    print("=" * 50)

    # --- CONSTRUÇÃO DO GRÁFICO ---
    plt.figure(figsize=(9, 5))

    # Plota a linha da trajetória parabólica
    plt.plot(posicoes_x, posicoes_y, color="#2b5c8f", linewidth=2.5, label="Trajetória do Projétil")

    # Marca o ponto de altura máxima no gráfico
    x_alt_max = posicoes_x[posicoes_y.index(max(posicoes_y))]
    plt.scatter(x_alt_max, max(posicoes_y), color="red", zorder=5, label=f"Alt. Máx: {altura_max_teorica:.2f}m")

    # Configurações de estilo e títulos
    plt.title(f"Trajetória Parabólica (v0 = {v0} m/s, θ = {angulo_graus}°)", fontsize=13, fontweight='bold')
    plt.xlabel("Distância Horizontal (m)", fontsize=11)
    plt.ylabel("Altura (m)", fontsize=11)
    plt.ylim(bottom=0)  # Garante que o eixo Y comece no chão (0)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Exibe a janela com o gráfico
    plt.show()


if __name__ == "__main__":
    v_inicial, angulo = obter_entrada_valida()
    simular_e_plotar_lancamento(v_inicial, angulo)