# Sistema Bancário Completo em Python 🏦🐍

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Licença](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)

## 📄 Descrição do Projeto

Este projeto é uma simulação de um sistema bancário completo desenvolvido em Python, com suporte a múltiplos usuários e contas. O objetivo é praticar conceitos fundamentais de programação, como funções, listas, dicionários, parâmetros nomeados, além de lógica de controle e interação via terminal.

O sistema permite que o usuário realize operações como depósito, saque, extrato, criação de usuários e contas, e listagem de contas, tudo por meio de um menu interativo.

## ✨ Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

* **[1] Depositar:** Adiciona um valor ao saldo da conta. O valor do depósito deve ser positivo.
* **[2] Sacar:** Retira um valor do saldo da conta, sujeito a regras de limite e quantidade de saques.
* **[3] Extrato:** Exibe todas as transações (depósitos e saques) realizadas e o saldo atual da conta.
* **[4] Nova conta:** Cria uma nova conta bancária para um usuário já cadastrado.
* **[5] Listar contas:** Exibe todas as contas cadastradas no sistema.
* **[6] Novo usuário:** Permite o cadastro de um novo usuário no sistema.
* **[0] Sair:** Encerra a aplicação.

## 🏦 Regras de Negócio

1.  **Depósito:**
    * Não é permitido depositar valores negativos ou iguais a zero.

2.  **Saque:**
    * O sistema permite um máximo de **3 saques** por usuário.
    * O valor máximo por saque é de **R$ 500,00**.
    * Não é possível sacar um valor maior do que o saldo disponível em conta.

3.  **Extrato:**
    * Se nenhuma transação tiver sido feita, exibe a mensagem: "Não foram realizadas movimentações."
    * Ao final do extrato, sempre exibe o saldo atual da conta, formatado como `R$ xxx.xx`.

4.  **Usuários e Contas:**
    * Cada usuário é identificado por um CPF único.
    * Uma conta só pode ser criada para um usuário já cadastrado.
    * É possível listar todas as contas e seus titulares.

## 🚀 Como Executar

Para rodar este projeto, você precisará ter o **Python 3** instalado em sua máquina.

1.  **Faça o download ou clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/Sistema_Bancario_Python.git
    ```
    *(Se não estiver no GitHub, apenas salve o arquivo `desafio.py` em uma pasta no seu computador)*.

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Sistema_Bancario_Python
    ```

3.  **Execute o script Python:**
    ```bash
    python desafio.py
    ```

Após a execução, o menu interativo será exibido no seu terminal.

## 💡 Possíveis Melhorias

* **Persistência de Dados:** Salvar os dados dos usuários e contas em arquivos (`.txt`, `.csv`, `.json`) para manter as informações após fechar o programa.
* **Validação de Dados:** Melhorar a validação dos campos de entrada (CPF, datas, valores).
* **Interface Gráfica:** Desenvolver uma interface mais amigável utilizando bibliotecas como `Tkinter` ou `PyQt`.
* **Relatórios:** Gerar relatórios de movimentações por usuário ou conta.
* **Testes Automatizados:** Adicionar testes para garantir a robustez do sistema.

---

Projeto para fins educacionais, desenvolvido para praticar lógica e fundamentos de Python.
