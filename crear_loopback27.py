
import requests
from getpass import getpass
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native/interface/"

username = input("Usuario del router: ")
password = getpass("Contrasena: ")

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

payload = {
    "Loopback": [
        {
            "name": 27,
            "description": "SHUTDOWN CCNA DEVNET",
            "ip": {
                "address": {
                    "primary": {
                        "address": "27.1.2.1",
                        "mask": "255.255.255.255"
                    }
                }
            },
            "shutdown": [None]
        }
    ]
}

try:
    response = requests.post(
        url,
        auth=(username, password),
        headers=headers,
        json=payload,
        verify=False,
        timeout=30
    )

    print("Codigo HTTP:", response.status_code)
    print("Respuesta:", response.text)

    if response.status_code in (200, 201, 204):
        print("Loopback 27 creada correctamente")
    else:
        print("Error al crear la interfaz")

except requests.exceptions.RequestException as error:
    print("Error de conexion:", error)
