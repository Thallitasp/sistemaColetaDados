# 📋 Sistema de Coleta de Dados Básico em Python (`sistemaColetaDados`)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Licença](https://img.shields.io/badge/Licença-Acadêmica-lightgrey)

Sistema interativo desenvolvido em **Python** para coleta, validação, classificação e análise estatística de dados de clientes da empresa fictícia **TechNova Soluções Digitais**. O projeto aplica os fundamentos de pensamento lógico-computacional, tipos de dados, estruturas sequenciais, estruturas condicionais, operadores lógicos/relacionais e laços de repetição (`while` e `for`).

---

## 📑 Índice

1. [Objetivo do Projeto](#-objetivo-do-projeto)
2. [Estrutura do Repositório](#-estrutura-do-repositório)
3. [Arquitetura e Detalhamento da Classe](#-arquitetura-e-detalhamento-da-classe)
4. [Conceitos Aplicados](#-conceitos-aplicados)
5. [Como Executar](#-como-executar)
6. [Exemplos de Uso e Saída](#-exemplos-de-uso-e-saída)
7. [Autoria](#-autoria)

---

## 🎯 Objetivo do Projeto

Construir uma aplicação de linha de comando (CLI) funcional e bem comentada para registrar pesquisas de satisfação e perfil socioeconômico de clientes, transformando entradas brutas do usuário em classificações estratégicas e indicadores gerenciais consolidados.

---

## 📁 Estrutura do Repositório

```text
sistemaColetaDados/
├── coletaDados.py   # Código-fonte principal contendo a classe SistemaColetaDados
└── README.md        # Documentação técnica do projeto
```

---

## 🧩 Arquitetura e Detalhamento da Classe

Toda a lógica da aplicação está encapsulada na classe **`SistemaColetaDados`** (`coletaDados.py`):

- **`__init__(self, nome_empresa: str = "TechNova Soluções Digitais")`**  
  Inicializa a identidade da empresa e a lista `self.registros` onde os dicionários de cada cliente são armazenados.
- **`classificar_perfil_cliente(self, idade: int, renda: float, nota: int) -> str`**  
  Aplica estruturas condicionais encadeadas (`if / elif / else`) combinadas com operadores relacionais (`>=`, `<=`, `<`) e lógicos (`and`, `or`) para segmentar cada cliente em *Cliente VIP Promotor*, *Jovem Engajado*, *Atenção / Retenção Prioritária* ou *Cliente Padrão*.
- **`coletar_novo_cliente(self) -> None`**  
  Conduz a coleta sequencial dos dados (`nome`, `cidade`, `idade`, `renda`, `nota` e `aceita_contato`), protegendo cada campo numérico e textual com laços `while` de validação e tratamento de exceções (`ValueError`).
- **`listar_clientes_cadastrados(self) -> None`**  
  Itera sobre `self.registros` com um loop `for` para exibir todos os cadastros formatados.
- **`exibir_relatorio_geral(self) -> None`**  
  Processa acumuladores dentro de um loop `for` para calcular média de idade, renda média, nota média de satisfação, percentual de clientes promotores e adesão à newsletter.
- **`executar_menu(self) -> None`**  
  Controla o fluxo contínuo da aplicação via loop `while True` até que o usuário selecione a opção de encerramento (`0`).

---

## 🛠️ Conceitos Aplicados

- **Tipos de Dados e Variáveis:** Manipulação explícita de `str`, `int`, `float`, `bool`, `list` e `dict`.
- **Estruturas Sequenciais:** Fluxo ordenado de entrada, processamento, classificação e exibição de confirmação a cada cadastro.
- **Estruturas Condicionais e Operadores:** Tomada de decisão no menu, validações de intervalo (`18 <= idade <= 110`, `1 <= nota <= 5`) e regras compostas (`and` / `or`) de segmentação de perfil.
- **Estruturas de Repetição:** Uso de `while` para controle de menu e repetição até entrada válida, e `for` para varredura de registros e cálculos estatísticos.

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.8 ou superior** instalado (utiliza apenas recursos nativos da linguagem).

### Passo a passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/Thallitasp/sistemaColetaDados.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistemaColetaDados
   ```
3. Execute o sistema:
   - **Windows (PowerShell / CMD):**
     ```powershell
     py coletaDados.py
     ```
   - **Linux / macOS:**
     ```bash
     python3 coletaDados.py
     ```

---

## 🖥️ Exemplos de Uso e Saída

### Menu Principal
```text
####################################################
  TECHNOVA SOLUÇÕES DIGITAIS - COLETA DE DADOS
####################################################
1 - Coletar dados de novo cliente
2 - Listar clientes cadastrados
3 - Exibir relatório estatístico consolidado
0 - Encerrar sistema
####################################################
Escolha uma opção:
```

### Relatório Estatístico Consolidado
```text
====================================================
   RELATÓRIO ANALÍTICO — TECHNOVA SOLUÇÕES DIGITAIS
====================================================
Total de clientes entrevistados: 3
Média de idade do público: 29.7 anos
Renda mensal média: R$ 4100.00
Nota média de satisfação: 4.33 / 5.00
Clientes satisfeitos (notas 4 e 5): 2 (66.7%)
Aceitaram receber novidades: 2 de 3
====================================================
```

---

## 👩‍💻 Autoria

Desenvolvido por **Thallita da Silva Pedreira**  