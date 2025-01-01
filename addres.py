from pymodbus.client import ModbusSerialClient
import logging

# Fungsi untuk memindai alamat register pada slave tertentu
def scan_registers(client, slave_id, address_range=(0, 100)):
    for address in range(address_range[0], address_range[1] + 1):
        print(f"Scanning address {address} for Slave ID {slave_id}...")
        try:
            # Cobalah untuk membaca 1 Holding Register dari alamat yang dicoba
            result = client.read_holding_registers(address=address, count=1, slave=slave_id)
            if result.isError():
                print(f"Address {address}: No response or error.")
            else:
                print(f"Address {address}: Holding Register Value: {result.registers[0]}")
        except Exception as e:
            print(f"Error reading address {address}: {str(e)}")

# Mengaktifkan logging untuk debugging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Konfigurasi Modbus RTU
client = ModbusSerialClient(
    port='/dev/ttyUSB0',   # Gantilah dengan port serial yang sesuai
    baudrate=9600,         # Baudrate
    parity='N',            # Parity (N = None, E = Even, O = Odd)
    stopbits=1,            # Stop bits
    bytesize=8,            # Data bits
    timeout=3              # Timeout (detik)
)

# Koneksi ke perangkat Modbus
if client.connect():
    print("Connected to Modbus Master. Scanning registers for Slave ID 4...")
    scan_registers(client, slave_id=1, address_range=(0, 100))  # Memindai alamat register dari 0 hingga 100
    client.close()
else:
    print("Failed to connect to Modbus Slave")
