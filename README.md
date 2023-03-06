# Programa Trainee Biopark 2023
Projeto desenvolvido como solução para o Desafio Tech do Programa de Trainee 2023 do Biopark.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Ferramentas utilizadas

* Python 3.9
* Flask
* SQL Alchemy
* PyMySQL
* SQL Alchemy orm
* MySQL
* Pycharm Community Edition 2022.3.2
* HTML
* CSS

Clone o projeto para a sua pasta pessoal através do comando git:

```
git clone https...
```

Se já tiver o Python 3.9 instalado é só prosseguir com os próximos passos, caso contrário,
após a instalação do Python 3.9, crie seu ambiente virtual da seguinte maneira:

```
python -m venv venv
```

Realize as instalações do Flask e suas dependências, conforme descrito abaixo:

```
pip install flask
```
```
pip install SQLAlchemy
```
```
pip install sqlalchemy-orm
```
```
pip install PyMySQL
```

** É necessária a criação de uma instância de banco de dados MySQL para o armazenamento das tabelas que serão criadas.

Após a instalação das dependências e da criação do banco de dados, abra o arquivo main e configure a conexão com o banco da seguinte maneira:

```
app.config['SQLALCHEMY_DATABASE_URI'] = '{mysql+pymysql}://{root}:{senha}@{localhost}/{banco de dados}'
```
Após realizar a configuração, é só executar o arquivo main.py no terminal:

```
python main.py
```

As tabelas serão criadas de forma automática pelo script Flask e as funcionalidades da aplicação estarão prontas.

Será exibida uma rota para o acesso da aplicação no terminal conforme exemplo: 'http://127.0.0.1:5000/'

Basta acessar o sistema e conferir as funcionalidades requeridas no desafio. :)

## ✒️ Autor

* Wesley Antonio Santos de Andrade Sobreira
