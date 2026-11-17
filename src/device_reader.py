import asyncio, os
from bleak import BleakClient
from dotenv import load_dotenv

load_dotenv()

DIRECCION = os.getenv("DIRECCION")

CARACTERISTICAS = {
    "fabricante": os.getenv("SERV1_FABRICANTE"),
    "id del sistema": os.getenv("SERV1_ID_SISTEMA"),
    "modelo": os.getenv("SERV1_MODELO"),
    "numero de serie": os.getenv("SERV1_NUMERO_SERIE"),
    "firmware": os.getenv("SERV1_FIRMWARE"),
    "hardware": os.getenv("SERV1_HARDWARE"),
    "software": os.getenv("SERV1_SOFTWARE")
}

async def main():
    print("conectando con huawei band 4 pro")
    try:
        async with BleakClient(DIRECCION, timeout=20) as client:
            if client.is_connected:
                print("si se pudo conectar")

                for clave, valor in CARACTERISTICAS.items():
                    try:
                        datos = await client.read_gatt_char(valor)
                        try:
                            valor = datos.decode("utf-8").strip()
                        except UnicodeDecodeError:
                            valor = datos.hex(" ")

                        print(clave + ": ", valor)
                    except Exception as error:
                        print("error al leer los datos -> ", error)

    except Exception as error:
        print("error en la conexion -> ", error)


asyncio.run(main())


