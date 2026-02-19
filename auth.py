import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Permiso para gestionar contactos
SCOPES = ['https://www.googleapis.com/auth/contacts']

def autenticar():
    creds = None

    # Si ya existe token guardado
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Si no hay credenciales válidas
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardar token para futuras ejecuciones
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    print("Autenticación exitosa")
    return creds

if __name__ == '__main__':
    autenticar()
