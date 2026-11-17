import asyncio
from datetime import datetime
from huawei_band.ble_client import BleClient
from huawei_band.config import load_settings

def create_notification_callback(name:str):
    def callback(sender, data):
        time = datetime.now().strftime("%H:%M:%S.%f")[:-3]

        print(f"\n [{time}] {name}")
        print("Hex: ", data.hex(" "))
        print("Bytes: ", list(data))

    return callback


async def run_experiment(name: str, duration: int):
    print(name)
    input("Enter para iniciar")

    await asyncio.sleep(duration)
    print("Experimento terminado")


async def main():
    settings = load_settings()
        
    print("Conectando con Huawei Band 4 Pro")
    try:
        async with BleClient(settings.huawei_address) as client:
            if not client.is_connected:
                print("No se pudo conectar")
                return
            
            print("Conectado correctamente")

            subscribed_characteristics = []

            for name, characteristic_uuid in settings.huawei_notification_characteristics.items():
                if not characteristic_uuid:
                    print(f"{name}: UUID no configurado")
                    continue

                await client.start_notifications(
                    characteristic_uuid,
                    create_notification_callback(name)
                )

                subscribed_characteristics.append(characteristic_uuid)
                print(f"Escuchando {name}")

            await run_experiment(
                "Prueba: cambiando el fondo de pantalla",
                90
            )

            for characteristic_uuid in subscribed_characteristics:
                await client.stop_notifications(characteristic_uuid)

            print("\n Notificaciones detenidas")

    except Exception as error:
        print(f"Error en la conexion -> {error}")


asyncio.run(main())

