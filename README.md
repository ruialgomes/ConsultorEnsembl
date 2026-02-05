# Consultor de Variantes do Ensembl

Uma aplicação web desenvolvida em Python e Flask para consulta de variantes genéticas humanas, utilizando a [Ensembl REST API](https://rest.ensembl.org/).

## Funcionalidades
- Consulta de variantes por identificador (rsID).
- Visualização de dados principais: Cromossomo, Posição, Alelos e MAF.
- **Tabela Dinâmica**: Opção para expandir e visualizar todos os atributos retornados pela API.
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
Certifique-se de ter o Docker instalado. Na raiz do projeto, execute:

```bash
# Construir a imagem
docker build -t consultor-ensembl .

# Rodar o container
docker run -p 5000:5000 consultor-ensembl
```

Abra o navegador em http://localhost:5000/

No campo de busca, insira um Identificador de Variante (rsID).

Clique em Consultar

O sistema exibirá um card com as informações essenciais (Cromossomo, Posição, Alelos, etc.).

Se desejar ver todos os dados técnicos retornados pelo Ensembl, clique nos botões para abrir em uma tabela ou direto no formato JSON para ser reaproveitado.