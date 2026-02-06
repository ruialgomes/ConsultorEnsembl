# Consultor de Variantes do Ensembl

Essa é uma aplicação web para realizar a consulta de variantes genéticas humanas, utilizando a [Ensembl REST API](https://rest.ensembl.org/) como fonte de dados e desenvolvida em Python e Flask, e utilizando docker. Apos inserir o rsID desejado, é feita a busca no Ensembl para variantes humanas, e os resultados principais sao mostrados. Ainda, caso desejado, há botões que permitem acessar toda informação disponibilizada pelo Ensembl, tanto em forma de tabela simples com lista de dados, quanto diretamente no formato JSON disponibilizado pelo banco de dados, ou ate usar diretamente o JSON obtendo da API.

## Funcionalidades
- Consulta de variantes por identificador (rsID).
- Visualização de dados principais: Cromossomo, Posição, Alelos e MAF.
- Tabelas Dinâmicas, com opção para expandir e visualizar todos os atributos retornados pela API em formato tabular ou JSON.
- Interface responsiva utilizando Bootstrap 5.
- API Endpoint interno para retorno em formato JSON.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Web Framework:** Flask 3.0.0
- **Consumo de API:** Requests 2.31.0
- **Testes:** Pytest 7.4.0
- **Containerização:** Docker 29.2.1

---

## Como Executar o Projeto

### Docker
Certifique-se de ter o [Docker](https://www.docker.com/get-started/) instalado. Baixe o projeto para sua máquina e extraia para a pasta desejada. Abra o terminal/bash e navegue ate a pasta extraida do projeto e execute os seguintes comandos:

```bash
# Construir a imagem
docker build -t consultor-ensembl .

# Rodar o container
docker run -p 5000:5000 consultor-ensembl
```
Onde 'Consultor-ensembl' pode ser trocado para qualquer nome desejado.

Abra o navegador em http://localhost:5000/

No campo de busca, insira um Identificador de Variante (rsID).

Clique em Consultar

O sistema exibirá um card com as informações essenciais (Cromossomo, Posição, Alelos, etc.).

Se desejar ver todos os dados técnicos retornados pelo Ensembl, clique nos botões para abrir em uma tabela ou direto no formato JSON para ser reaproveitado.

Para testar com pytest, execute: 

```bash
# Testar com pytest
docker run --rm consultor-ensembl pytest
```
