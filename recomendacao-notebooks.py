import json

with open("notebooks.json", "r") as arquivo_json:
    notebooks = json.load(arquivo_json)

pesos = {
    "preco": 0.3,
    "placa_de_video": 0.15,
    "tamanho": 0.1,
    "marca": 0.2,
    "capacidade_disco": 0.15,
    "uso": 0.1
}

# Função para calcular a pontuação percentual de um notebook com base nas respostas do usuário


def calcular_pontuacao_percentual(notebook, respostas_usuario, pesos):
    pontuacao_total = 0
    peso_total = 0
    # Obtém a marca escolhida pelo usuário
    marca_usuario = respostas_usuario.get("marca", None)

    if marca_usuario and marca_usuario != "Sem preferência":
        # Se o usuário escolheu uma marca específica, verifica se a marca do notebook corresponde
        if "marca" in notebook and notebook["marca"] != marca_usuario:
            return 0

    for pergunta, resposta in respostas_usuario.items():
        if resposta is None or resposta == "Sem preferência":
            continue

        if pergunta in notebook:
            if isinstance(resposta, list):
                if any(valor in resposta for valor in notebook[pergunta]):
                    if notebook[pergunta] != None:
                        pontuacao_total += pesos[pergunta]
                        peso_total += pesos[pergunta]
            else:
                if resposta == notebook[pergunta]:
                    pontuacao_total += pesos[pergunta]
                    peso_total += pesos[pergunta]

    if peso_total == 0:
        return 0

    # Verifica se o preço está dentro da faixa do usuário
    if "preco" in respostas_usuario:
        preco_maximo = respostas_usuario["preco"]
        if "preco" in notebook and notebook["preco"] <= preco_maximo:
            # Ajuste para dar maior porcentagem para preços menores
            pontuacao_total += (1 -
                                (notebook["preco"] / preco_maximo)) * pesos["preco"]

    # Classifica o tamanho do notebook
    if "tamanho" in notebook:
        tamanho = notebook["tamanho"]
        if tamanho <= 15.6:
            tamanho_classificado = "compacto"
        elif 15.7 <= tamanho <= 16.9:
            tamanho_classificado = "médio"
        else:
            tamanho_classificado = "grande"

        if "tamanho" in respostas_usuario and respostas_usuario["tamanho"] == tamanho_classificado:
            pontuacao_total += pesos["tamanho"]

    pontuacao_percentual = (pontuacao_total / sum(pesos.values())) * 100

    return pontuacao_percentual


# Perguntas para o usuário
print("Bem-vindo ao sistema de recomendação de notebooks!")
respostas_usuario = {}
respostas_usuario["preco"] = float(input("Qual é o seu orçamento máximo? "))
placa_de_video = input(
    "Você precisa de uma placa de vídeo dedicada? (Sim ou Não): ")
tamanho = input(
    "Qual tamanho de tela você prefere? (compacto, médio ou grande): ")
respostas_usuario["tamanho"] = tamanho
marca = input(
    "Tem preferência por uma marca específica? (Digite o nome da marca ou 'Sem preferência'): ")
respostas_usuario["marca"] = marca
respostas_usuario["capacidade_disco"] = int(
    input("De quanto espaço de armazenamento você precisa (em GB)? "))
usos = input(
    "Para que você pretende usar o notebook? (edição de vídeo, edição de foto, edição de arquivo de áudio, jogos ou nenhuma das opções): ")
if usos.lower() != "nenhuma das opções":
    respostas_usuario["uso"] = usos.split(", ")

# Calcula a pontuação percentual para cada notebook
notebooks_classificados = []

for notebook in notebooks:
    pontuacao_percentual = calcular_pontuacao_percentual(
        notebook, respostas_usuario, pesos)
    if pontuacao_percentual > 0:
        notebook["pontuacao_percentual"] = pontuacao_percentual
        notebooks_classificados.append(notebook)

# Exibe os notebooks classificados ao usuário
if notebooks_classificados:
    notebooks_classificados = sorted(
        notebooks_classificados, key=lambda x: x["pontuacao_percentual"], reverse=True)
    print("\nRecomendação de Notebooks:")
    for notebook in notebooks_classificados:
        print(
            f"Modelo: {notebook['modelo']}, Marca: {notebook['marca']}, Pontuação: {int(notebook['pontuacao_percentual'])}%")
else:
    print("Desculpe, não encontramos nenhum notebook que corresponda às suas preferências.")
