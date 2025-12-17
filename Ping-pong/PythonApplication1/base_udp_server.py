import socket
import json

HOST = "127.0.0.1"
PORT = 9999
BUFFER_SIZE = 4096

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Pong Server läuft auf {HOST}:{PORT}")

while True:
    data, client_address = sock.recvfrom(BUFFER_SIZE)

    try:
        message = json.loads(data.decode())
        seq = message["seq"]
        spin = int(message["spin"])
    except Exception as e:
        print("Fehlerhafte Nachricht:", e)
        continue

    print(f"[SERVER] Empfangen: seq={seq}, spin={spin}")

    response = {
        "seq": seq,
        "spin": spin + 1
    }

    sock.sendto(json.dumps(response).encode(), client_address)
    print(f"[SERVER] Gesendet: seq={seq}, spin={spin + 1}")

