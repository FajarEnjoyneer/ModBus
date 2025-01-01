from pymodbus.client import ModbusSerialClient

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
    print("Connected to Modbus Slave")
    
    # Membaca 10 holding register mulai dari alamat 0 untuk Slave ID 1
    result = client.read_holding_registers(address=32, count=10, slave=1)
    
    if result.isError():
        print(f"Error: {result}")
    else:
        print(f"Registers: {result.registers}")
    
    client.close()
else:
    print("Failed to connect to Modbus Slave")
