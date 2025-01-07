import pyautogui as spam
from time import sleep

# Solicitar número de mensagens e a mensagem
limitMsg = int(input('Número de mensagens: '))
msg = input('Mensagem: ')

# Espera para garantir que o WhatsApp Web ou a janela esteja focada
sleep(3)

# Loop para enviar a mensagem o número de vezes solicitado
for i in range(limitMsg):
    spam.typewrite(msg)   # Digita a mensagem
    spam.press('enter')   # Pressiona a tecla "enter" para enviar a mensagem
    sleep(1)  # Tempo entre os envios (1 segundo para simular spam rápido)
    print(f'Mensagem {i+1} enviada')  # Exibe no terminal o número da mensagem enviada
