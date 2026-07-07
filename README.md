# Automação de Tarefas (Task Automation)

Este projeto consiste no desenvolvimento de um sistema automatizado para o cadastro de produtos em uma plataforma web. A solução foi implementada em Python, utilizando as bibliotecas PyAutoGUI e Pandas, como parte do material de estudos da Jornada Python desenvolvida pela Hashtag Treinamentos.

## Descrição

O projeto tem como objetivo otimizar e automatizar o processo repetitivo de inserção de dados de produtos, realizando o preenchimento de formulários web a partir do consumo de uma base de dados em formato CSV. A ferramenta emula de forma precisa a interação humana com a interface gráfica do sistema receptor, executando rotinas de clique, digitação e navegação contextual.

## Funcionalidades

* Inicialização automatizada do navegador web.
* Navegação direcionada à URL do sistema de cadastro.
* Autenticação de usuário (Login) automatizada.
* Importação e processamento de dados estruturados a partir de arquivo CSV.
* Preenchimento dinâmico dos campos do formulário com base nos registros importados.
* Tratamento condicional para campos opcionais (ex: observações).
* Estrutura de repetição integrada para o processamento em lote de todos os itens da planilha.

## Conceitos e Técnicas Aplicadas

* **Automação de Interface Gráfica (GUI):** Controle programático de periféricos (mouse e teclado) via PyAutoGUI.
* **Engenharia de Dados Básica:** Manipulação, filtragem e leitura de arquivos CSV através da biblioteca Pandas.
* **Orquestração de Fluxo:** Implementação de estruturas de repetição para processamento em massa e condicionais para validação de dados.
* **Sincronização de Processos:** Gerenciamento de tempo de espera (*delays*) para alinhamento com o tempo de resposta da interface web.

## Metodologia e Boas Práticas

1. **Segregação de Escopo:** Divisão do projeto em scripts de mapeamento de ambiente e scripts de execução principal.
2. **Mapeamento de Coordenadas:** Utilização de ferramenta auxiliar para identificação dos pontos cartesianos da tela, garantindo a precisão dos cliques.
3. **Desenvolvimento Incremental:** Homologação do código por meio de testes controlados com amostragem reduzida antes da execução em larga escala.
4. **Otimização de Navegação:** Uso estratégico de atalhos de teclado (como a tecla `TAB`) para garantir a fluidez e velocidade na alternância de campos.

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem de programação core.
* **PyAutoGUI:** Biblioteca para automação de interações de interface.
* **Pandas:** Biblioteca para análise e manipulação de estruturas de dados.

## Arquivos do Projeto

* `gabarito.py`: Script principal responsável pela execução do fluxo de automação.
* `pegar_posicao.py`: Script utilitário para captura das coordenadas dos elementos na tela.
* `produtos.csv`: Base de dados local contendo o inventário de produtos a ser cadastrado.
* `logica.drawio`: Diagrama de fluxo representando a arquitetura lógica do algoritmo.

---

## Como Usar

Siga as instruções abaixo para configurar o ambiente e executar a automação de forma correta.

### 1. Pré-requisitos
Certifique-se de possuir o Python instalado em sua máquina. Caso não possua, faça o download e instalação através do link oficial:

> 📥 [Clique aqui para baixar o Python (Site Oficial)](https://www.python.org/downloads/)

*Nota: Durante a instalação no Windows, lembre-se de marcar a opção **"Add Python to PATH"**.*

### 2. Instalação das Dependências
Clone o repositório, acesse a pasta do projeto via terminal e instale os pacotes necessários utilizando o gerenciador de pacotes (`pip`):

```bash
pip install -r requirements.txt
```

*Caso não possua o arquivo `requirements.txt`, você pode instalar as dependências diretamente executando:*

```bash
pip install pyautogui pandas openpyxl
```

### 3. Mapeamento da Tela (Coordenadas)
Como a automação baseia-se em cliques na tela, execute o script auxiliar para descobrir as posições cartesianas (X, Y) dos campos no seu monitor. Execute o comando, posicione o mouse sobre o campo desejado e aguarde o retorno no terminal:

```bash
python pegar_posicao.py
```

### 4. Configuração do Script Principal
* Abra o arquivo `gabarito.py` em seu editor de código.
* Atualize as coordenadas obtidas no passo anterior nas respectivas funções do PyAutoGUI.
* Insira as credenciais válidas nos campos de login, caso necessário.

### 5. Execução do Sistema
Para iniciar o processo de cadastro automatizado, execute o script principal:

```bash
python gabarito.py
```

> 💡 **Recomendação de Teste:** Antes de rodar o processo completo, reduza a base `produtos.csv` para apenas 3 ou 5 registros a fim de validar a integridade do fluxo.

---

## Público-Alvo

* Desenvolvedores de nível iniciante a intermediário que buscam aplicações práticas da linguagem Python.
* Profissionais de operações e administração focados em otimização de processos e eliminação de tarefas repetitivas (*RPA*).

## Aviso Legal

Este software foi desenvolvido estritamente para fins educacionais e didáticos. Certifique-se de possuir as devidas autorizações e conformidade com os termos de uso dos sistemas terceiros antes de implementar qualquer rotina de automação em ambientes de produção.