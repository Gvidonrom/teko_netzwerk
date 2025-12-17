import socket
import json
import uuid

# Server-Adresse
SERVER = ("127.0.0.1", 9999)

# UDP-Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2.0)   # Timeout für Antwort

def ping(spin):
    # Einzigartige Nachrichten-ID generieren
    seq = str(uuid.uuid4())

    # Nachricht erstellen
    message = {
        "seq": seq,
        "spin": spin
    }

    data = json.dumps(message).encode()

    print(f"[CLIENT] Senden: seq={seq}, spin={spin}")

    # Nachricht an den Server senden
    sock.sendto(data, SERVER)

    # Antwort empfangen
    try:
        response_data, addr = sock.recvfrom(4096)
    except socket.timeout:
        print("[CLIENT] Timeout: Keine Antwort vom Server")
        return None

    response = json.loads(response_data.decode())

    print(f"[CLIENT] Antwort erhalten: {response}")

    return response


if __name__ == "__main__":
    result = ping(10)
    print("Ergebnis:", result)
