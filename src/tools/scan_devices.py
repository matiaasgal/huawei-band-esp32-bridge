import asyncio
from bleak import BleakScanner

async def main():

    # devices será una lista de los dispositivos BLE escaneados luego de 15 segundos
    devices = await BleakScanner.discover(
        timeout=15, return_adv=True
    )

    # imprime informacion de los dispositivos escaneados
    for address, (device, adv) in devices.items():
        print("\n Nombre: ", device.name)
        print("Direccion: ", device.address)
        print("RSSI: ", adv.rssi)
        print("Servicios: ", adv.service_uuids)
        print("Datos: ", adv.manufacturer_data)

asyncio.run(main())