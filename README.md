# Projeto Fonte controlada

Um  projeto de desenvolvimento para uma fonte controlada usando Raspberry

## Pré-requisitos para o sistema

Para montar um ambiente de desenvolvimento python:

```text
Python 3.8 ou superior
pip 20.0 ou superior
virtualenv 20.4 ou superior
```

Criando o ambiente virtual:

```text
python -m venv <nome-ambiente>
```

Ativar o embiente:

```text
source nome_ambiente/bin/activate
```

Com o ambiente ativado instalamos as dependências:

```text
pip instal -r requirements.txt
```

Para atualizar o arquivo requirements.txt cada vez que for atualizando pacotes:

```text
pip freeze > requirements.txt
```
