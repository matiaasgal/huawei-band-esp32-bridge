import asyncio
from huawei_band.ble_client import BleClient
from huawei_band.config import load_settings

async def main():
    settings = load_settings()
    
    print("Conectando con Huawei Band 4 Pro")
    try:
        async with BleClient(settings.huawei_address) as client:
            if not client.is_connected:
                print("No se pudo conectar")
                return

            print("Conectado correctamente")
            for service in client.services:
                print(f"\n UUID del servicio: {service.uuid}")
                print(f"Descripcion: {service.description}")

                for characteristic in service.characteristics:
                    print(f"Caracteristica: {characteristic.uuid}")
                    print(f"Propiedades: {characteristic.properties}")
                    print(f"Descripcion: {characteristic.description}")

                    for descriptior in characteristic.descriptors:
                        print(f"Descriptor: {descriptior.uuid}")
    
    except Exception as error:
        print(f"Error en la conexion -> {error}")


asyncio.run(main())