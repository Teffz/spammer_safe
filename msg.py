import pyautogui as spam
from time import sleep
import webbrowser

# Função para garantir que o número de mensagens seja válido
def get_valid_number():
    while True:
        try:
            limitMsg = int(input('Número de mensagens: '))
            if limitMsg <= 0:
                print("Por favor, insira um número positivo.")
            else:
                return limitMsg
        except ValueError:
            print("Por favor, insira um número válido.")

# Solicitar número de mensagens e a mensagem
limitMsg = get_valid_number()  # Chama a função para garantir que o número seja válido
msg = input('Mensagem: ')
numero = input('Digite o número de telefone (incluindo código do país, ex: +5511999999999): ')

# Cria a URL para abrir a conversa no WhatsApp Web
url = f'https://web.whatsapp.com/send?phone={numero}&text={msg}'
print(f'Abrindo WhatsApp Web com o número: {numero} e mensagem: "{msg}"')

# Abrir o WhatsApp Web no navegador com o número e a mensagem
webbrowser.open(url)

# Espera para garantir que o WhatsApp Web ou a janela esteja focada
print("Aguardando 10 segundos para o WhatsApp Web carregar...")
sleep(10)  # Aumente o tempo se necessário para garantir que o WhatsApp Web esteja completamente carregado

# Garantir que a janela do WhatsApp esteja focada com um clique (ajuste se necessário)
spam.click(100, 100)  # Clique em uma posição na tela para garantir que a janela está focada
sleep(1)  # Espera 1 segundo para garantir que o clique foi registrado

# Loop para enviar a mensagem o número de vezes solicitado
for i in range(limitMsg):
    spam.press('enter')  # Pressiona a tecla "enter" para enviar a mensagem
    print(f'Mensagem {i+1} enviada')  # Exibe no terminal o número da mensagem enviada
    sleep(1)  # Tempo entre os envios (1 segundo para simular spam rápido)

print("Envio concluído!")
