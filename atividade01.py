# Importando a biblioteca pyautogui e atribuindo um apelido direto
import pyautogui as p


# Abre o executar do Windows.
p.hotkey("win", "d", duration=1)
p.hotkey("win", "r", duration=1)
p.sleep(1)
p.typewrite("chrome.exe https://github.com/")
p.sleep(1)
p.hotkey("enter")

p.sleep(2)
p.moveTo(x=1152, y=93, duration=1)
p.click(x=1152, y=93)

p.sleep(1)
p.moveTo(x=1211, y=111, duration=1)
p.click(x=1211, y=111)

# Click no label Usuário.
p.sleep(1)
p.moveTo(x=606, y=292, duration=1)
p.click(x=606, y=292)
p.typewrite("david.simas81@gmail.com")

# Click no label Password.
p.sleep(1)
p.moveTo(x=606, y=363, duration=1)
p.click(x=606, y=363)
p.typewrite("1234567890")

# Click no botão login.
p.sleep(1)
p.moveTo(x=606, y=419, duration=1)
p.click(x=606, y=419)

# Click para fechar o tradutor.
p.sleep(1)
p.moveTo(x=1301, y=90, duration=1)
p.click(x=1301, y=90)

# Click no botão para criar um novo Repositório.
p.sleep(1)
p.moveTo(x=281, y=176, duration=1)
p.click(x=281, y=176)

# Click no label nome do repositório.
p.sleep(1)
p.moveTo(x=541, y=332, duration=1)
p.click(x=541, y=332)
# Nome do repositório.
p.typewrite("atividade_automacao")

# Click no label descrição do repositório.
p.sleep(1)
p.moveTo(x=382, y=435, duration=1)
p.click(x=382, y=435)
# Descrição do repositório.
p.typewrite("Atividade em sala sobre automação em Python.")

# Click no checkbox "Adicionar um arquivo README".
p.sleep(1)
p.moveTo(x=368, y=671, duration=1)
p.click(x=368, y=671)

# Click para o scroll da tela.
p.sleep(1)
p.moveTo(x=1429, y=819, duration=1)
p.click(x=1429, y=819)

# Adiciona o .gitignore.
p.sleep(1)
p.moveTo(x=511, y=442, duration=1)
p.click(x=511, y=442)

# Seleciona Python.
p.sleep(1)
p.moveTo(x=492, y=521, duration=1)
p.click(x=492, y=521)
p.typewrite("Python")
p.sleep(1)
p.hotkey("enter")

# Click no botão "Create repository".
p.sleep(1)
p.moveTo(x=404, y=689, duration=1)
p.click(x=404, y=689)

# Click no botão "Code".
p.sleep(7)
p.moveTo(x=956, y=281, duration=1)
p.click(x=956, y=281)

# Copia o link do repositório.
p.sleep(7)
p.moveTo(x=965, y=461, duration=1)
p.click(x=965, y=461)

p.hotkey("win", "d", duration=1)
p.sleep(1)

p.hotkey("win", "r", duration=1)
p.typewrite("cmd")
p.hotkey("enter")
p.sleep(1)
p.typewrite("cd /")
p.hotkey("enter")
p.typewrite("cd Python")
p.hotkey("enter")
# Comando para clonar o repositório.
p.typewrite("git clone https://github.com/davidsimas/atividade_automacao.git")
p.hotkey("enter")
p.typewrite("cd atividade_automacao")
p.hotkey("enter")
p.typewrite("type nul > exemplo.py")
p.hotkey("enter")
p.typewrite("code .")
p.hotkey("enter")
