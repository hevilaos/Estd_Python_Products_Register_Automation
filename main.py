# O Problema:
# Cadastrar todos os produtos da base de dados no site fornecido
import pandas as pd
import pyautogui as py
import time

linkSite = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.PAUSE = 0.5

#importando a base de dados
tabela = pd.read_csv("produtos.csv")
#print(tabela)

# O que precisa ser feito:seu-email@example.com sua_senha   
# 1. Abrir o navegador
py.hotkey("command" , "space")
py.write("safari")
py.press("enter")
# 2. Acessar o site fornecido
time.sleep(2)
py.write(linkSite)
py.press("enter")
# 3. Fazer login 
## e-mail
time.sleep(1)
py.click(x=2565, y=430)
py.write("seu_email@example.com")
py.press("tab")

## senha
py.write("sua_senha")
py.press("tab")

##clicar no botão de login
py.click(x=2687, y=594)
time.sleep(3)

# 4. Inserir as informações do produto 
## fluxo de repetição
for linha in tabela.index:
    ### Código do produto
    py.click(x=2455, y=312)
    py.write(str(tabela.loc[linha, "codigo"]))
    py.press("tab")
    ### Marca do produto
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    ### Tipo do produto
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    ### Categoria do produto
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    ### Preço unitario do produto
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    ### Custo do produto
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    ### OBS
    if not pd.isna(tabela.loc[linha, "obs"]):
       py.write(str(tabela.loc[linha, "obs"]))
    # 5. Clicar no botão para enviar
    py.scroll(-5)
    py.press("tab")
    py.click(x=2556, y=767)
    ##voltando ao inicicio da tela
    py.scroll(100)
# 6. Repetir o processo para todos os p rodutos da base de dados