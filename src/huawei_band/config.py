import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    huawei_address: str
    esp32_name: str
    esp32_service_uuid: str
    esp32_characteristic_uuid: str
    huawei_device_info_characteristics: dict[str, str]
    huawei_notification_characteristics: dict[str, str]



def load_settings() -> Settings:
    required = {
        "HUAWEI_BAND_ADDRESS": os.getenv("HUAWEI_BAND_ADDRESS"),
        "ESP32_DEVICE_NAME": os.getenv("ESP32_DEVICE_NAME"),
        "ESP32_CHARACTERISTIC_UUID": os.getenv("ESP32_CHARACTERISTIC_UUID"),
        "ESP32_SERVICE_UUID": os.getenv("ESP32_SERVICE_UUID"),
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise ValueError(
            "Faltan variables de entorno: " + ", ".join(missing)
        )

    device_info_characteristics = {
        "manufacturer": os.getenv("HUAWEI_BAND_DEVICE_INFO_MANUFACTURER_UUID", ""),
        "system_id": os.getenv("HUAWEI_BAND_DEVICE_INFO_SYSTEM_ID_UUID", ""),
        "model": os.getenv("HUAWEI_BAND_DEVICE_INFO_MODEL_NUMBER_UUID", ""),
        "serial_number": os.getenv("HUAWEI_BAND_DEVICE_INFO_SERIAL_NUMBER_UUID", ""),
        "firmware": os.getenv("HUAWEI_BAND_DEVICE_INFO_FIRMWARE_REVISION_UUID", ""),
        "hardware": os.getenv("HUAWEI_BAND_DEVICE_INFO_HARDWARE_REVISION_UUID", ""),
        "software": os.getenv("HUAWEI_BAND_DEVICE_INFO_SOFTWARE_REVISION_UUID", "")
    }

    notification_characteristics = {
        "fe02": os.getenv("HUAWEI_BAND_NOTIFICATION_FE02_UUID",""),
        "fe04": os.getenv("HUAWEI_BAND_NOTIFICATION_FE04_UUID",""),
    }

    return Settings(
        huawei_address=required["HUAWEI_BAND_ADDRESS"],
        esp32_name=required["ESP32_DEVICE_NAME"],
        esp32_service_uuid=required["ESP32_SERVICE_UUID"],
        esp32_characteristic_uuid=required["ESP32_CHARACTERISTIC_UUID"],
        huawei_device_info_characteristics=device_info_characteristics,
        huawei_notification_characteristics=notification_characteristics,
    )