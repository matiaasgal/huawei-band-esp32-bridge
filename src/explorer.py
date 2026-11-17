import asyncio, os
from bleak import BleakClient
from dotenv import load_dotenv

load_dotenv()

DIRECCION = os.getenv("DIRECCION")

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