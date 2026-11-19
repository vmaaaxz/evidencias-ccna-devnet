from ncclient import manager
from getpass import getpass

host = "192.168.56.102"
username = input("Usuario del router: ")
password = getpass("Contrasena: ")

config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>38</name>
                <description>CCNA DEVNET 2026</description>
                <ip>
                    <address>
                        <primary>
                            <address>38.20.2.1</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
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

        print("Loopback 38 creada:", resultado.ok)
        print(resultado.xml)

except Exception as error:
    print("Error:", error)
