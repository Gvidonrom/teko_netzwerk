import socket
import json

# Server-Adresse
HOST = "127.0.0.1"
PORT = 9999
BUFFER = 4096

# UDP-Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Pong Server läuft auf {HOST}:{PORT}")

while True:
    # Daten vom Client empfangen
    data, client_addr = sock.recvfrom(BUFFER)

    try:
        message = json.loads(data.decode())
        seq = message["seq"]     # eindeutige Nachrichten-ID
        spin = int(message["spin"])
    except Exception as e:
        print("Fehler beim Verarbeiten der Nachricht:", e)
        continue

    print(f"[SERVER] Empfangen: seq={seq}, spin={spin} von {client_addr}")

    # Antwort vorbereiten (spin + 1)
    response = {
        "seq": seq,
        "spin": spin + 1
    }

    # Antwort an den Client senden
    sock.sendto(json.dumps(response).encode(), client_addr)

    print(f"[SERVER] Gesendet: seq={seq}, spin={spin + 1}")
