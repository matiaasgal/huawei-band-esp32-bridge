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
            for name, characteristic_uuid in (settings.huawei_device_info_characteristics.items()):
                if not characteristic_uuid:
                    print(f"{name}: UUID no configurado")
                    continue

                try:
                    datos = await client.read_characteristic(characteristic_uuid)
                    
                    try:
                        valor = datos.decode("utf-8").strip()
                    except UnicodeDecodeError:
                        valor = datos.hex(" ")

                    print(f"{name}: {valor}")

                except Exception as error:
                    print(f"Error al leer {name} -> {error}")

    except Exception as error:
        print(f"Error en la conexion -> {error}")


asyncio.run(main())


