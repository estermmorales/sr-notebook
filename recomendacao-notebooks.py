import json

with open("notebooks.json", "r") as arquivo_json:
    notebooks = json.load(arquivo_json)

perguntas = {
    "preco": "Qual é o seu orçamento máximo?",
    "placa_de_video": "Você precisa de uma placa de vídeo dedicada? (Sim ou Não)",
    "tamanho": "Qual tamanho de tela você prefere? (compacto, médio, grande ou sem preferência)",
    "marca": "Tem preferência por uma marca específica? (Digite o nome da marca ou 'sem preferência')",
    "capacidade_disco": "De quanto espaço de armazenamento você precisa (em GB)?",
    "uso": "Para que você pretende usar o notebook? (edição de vídeo, edição de foto, arquivo de áudio, jogos ou nenhuma das opções)"
}

pesos = {
    "preco": 0.3,
    "placa_de_video": 0.15,
    "tamanho": 0.1,
    "marca": 0.2,
    "capacidade_disco": 0.15,
    "uso": 0.1
}
