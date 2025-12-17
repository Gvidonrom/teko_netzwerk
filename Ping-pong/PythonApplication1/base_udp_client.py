import socket
import json
import uuid

SERVER_ADDRESS = ("127.0.0.1", 9999)
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2.0)

def ping(spin: int):
    seq = str(uuid.uuid4())

    message = {
        "seq": seq,
        "spin": spin
    }

    data = json.dumps(message).encode()

    print(f"[CLIENT] Senden: seq={seq}, spin={spin}")
    sock.sendto(data, SERVER_ADDRESS)

    try:
        response_data, _ = sock.recvfrom(BUFFER_SIZE)
    except socket.timeout:
        print("[CLIENT] Timeout: keine Antwort vom Server")
        return None
    except ConnectionResetError:
        print("[CLIENT] WinError 10054: Server nicht erreichbar")
        return None

    response = json.loads(response_data.decode())
    print(f"[CLIENT] Antwort erhalten: {response}")
    return response


if __name__ == "__main__":
    result = ping(10)
    print("Ergebnis:", result)

