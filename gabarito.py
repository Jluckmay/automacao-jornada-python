# Importando as bibliotecas necessárias
import pyautogui
import time
import pandas as pd
import plataform as plt

# Configurações iniciais
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
link = "https://jluckmay.github.io/automacao-jornada-python/"
email = "automacao@hashtag.com"
senha = "senha_super_secreta"

# Detectando o sistema operacional
sistema = plt.system()

# Configurando o navegador e a tecla de atalho para abrir o menu iniciar
if sistema == "Windows":
    navegador = "edge"
    iniciar = "win"
elif sistema == "Linux":
    navegador = "firefox"
    iniciar = "super"
elif sistema == "Darwin":  # macOS
    navegador = "safari"
    iniciar = ["command", "space"]
else:
    raise Exception("Sistema operacional não suportado.")

# Configurando o tempo de pausa entre as ações do PyAutoGUI
pyautogui.PAUSE = 0.5

# Abrir o navegador padrão Windows (Edge)
if sistema == "Darwin":
    pyautogui.hotkey(*iniciar)  # Pressiona Command + Space para abrir o Spotlight
else:
    pyautogui.press(iniciar)  # Pressiona a tecla de atalho para abrir o menu iniciar

pyautogui.write(navegador)
pyautogui.press("enter")

# Acessar o link do sistema de cadastro
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login

# Selecionar o campo de email
pyautogui.press("tab") 

# Preencher o campo de email
pyautogui.write(email)
# Passar para o próximo campo
pyautogui.press("tab")
# Preencher o campo de senha
pyautogui.write(senha)
# Enviar o formulário de login
pyautogui.press("enter") 
# Aguardar 3 segundos para a página carregar
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar    
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:

    pyautogui.press("tab") # passar pro campo de código

    # Pegando código da tabela
    codigo = tabela.loc[linha, "codigo"]
    # Preencher o campo
    pyautogui.write(str(codigo))

    # Passar para o proximo campo
    pyautogui.press("tab")

    # Preencher o campo marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # Preencher o campo tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # Preencher o campo categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preencher o campo preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Preencher o campo custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Pegando a observação da tabela, caso exista
    obs = tabela.loc[linha, "obs"]
    # Se a observação não for nula, preenche o campo de observação
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    # Cadastra o produto (botão enviar)
    pyautogui.press("enter") 
   
    # Ir para o topo da página para cadastrar o próximo produto
    pyautogui.press("home")

    # Passo 5: Repetir o processo de cadastro até o fim
