# Automação de Tarefas com PyAutoGUI

Neste projeto, utilizamos a biblioteca PyAutoGUI para automatizar tarefas repetitivas em um sistema. O PyAutoGUI é uma ferramenta poderosa que permite simular interações do usuário, como cliques do mouse e pressionamentos de teclas, tornando a automação de tarefas simples e eficiente.

## Passo a passo do projeto

1. **Entrar no Sistema:**
   - Abrimos o navegador (no caso, Safari) para acessar o site necessário.
   - Informamos o link do site e pressionamos "Enter".

2. **Fazer Login no Sistema:**
   - Digitamos o e-mail e a senha nos campos correspondentes.
   - Clicamos no botão de login.

3. **Importar Base de Dados:**
   - Utilizamos a biblioteca Pandas para importar uma base de dados em formato CSV.

4. **Cadastrar Produtos:**
   - Percorremos cada linha da base de dados e preenchemos os campos de cadastro de produtos.
   - Clicamos em "Enviar" para cadastrar o produto.


## Código Auxiliar para Obter Posição do Mouse

```python
import pyautogui
import time

# Esperar 5 segundos antes de mostrar a posição do mouse
time.sleep(5)
print(pyautogui.position())
```

Esse projeto demonstra como a automação de tarefas pode ser facilitada com o PyAutoGUI, economizando tempo e esforço em atividades rotineiras.
