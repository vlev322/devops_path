@dataclass
class DmiInfo:
    board_name: str
    product_name: str
    vendor: str
    
@dataclass
class HardwareInventory:
    mac_addresses: list[MacEntry]        # назва інтерфейсу → MAC
    storage_devices: list[StorageEntry]  # тип пристрою (SATA/NVMe), модель, розмір, серійний номер
    dmi: DmiInfo                         # board_name, product_name, vendor, serial, uuid