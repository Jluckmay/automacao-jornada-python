# Automação de Tarefas | Task Automation

🌍 *[Read this in English](#-english-version)* | 🇧🇷 *[Leia em Português](#-versão-em-português)*

---

## 🇧🇷 Versão em Português

Este projeto consiste no desenvolvimento de um sistema automatizado para o cadastro de produtos em uma plataforma web. A solução foi implementada em Python, utilizando as bibliotecas PyAutoGUI e Pandas, como parte do material de estudos da Jornada Python desenvolvida pela Hashtag Treinamentos.

### Descrição

O script tem como objetivo otimizar e automatizar o processo repetitivo de inserção de dados de produtos, realizando o preenchimento de formulários web a partir do consumo de uma base de dados em formato CSV. A ferramenta emula de forma precisa a interação humana com a interface gráfica do sistema receptor, executando rotinas de clique, digitação e navegação contextual.

### Funcionalidades

* Inicialização automatizada do navegador web.
* Navegação direcionada à URL do sistema de cadastro.
* Autenticação de usuário (Login) automatizada.
* Importação e processamento de dados estruturados a partir de arquivo CSV.
* Preenchimento dinâmico dos campos do formulário com base nos registros importados.
* Tratamento condicional para campos opcionais (ex: observações).
* Estrutura de repetição integrada para o processamento em lote de todos os itens da planilha.

### Conceitos e Técnicas Aplicadas

* **Automação de Interface Gráfica (GUI):** Controle programático de periféricos (mouse e teclado) via PyAutoGUI.
* **Engenharia de Dados Básica:** Manipulação, filtragem e leitura de arquivos CSV através da biblioteca Pandas.
* **Orquestração de Fluxo:** Implementação de estruturas de repetição para processamento em massa e condicionais para validação de dados.
* **Sincronização de Processos:** Gerenciamento de tempo de espera (*delays*) para alinhamento com o tempo de resposta da interface web.

### Metodologia e Boas Práticas

1. **Segregação de Escopo:** Divisão do projeto em scripts de mapeamento de ambiente e scripts de execução principal.
2. **Mapeamento de Coordenadas:** Utilização de ferramenta auxiliar para identificação dos pontos cartesianos da tela, garantindo a precisão dos cliques.
3. **Desenvolvimento Incremental:** Homologação do código por meio de testes controlados com amostragem reduzida antes da execução em larga escala.
4. **Otimização de Navegação:** Uso estratégico de atalhos de teclado (como a tecla `TAB`) para garantir a fluidez e velocidade na alternância de campos.

### Tecnologias Utilizadas

* **Python 3.x:** Linguagem de programação core.
* **PyAutoGUI:** Biblioteca para automação de interações de interface.
* **Pandas:** Biblioteca para análise e manipulação de estruturas de dados.

### Arquivos do Projeto

* `gabarito.py`: Script principal responsável pela execução do fluxo de automação.
* `pegar_posicao.py`: Script utilitário para captura das coordenadas dos elementos na tela.
* `produtos.csv`: Base de dados local contendo o inventário de produtos a ser cadastrado.
* `logica.drawio`: Diagrama de fluxo representando a arquitetura lógica do algoritmo.

### Como Usar

Siga as instruções abaixo para configurar o ambiente e executar a automação de forma correta.

#### 1. Pré-requisitos
Certifique-se de possuir o Python instalado em sua máquina. Caso não possua, faça o download e instalação através do link oficial:

> 📥 [Clique aqui para baixar o Python (Site Oficial)](https://www.python.org/downloads/)

*Nota: Durante a instalação no Windows, lembre-se de marcar a opção **"Add Python to PATH"**.*

#### 2. Instalação das Dependências
Clone o repositório, acesse a pasta do projeto via terminal e instale os pacotes necessários utilizando o gerenciador de pacotes (`pip`):

```bash
pip install -r requirements.txt
```

*Caso não possua o arquivo `requirements.txt`, instale diretamente:*

```bash
pip install pyautogui pandas openpyxl
```

#### 3. Mapeamento da Tela (Coordenadas)
Como a automação baseia-se em cliques na tela, execute o script auxiliar para descobrir as posições cartesianas (X, Y) dos campos no seu monitor. Execute o comando, posicione o mouse sobre o campo desejado e aguarde o retorno no terminal:

```bash
python pegar_posicao.py
```

#### 4. Configuração do Script Principal
* Abra o arquivo `gabarito.py` em seu editor de código.
* Atualize as coordenadas obtidas no passo anterior nas respectivas funções do PyAutoGUI.
* Insira as credenciais válidas nos campos de login, caso necessário.

#### 5. Execução do Sistema
Para iniciar o processo de cadastro automatizado, execute o script principal:

```bash
python gabarito.py
```

> 💡 **Recomendação de Teste:** Antes de rodar o processo completo, reduza a base `produtos.csv` para apenas 3 ou 5 registros a fim de validar a integridade do fluxo.

### Público-Alvo

* Desenvolvedores de nível iniciante a intermediário que buscam aplicações práticas da linguagem Python.
* Profissionais de operações e administração focados em otimização de processos e eliminação de tarefas repetitivas (*RPA*).

### Aviso Legal

Este software foi desenvolvido estritamente para fins educacionais e didáticos. Certifique-se de possuir as devidas autorizações e conformidade com os termos de uso dos sistemas terceiros antes de implementar qualquer rotina de automação em ambientes de produção.

---

## 🇺🇸 English Version

This project consists of the development of an automated system for registering products on a web platform. The solution was implemented in Python, using the PyAutoGUI and Pandas libraries, as part of the study material for the Python Journey developed by Hashtag Treinamentos.

### Description

The script aims to optimize and automate the repetitive process of entering product data by filling out web forms based on data consumed from a CSV file. The tool accurately emulates human interaction with the target system's graphical interface, executing routines for clicking, typing, and contextual navigation.

### Features

* Automated web browser initialization.
* Targeted navigation to the registration system URL.
* Automated user authentication (Login).
* Import and processing of structured data from a CSV file.
* Dynamic form field filling based on imported records.
* Conditional handling for optional fields (e.g., remarks).
* Integrated loop structure for batch processing all items in the spreadsheet.

### Applied Concepts and Techniques

* **Graphical User Interface (GUI) Automation:** Programmatic control of peripherals (mouse and keyboard) via PyAutoGUI.
* **Basic Data Engineering:** Manipulation, filtering, and reading of CSV files through the Pandas library.
* **Flow Orchestration:** Implementation of loop structures for mass processing and conditionals for data validation.
* **Process Synchronization:** Management of wait times (*delays*) to align with the web interface's response time.

### Methodology and Best Practices

1. **Scope Segregation:** Division of the project into environment mapping scripts and main execution scripts.
2. **Coordinate Mapping:** Use of an auxiliary tool to identify the Cartesian points on the screen, ensuring click accuracy.
3. **Incremental Development:** Code homologation through controlled tests with a reduced sample size before large-scale execution.
4. **Navigation Optimization:** Strategic use of keyboard shortcuts (such as the `TAB` key) to ensure fluidity and speed when switching fields.

### Technologies Used

* **Python 3.x:** Core programming language.
* **PyAutoGUI:** Library for interface interaction automation.
* **Pandas:** Library for data structure analysis and manipulation.

### Project Files

* `gabarito.py`: Main script responsible for executing the automation flow.
* `pegar_posicao.py`: Utility script for capturing the coordinates of screen elements.
* `produtos.csv`: Local database containing the product inventory to be registered.
* `logica.drawio`: Flowchart representing the algorithm's logical architecture.

### How to Use

Follow the instructions below to configure the environment and run the automation correctly.

#### 1. Prerequisites
Make sure you have Python installed on your machine. If you do not have it, download and install it from the official link:

> 📥 [Click here to download Python (Official Site)](https://www.python.org/downloads/)

*Note: During installation on Windows, remember to check the **"Add Python to PATH"** option.*

#### 2. Installing Dependencies
Clone the repository, access the project folder via the terminal, and install the necessary packages using the package manager (`pip`):

```bash
pip install -r requirements.txt
```

*If you do not have the `requirements.txt` file, install them directly:*

```bash
pip install pyautogui pandas openpyxl
```

#### 3. Screen Mapping (Coordinates)
Since the automation relies on screen clicks, run the auxiliary script to find the Cartesian positions (X, Y) of the fields on your monitor. Run the command, position your mouse over the desired field, and wait for the terminal output:

```bash
python pegar_posicao.py
```

#### 4. Main Script Configuration
* Open the `gabarito.py` file in your code editor.
* Update the coordinates obtained in the previous step in the respective PyAutoGUI functions.
* Insert valid credentials in the login fields, if necessary.

#### 5. System Execution
To start the automated registration process, run the main script:

```bash
python gabarito.py
```

> 💡 **Testing Recommendation:** Before running the complete process, reduce the `produtos.csv` database to only 3 or 5 records to validate the flow's integrity.

### Target Audience

* Beginner to intermediate developers looking for practical applications of the Python language.
* Operations and administration professionals focused on process optimization and elimination of repetitive tasks (*RPA*).

### Disclaimer

This software was developed strictly for educational and didactic purposes. Make sure you have the proper authorizations and comply with the terms of use of third-party systems before implementing any automation routine in production environments.