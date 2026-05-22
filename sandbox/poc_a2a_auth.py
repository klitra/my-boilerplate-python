import os
import requests
from dotenv import load_dotenv

# 1. SEGURANÇA: Carrega as variáveis da pasta instance/
# (O caminho sobe uma pasta com '../' pois estamos dentro de sandbox/)
load_dotenv(dotenv_path="../instance/.env")

CLIENT_ID = os.getenv("A2A_CLIENT_ID")
CLIENT_SECRET = os.getenv("A2A_CLIENT_SECRET")

# URLs fictícias para a PoC (Substitua pelas URLs do sistema alvo)
TOKEN_URL = "https://api.sistema-alvo.com/oauth2/token"
API_URL = "https://api.sistema-alvo.com/v1/identities" 

def get_a2a_token():
    """Realiza a autenticação A2A via Client Credentials e retorna o Bearer Token."""
    print("🔄 Iniciando autenticação A2A...")
    
    # O padrão OAuth2 A2A geralmente pede os dados em formato form-urlencoded
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    
    try:
        response = requests.post(TOKEN_URL, data=payload)
        response.raise_for_status() # Força um erro se o status HTTP não for 200-299
        
        token_data = response.json()
        print("✅ Token adquirido com sucesso!")
        return token_data.get("access_token")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Falha ao obter o token: {e}")
        if response is not None:
            print(f"Detalhes do erro: {response.text}")
        return None

def fetch_data(token):
    """Usa o token para buscar uma informação opcional na API."""
    print("\n🔄 Consultando a API com o Token adquirido...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        # Fazendo um request GET para trazer informações
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        
        dados = response.json()
        print("✅ Dados retornados com sucesso:")
        print(dados)
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Falha ao consultar a API: {e}")
        if response is not None:
            print(f"Detalhes da API: {response.text}")

if __name__ == "__main__":
    # Verifica se as credenciais foram carregadas corretamente
    if not CLIENT_ID or not CLIENT_SECRET:
        print("⚠️ ERRO: Credenciais não encontradas. Verifique o arquivo instance/.env")
    else:
        # Fluxo de execução
        access_token = get_a2a_token()
        
        if access_token:
            # Se conseguiu o token, faz a requisição de dados
            fetch_data(access_token)
