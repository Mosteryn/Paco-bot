import requests

# Define tus credenciales
CLIENT_ID = '521644868'
TOKEN = 'fivq2qq19j0os0vrs4uay9d8dm4rsa'

# Define los headers para la solicitud
headers = {
    'Client-ID': CLIENT_ID,
    'Authorization': f"Bearer {TOKEN}",
}

# Define el nuevo título
nuevo_titulo = "Mi nuevo título"

# Realiza la solicitud para actualizar el título
response = requests.patch('https://api.twitch.tv/helix/channels', headers=headers, data={'title': nuevo_titulo})

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Título actualizado con éxito")
else:
    print(f"Error al actualizar el título: {response.content}")