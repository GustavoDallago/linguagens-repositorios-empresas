# Projeto: Extração de Linguagens de Programação via API do GitHub 🚀

Este projeto foi desenvolvido como parte da formação de **Python com foco em APIs** da **Alura**. O objetivo central é explorar o ecossistema de APIs REST, praticar automação de processos de dados e aplicar os conceitos de **Programação Orientada a Objetos (POO)**.

## 📋 Sobre o Projeto
O sistema realiza um pipeline de **ETL** (Extract, Transform, Load) para identificar as linguagens de programação predominantes nos repositórios das "Big Techs": **Amazon, Netflix, Spotify e Apple**.

Os dados são extraídos da API oficial do GitHub, processados em DataFrames e exportados para arquivos CSV, que são posteriormente enviados de volta ao GitHub de forma automatizada.

## 🏗️ Estrutura do Repositório (Ambiente WSL/Ubuntu)

O projeto está organizado seguindo as boas práticas de separação de responsabilidades:

* **`1. Projeto/`**: Contém a lógica principal da aplicação.
    * `dados_repos.py`: Classe em POO responsável pela extração (GET) e tratamento dos dados.
    * `repositorio.py`: Script de automação para upload (POST/PUT) dos resultados para o GitHub.
    * `linguagens_usadas.ipynb`: Notebook de estudo com o passo a passo e prototipagem do código.
* **`2. Dados/`**: Repositório local dos arquivos CSV gerados pela aplicação (`amazon.csv`, `apple.csv`, etc.).
* **`3. Atividades/`**: Notebooks com exercícios e desafios propostos durante o curso.

## 🛠️ Tecnologias e Paradigmas
* **Linguagem:** Python 3.10+
* **Bibliotecas Principais:** * `requests`: Comunicação com a API REST.
    * `pandas`: Estruturação e limpeza dos dados extraídos.
    * `base64`: Codificação necessária para o tráfego de arquivos via API.
* **Conceitos Aplicados:** * Programação Orientada a Objetos (Classes, Métodos, `__init__`).
    * Manipulação de Sistemas de Arquivos no Linux (WSL).
    * Autenticação via Tokens (Bearer Token).

---
*Projeto desenvolvido por [Gustavo Dallago](https://github.com/GustavoDallago)*