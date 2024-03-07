#passo a passo do projeto
#pyautogui.clik -> clicar em algum lugar da tela 
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar um botao 

#passo 1: entrar no sistema 
 
import pyautogui 
import time
import pandas

#vai dar uma pausa em todo seu programa depois do pyautogui ser usado 
pyautogui.PAUSE = 0.5
  


#abrir o navegador (chrome) no windows 
pyautogui.press("win")
pyautogui.write("safari")
pyautogui.press("enter")

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa caso a internet esteja lenta
time.sleep(3)

#passo 2: fazer login no sistema 
#fazer login acessando a posição da tela usando o arquiv "auxiliar_automacao.py"

#digitar email
pyautogui.click(x=714, y=465)
pyautogui.write("emailteste@gmail.com")

#digitar a senha 
pyautogui.press("tab")
pyautogui.write("senha")

#logar
pyautogui.click(x=952, y=680)
time.sleep(3)

#passo 3: impotar basse de dados

tabela = pandas.read_csv("produtos.csv") #read + a extenção do arquivo 

#passo 4: cadastrar pordutos
#clicar na primeira posição

for linha in tabela.index:
    pyautogui.click(x=709, y=319)

    #cadastrar o produto
    #codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

#enviar
pyautogui.press("enter")
pyautogui.scroll(5000)
