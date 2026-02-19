from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/contacts']

def probar_api():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    service = build('people', 'v1', credentials=creds)

    resultados = service.people().connections().list(
        resourceName='people/me',
        pageSize=5,
        personFields='names,phoneNumbers'
    ).execute()

    conexiones = resultados.get('connections', [])

    if not conexiones:
        print("No se encontraron contactos.")
    else:
        print("Contactos encontrados:\n")
        for persona in conexiones:
            nombre = persona.get('names', [{}])[0].get('givenName', 'Sin nombre')
            telefonos = persona.get('phoneNumbers', [])
            print(f"Nombre: {nombre}")
            for tel in telefonos:
                print(f" - {tel.get('value')}")
            print("------")

if __name__ == "__main__":
    probar_api()
