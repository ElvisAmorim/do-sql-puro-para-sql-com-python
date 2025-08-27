# Do SQL puro para SQL com Python

Este repositório mostra como sair do SQL puro e começar a utilizar **Python** para rodar consultas em bancos Oracle (e outros bancos SQL), aproveitando a flexibilidade da linguagem para organizar filtros, automatizar execuções e gerar arquivos.

A ideia é simples: centralizar a conexão com o banco em um único arquivo (`src/conexao_bd.py`) e utilizar notebooks para análises do dia a dia.

## 🚀 Estrutura do Projeto

|- notebooks  
|-- consulta-dia-dia.ipynb # Notebook de exemplo para rodar consultas  
|- src  
|-- conexao_bd.py # Script central de conexão ao banco  
|- .env # Variáveis de ambiente (credenciais do banco)  
|- requirements.txt # Lista de dependências do projeto

## 🔧 Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/ElvisAmorim/do-sql-puro-para-sql-com-python.git
   cd do-sql-puro-para-sql-com-python

2. Crie e ative um ambiente virtual:
    
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows
    ```
    
3. Instale as dependências:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. Configure o arquivo `.env` com suas credenciais de banco:
    
    ```ini
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_HOST=seu_host
    DB_PORT=porta_do_banco
    DB_SERVICE=seu_service
    ```

## ▶️ Como Usar

* Abra o notebook de exemplo:

  *  jupyter notebook notebooks/consulta-dia-dia.ipynb
    
* Edite os trechos de SQL conforme sua necessidade.
    
* Utilize variáveis do Python para passar listas, filtros e parâmetros sem precisar alterar a query manualmente.
    

## 📌 Boas Práticas

* **Não versionar credenciais:** o arquivo `.env` deve permanecer fora do controle de versão.
    
* **Separação de responsabilidades:** use notebooks apenas para análises, deixando conexões e funções auxiliares em `src/`.
    
* **Reaproveitamento:** crie funções genéricas no `conexao_bd.py` e apenas importe quando precisar.
    
## 🤝 Contribuição

Fique à vontade para abrir _issues_ ou enviar _pull requests_.  
Sugestões e melhorias são sempre bem-vindas! 🚀


## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
