import asyncio
from bleak import BleakScanner

from huawei_band.ble_client import BleClient
from huawei_band.config import load_settings

def receive_response(sender, data):
    message = data.decode("utf-8", errors="replace")
    print(f"Respuesta recibida -> {message}")


async def find_esp32(device_name: str):
    print("Buscando ESP32")
    devices = await BleakScanner.discover(timeout=10)

    for device in devices:
        if device.name == device_name:
            return device
    return None


async def main():
    settings = load_settings()

    esp32 = await find_esp32(settings.esp32_name)

    if esp32 is None:
        print("No se encontro el dispositivo")
        return

    print("Dispositivo encontrado: ", esp32.name)
    try:
        async with BleClient(esp32.address) as client:
            if not client.is_connected:
                print("No se pudo conectar")
                return
            
            print("Conectado correctamente")

            await client.start_notifications(
                settings.esp32_characteristic_uuid,
                receive_response
            )

            try:
               initial_value = await client.read_characteristic(
                   settings.esp32_characteristic_uuid
               )

               print(f"Valor inicial: ", initial_value.decode("utf-8", errors="replace"))
               
               message = "HOLA ESP32"
               print(f"Enviando mensaje: {message}")

               await client.write_characteristic(
                   settings.esp32_characteristic_uuid,
                   message.encode("utf-8")
               )

               await asyncio.sleep(2)
            
            finally:
               await client.stop_notifications(
                   settings.esp32_characteristic_uuid
               )

               print("Notificaciones detenidas")

    except Exception as error:
        print(f"Error en la conexion -> {error}")

asyncio.run(main())
