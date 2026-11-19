from ncclient import manager
from getpass import getpass

host = "192.168.56.102"
username = input("Usuario del router: ")
password = getpass("Contraseña: ")

try:
    with manager.connect(
        host=host,
        port=830,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={"name": "csr"},
        timeout=30
    ) as connection:

        print("Conexion NETCONF exitosa")
        print("Session ID:", connection.session_id)

except Exception as error:
    print("Error de conexion:", error)
