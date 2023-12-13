## 1 - Titanic Survivors
MVP apresentado à disciplina de Qualidade de Software, Segurança e Sistemas Inteligentes, do curso de Engenharia de Software da PUC-Rio, e que teve por objetivo realizar o treinamento de um modelo de machine learn, utilizando o dataset Titanic, para um problema de classificação.

## 2 - Tecnologias utilizadas

- - Framework e Extensões Flask:
Flask, Flask-Cors, flask-openapi3 e Flask-SQLAlchemy

- Testes e Validação de Dados:
nose2 (0.14.0) e pydantic (2.5.2)

- Bancos de Dados e SQL:
SQLAlchemy (2.0.12) e SQLAlchemy-Utils (0.41.1)

- Machine Learning:
scikit-learn (1.3.2), numpy (1.26.2), pandas (2.1.4) e joblib (1.3.2)

- Testes Automatizados:
pytest (7.4.3)

## 3 - Como executar

- Navegue até o diretório da API, na raiz do projeto.

- Crie e ative um ambiente virtual (opcional, mas fortemente recomendado):

Mac / Linux

$ python3 -m venv env 

$ source env/bin/activate  # no Linux/macOS

Windows

$ env\Scripts\activate  # no Windows

- Instale as dependências:
(env)$ pip install -r requirements.txt

- Para executar a API, utilize o comando:
(env)$ flask run --port=5000

Navegue até http://localhost:5000 para acessar a documentação da API, disponível através do Swagger.
---

## 4 - Execução do Teste Automatizado

A aplicação possui um teste automatizado, criado com o framework pytest. Execute o teste usando o seguinte comando:
$ pytest -v test_modelos.py
