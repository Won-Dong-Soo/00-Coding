import serial

ser = serial.Serial(
    port='/dev/cu.usbserial-1110',  # 네 환경
    baudrate=115200,
    timeout=1
)

while True:
    line = ser.readline().decode().strip()
    if line == "":
        continue
    value = int(line)
    ser.write(f"{value}\n ".encode())