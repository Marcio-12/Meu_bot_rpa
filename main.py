from src.services import buscar_pendencias
from src.database import iniciar_banco, pendencias_ja_processadas, salvar_pendencias
from src.notifier import enviar_alerta

def executar_bot():
    print("--- Iniciando Robô de Automação ---")
    
    iniciar_banco()
    
    pendencias = buscar_pendencias()
    novos_itens = 0

    # 3. Processa cada registro aplicando a verificação de duplicidade
    for item in pendencias:
        item_id = item['id']
        titulo = item['title']
        
        if pendencias_ja_processadas(item_id):
            print(f"[IGNORADO] ID {item_id} já consta no banco de dados.")
        else:
            print(f"[NOVO] Gravando ID {item_id}: {titulo}")
            salvar_pendencias(item_id, titulo)

            enviar_alerta(f"Nova pendência registrada: {titulo}")
            novos_itens += 1

    print(f"\nFluxo concluído! Total de novos registros gravados: {novos_itens}")

if __name__ == "__main__":
    executar_bot()