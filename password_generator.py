"""
@author matheus dias

---Português---
Script para gerar um número determinado de senhas aleatórias, podendo ser baseado em um modelo recomendado de segurança Forte

Segundo a Organization of American States, para se obter uma senha forte é necessário:

a. Comprimento da senha: mínimo de oito caracteres
b. Caracteres numéricos: mínimo de dois números
c. Caracteres especiais: mínimo de um caractere especial
d. Letras maiúsculas: mínimo de uma letra maiúscula
e. Letras minúsculas: mínimo de uma letra minúscula

---English---
Script to generate a determined number of random passwords, which can be based on a recommended Strong security model

According to the Organization of American States, to obtain a strong password you must:

The. Password length: minimum eight characters
B. Numeric characters: minimum of two numbers
w. Special characters: minimum of one special character
d. Letters saved: minimum of one letter saved
It is. Lowercase letters: minimum of one lowercase letter

"""

import random
import string

print('---------- Bem-vindo ao gerador de senhas ----------')

def resposta():
    """
    Pergunta ao usuário se deseja seguir o modelo recomendado de senha forte.
    
    Returns:
        bool: True se o usuário desejar seguir o modelo, False caso contrário.
    """
    resposta_usuario = input('Gostaria que as senhas sigam o modelo recomendado de segurança Forte? (Sim/Não): ')
    return resposta_usuario.lower() == 'sim'

modelo_forte = resposta()

if modelo_forte:
    while True:
        tamanho_da_senha = int(input('Quantos caracteres terá a senha? (mínimo de 8 caracteres): '))
        if tamanho_da_senha >= 8:
            break
        else:
            print("O tamanho mínimo da senha deve ser de 8 caracteres ou mais. Tente novamente.")

numero_de_senhas = int(input('Quantas senhas gostaria de gerar? '))

print('Aqui estão as senhas geradas: ')

def gerar_senha():
    """
    Gera uma senha seguindo o modelo recomendado de senha forte.
    
    Returns:
        str: A senha gerada.
    """
    caracteres_permitidos = string.ascii_letters + string.digits + string.punctuation
    senha = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    senha += ''.join(random.choice(caracteres_permitidos) for _ in range(max(tamanho_da_senha - 4, 4)))
    return ''.join(random.sample(senha, len(senha)))

if modelo_forte:
    for _ in range(numero_de_senhas):
        senha = gerar_senha()
        print(senha)
else:
    for _ in range(numero_de_senhas):
        senha = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(tamanho_da_senha))
        print(senha)
