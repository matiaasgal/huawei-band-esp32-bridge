import asyncio
from collections.abc import Callable
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic

NotificationCallback = Callable[
    [BleakGATTCharacteristic, bytearray],
    None
]

class BleClient:
    def __init__(self, address: str, timeout: float = 20.0) -> None:
        self._client = BleakClient(address, timeout=timeout)

    @property
    def is_connected(self) -> bool:
        return self._client.is_connected

    @property
    def services(self):
        return self._client.services

    async def __aenter__(self) -> "BleClient":
        await self._client.connect()
        return self

    async def __aexit__(self, exception_type, exception, traceback) -> None:
        await self._client.disconnect()

    async def read_characteristic(self, characteristic_uuid: str) -> bytearray:
        return await self._client.read_gatt_char(characteristic_uuid)

    async def write_characteristic(
            self,
            characteristic_uuid: str,
            data: bytes,
            response: bool = True
    ) -> None:
        await self._client.write_gatt_char(
            characteristic_uuid,
            data,
            response=response
        )

    async def start_notifications(
        self,
        characteristic_uuid: str,
        callback: NotificationCallback
    ) -> None:
        await self._client.start_notify(
            characteristic_uuid,
            callback
        )

    async def stop_notifications(self, characteristic_uuid: str) -> None:
        await self._client.stop_notify(characteristic_uuid)