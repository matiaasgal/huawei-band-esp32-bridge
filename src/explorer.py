import asyncio
from bleak import BleakClient

DIRECCION = "F717EA77-4EE7-5A20-CA65-6C82CF98F629"

async def main():
    print("conectando con huawei band 4 pro")
    try:
        async with BleakClient(DIRECCION, timeout=20) as client:
            if client.is_connected:
                print("si se pudo conectar")

                for service in client.services:
                    print("\n servicio ", service.uuid)
                    print("descripcion ", service.description)

                    for characteristic in service.characteristics:
                        print("caracteristica ", characteristic.uuid)
                        print("propiedades ", characteristic.properties)
                        print("descripcion ", characteristic.description)

                        for descriptior in characteristic.descriptors:
                            print("descriptor ", descriptior.uuid)

    except Exception as error:
        print("error en la conexion -> ", error)


asyncio.run(main())