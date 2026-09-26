# Simulador de Lançamento de Projéteis em Python

Projeto desenvolvido para a disciplina de programação com o objetivo de praticar conceitos de estruturas de repetição, lógica matemática e visualização de dados em Python.

O programa simula o movimento parabólico de um objeto lançado no vácuo a partir de uma velocidade inicial e de um ângulo informados pelo usuário.

## O que o projeto faz

- Solicita a velocidade inicial e o ângulo de lançamento com validação de dados para evitar entradas inválidas.
- Calcula a posição x e y a cada fração de tempo utilizando a biblioteca nativa `math`.
- Exibe o tempo total de voo, o alcance horizontal e a altura máxima atingida.
- Plota o gráfico da trajetória utilizando `matplotlib` e destaca o ponto mais alto da curva.

## Tecnologias e Bibliotecas

- Python 3
- `math` (padrão da linguagem)
- `matplotlib` (para gerar o gráfico)

## Como executar

1. Instale a biblioteca necessária:
```bash
pip install matplotlib