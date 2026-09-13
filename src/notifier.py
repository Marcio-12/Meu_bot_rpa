import requests

def enviar_alerta(mensagem):
    ("""
    Envia uma notificação de alerta sobre itens processados
    """)
    print(f"[ALERTA NOTIFIER] {mensagem}")
    