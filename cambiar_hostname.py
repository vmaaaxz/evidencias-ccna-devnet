
from ncclient import manager
from getpass import getpass

host = "192.168.56.102"
username = input("Usuario del router: ")
password = getpass("Contrasena: ")

config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>ARRATIAMAXIMILIANO</hostname>
    </native>
</config>
"""

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

        resultado = connection.edit_config(
            target="running",
            config=config
        )

        print("Cambio aplicado:", resultado.ok)

except Exception as error:
    print("Error:", error)
