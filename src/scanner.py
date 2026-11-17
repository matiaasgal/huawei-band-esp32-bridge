import asyncio
from bleak import BleakScanner

async def main():
    print("buscando dispositivos \n")
    devices = await BleakScanner.discover(
        timeout=15, return_adv=True
    )

    for address, (device, adv) in devices.items():
        print("nombre: ", device.name)
        print("direccion: ", device.address)
        print("rssi: ", adv.rssi)
        print("servicios: ", adv.service_uuids)
        print("datos: ", adv.manufacturer_data)

asyncio.run(main())