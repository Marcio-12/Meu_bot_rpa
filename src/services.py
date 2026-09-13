import requests # type: ignore

def buscar_pendencias():
    """
    Simula a busca de registros/tarefas pendentes em uma API.
    Retorna uma lista de dicionários com os dados.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  # Dispara erro se o status HTTP for 4xx ou 5xx
        
        dados = resposta.json()
        
        # Regra de Negócio: Filtrar apenas tarefas não concluídas (completed == False) do usuário 1
        pendencias = [item for item in dados if item['userId'] == 1 and not item['completed']]
        
        return pendencias

    except requests.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
        return []

