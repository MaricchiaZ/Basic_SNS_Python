# Projeto Básico em python para um primeiro contato com o AWS SNS

### Pré-requisito:

Abra o docker desktop...\

Já no VsCode inicialize o container:\
`localstack start -d`

# 1 - Iniciando um projeto Python:

`touch main.py`

### Entre na pasta do projeto:

Para "compilar" o arquivo python:\
`python3 main.py`

### Para listar os tópicos no SNS:
Para ver o retorno da função no terminal:\
`awslocal sns list-topics`\

### Para listar os inscritos nos tópicos:
Para ver o retorno da função no terminal:\
`awslocal sns list-subscriptions`\

