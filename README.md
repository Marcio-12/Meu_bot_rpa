# Bot de Automação RPA (Python + MySQL)

Sistema de automação para consumo de dados via API REST, filtragem baseada em regras de negócio, persistência em banco de dados relacional (MySQL) para controle de duplicidade e envio de notificações.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Requests** (Consumo de APIs REST)
* **SQLite3** (Persistência de dados local)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente)

## 📁 Estrutura do Projeto

```text
Meu_bot_rpa/
├── src/
│   ├── database.py   # Gerenciamento e conexão com o banco SQLite
│   ├── notifier.py   # Módulo de envio de alertas e notificações
│   └── services.py   # Consumo da API REST e filtros de negócio
├── .gitignore        # Arquivos ignorados pelo Git
├── main.py           # Script principal (Orquestrador)
└── requirements.txt  # Dependências do projeto


🛠️ Como Executar o Projeto

Clone o repositório:

1- Clone o repositório:
Bash
git clone <URL_DO_SEU_REPOSITORIO>
cd Meu_bot_rpa

2-Crie e ative o ambiente virtual:

PowerShell
python -m venv .venv
.\.venv\Scripts\activate

3-Instale as dependências:

Bash
pip install -r requirements.txt

4-Execute o robô:

Bash
python main.py