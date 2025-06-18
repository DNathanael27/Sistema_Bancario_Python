# Sistema Bancário Simples em Python 🐍

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Licença](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)

## 📄 Descrição do Projeto

Este projeto é uma simulação de um sistema bancário básico desenvolvido em Python. O objetivo é praticar conceitos fundamentais de programação, como variáveis, condicionais e laços de repetição, através da criação de um sistema interativo via terminal.

O sistema permite que o usuário realize três operações financeiras básicas: depósito, saque e visualização de extrato, operando com uma única conta.

## ✨ Funcionalidades

O sistema oferece um menu interativo com 4 opções:

* **[1] Depositar:** Adiciona um valor ao saldo da conta. O valor do depósito deve ser positivo.
* **[2] Sacar:** Retira um valor do saldo da conta, sujeito a certas regras e limites.
* **[3] Extrato:** Exibe todas as transações (depósitos e saques) realizadas e o saldo atual da conta.
* **[4] Sair:** Encerra a aplicação.

## 🏦 Regras de Negócio

Para garantir a integridade das operações, o sistema segue as seguintes regras:

1.  **Depósito:**
    * Não é permitido depositar valores negativos ou iguais a zero.

2.  **Saque:**
    * O sistema permite um máximo de **3 saques** por dia.
    * O valor máximo por saque é de **R$ 500,00**.
    * Não é possível sacar um valor maior do que o saldo disponível em conta.

3.  **Extrato:**
    * Se nenhuma transação tiver sido feita, exibe a mensagem: "Não foram realizadas movimentações."
    * Ao final do extrato, sempre exibe o saldo atual da conta, formatado como `R$ xxx.xx`.

## 🚀 Como Executar

Para rodar este projeto, você precisará ter o **Python 3** instalado em sua máquina.

1.  **Faça o download ou clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/Sistema_Bancario_Python.git](https://github.com/seu-usuario/Sistema_Bancario_Python.git)
    ```
    (Se não estiver no GitHub, apenas salve o arquivo `.py` em uma pasta no seu computador).

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Sistema_Bancario_Python
    ```

3.  **Execute o script Python:**
    ```bash
    python sistema_bancario.py
    ```
    *(Substitua `sistema_bancario.py` pelo nome que você deu ao seu arquivo)*.

Após a execução, o menu interativo será exibido no seu terminal.

## 💡 Possíveis Melhorias

Este é um projeto inicial, mas que pode ser expandido com novas funcionalidades:

* **Modularização:** Refatorar o código para usar funções, separando as responsabilidades (ex: `def depositar()`, `def sacar()`, etc.).
* **Múltiplos Usuários:** Criar uma estrutura (usando dicionários ou listas de objetos) para gerenciar múltiplas contas bancárias.
* **Persistência de Dados:** Salvar os dados da conta em um arquivo (`.txt`, `.csv`, `.json`) para que as informações não se percam ao fechar o programa.
* **Interface Gráfica:** Desenvolver uma interface mais amigável utilizando bibliotecas como `Tkinter` ou `PyQt`.
