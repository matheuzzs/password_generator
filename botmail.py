"""
---Português---
Script para automatizar o envio de e-mails

Um script para enviar emails automaticamente é uma ferramenta útil que automatiza o processo de envio de emails, tornando-o mais eficiente e conveniente.

---English---
Script to automate sending emails

An auto send email script is a useful tool that automates the email sending process, making it more efficient and convenient.

"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

# Configurações de email (criar arquivo .env)
email_de_envio = config("SEU_EMAIL")
senha = config("SUA_SENHA") #Apenas senhas de aplicativo (A2F)

# Lista de destinatários
destinatarios = ["matheusdias12356@gmail.com"]
assunto = "Assunto do Email"

# Corpo do email
mensagem = """
Olá,

Exemplo de link:
<a href="https://www.exemplo.com">Visitar o Site</a>

Exemplo de imagem:
<img src="https://www.exemplo.com/.png">
"""

# Configuração do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Porta padrão

# Criar o objeto MIME para o email
msg = MIMEMultipart()
msg['From'] = email_de_envio
msg['Subject'] = assunto

# Adicionar o corpo do email
msg.attach(MIMEText(mensagem, 'plain'))

# Criar uma conexão segura com o servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_de_envio, senha)

    # Enviar o email para cada destinatário
    for destinatario in destinatarios:
        msg['To'] = destinatario
        texto = msg.as_string()
        server.sendmail(email_de_envio, destinatario, texto)
        print(f"Email enviado para {destinatario} com sucesso!")

except Exception as e:
    print(f"Erro ao enviar os emails: {str(e)}")

finally:
    server.quit()
