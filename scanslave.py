from pymodbus.client import ModbusSerialClient

# Fungsi untuk mencoba semua Slave ID dari 1 hingga 247
def scan_slave_ids(client, address_range=(1, 247)):
    for slave_id in range(address_range[0], address_range[1] + 1):
        print(f"Scanning Slave ID: {slave_id}...")
        try:
            # Cobalah untuk membaca 1 Holding Register dari Slave ID yang dicoba
            result = client.read_holding_registers(address=0, count=1, slave=slave_id)
            if result.isError():
                print(f"Slave ID {slave_id} not responding.")
            else:
                print(f"Slave ID {slave_id} is responding!")
                print(f"Holding Register Value: {result.registers[0]}")
        except Exception as e:
            print(f"Error for Slave ID {slave_id}: {str(e)}")

# Konfigurasi Modbus RTU
client = ModbusSerialClient(
    port='/dev/ttyUSB0',   # Port serial
    baudrate=9600,         # Baudrate
    parity='N',            # Parity (N = None, E = Even, O = Odd)
    stopbits=1,            # Stop bits
    bytesize=8,            # Data bits
    timeout=1              # Timeout (detik)
)

# Koneksi ke perangkat
if client.connect():
    print("Connected to Modbus Master. Scanning for Slave IDs...")
    scan_slave_ids(client)  # Memulai scan slave ID
    client.close()
else:
    print("Failed to connect to Modbus Master")
