# Ping-Pong UDP Protocol (Python)

## Beschreibung

Dieses Projekt implementiert einen einfachen Ping-Pong-Protokollservice
auf Basis von UDP in Python.

Ein Client (Ping) sendet eine Zahl `n` (spin) an den Server.
Der Server (Pong) antwortet mit `n + 1`.

Das Projekt wurde im Rahmen des Moduls *Netzwerk / Programmierung*
erstellt und dient dem Verständnis von:
- UDP-Sockets
- Client-Server-Kommunikation
- einfachen Protokollen auf Anwendungsebene

---

## Projektstruktur

Ping-pong/
└── PythonApplication1/
├── base_udp_server.py # UDP Pong Server
├── base_udp_client.py # UDP Ping Client
└── PythonApplication1.pyproj

---

## Voraussetzungen

- Python 3.8 oder höher
- Windows / Linux / macOS
- Keine externen Bibliotheken erforderlich

---

## Starten des Servers

Im Terminal (PowerShell oder Bash):

```bash
python base_udp_server.py

Der Server lauscht auf:
127.0.0.1:9999

Starten des Clients

In einem zweiten Terminal:
python base_udp_client.py

Beispielausgabe:
[CLIENT] Senden: seq=..., spin=10
[CLIENT] Antwort erhalten: {'seq': '...', 'spin': 11}

Implementierte Funktionalität
	UDP-basierter Ping-Pong Dienst
	JSON-basierte Nachrichten
	Eindeutige Nachrichten-ID (UUID)
	Timeout-Behandlung im Client

Autor
Roman Nemchenko
GitHub: https://github.com/Gvidonrom/teko_netzwerk