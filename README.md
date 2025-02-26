# 🔐 Secure Network  
*A powerful and flexible networking extension for Python with built-in authentication, encryption, and HMAC security.*

---

## 🚀 Features  
✅ **Secure authentication** with `bcrypt` and Multi-Factor Authentication (MFA).  
✅ **Encrypted communication** using HMAC verification.  
✅ **Rate-limiting** to prevent brute force attacks.  
✅ **Event-driven architecture** for handling network interactions.  
✅ **Supports both authenticated and unauthenticated connections.**  

---

## 📦 Installation  
Install Secure Network via PyPI:  
```bash
pip install secure_network
```

## ⚡ Quick Start

### 1️⃣ Secure Authentication Server & Client

For authenticated connections, use the SERVER and CLIENT classes:
```python
import secure_network

# 🔹 Initialize the server
server = secure_network.SERVER(
    key=None, hmac_key=None, 
    address=("0.0.0.0", 12345), 
    on_event=lambda event: print(event), 
    max_clients=10
)

# 🔹 Set the accounts file (default: accounts.json)
server.accounts_file = "accounts.json"

# 🔹 Create user accounts
server.create_account("admin", "adminpass", role="admin")
server.create_account("user", "userpass", role="user", mfa_method="email", contact="user@example.com")

# 🔹 Initialize client
client = secure_network.CLIENT(
    key=None, hmac_key=None, 
    address=("127.0.0.1", 12345), 
    on_event=lambda event: print(event)
)

# 🚀 Start server and client
server.init()
client.init()
```

### 2️⃣ Basic Server & Client (Without Authentication)

If authentication isn't needed, use the Server and Client classes directly:
```python
import secure_network

# 🔹 Initialize server
server = secure_network.Server(
    key=None, hmac_key=None, 
    address=("0.0.0.0", 12345), 
    on_event=lambda event: print(event), 
    max_clients=10
)

# 🔹 Initialize client
client = secure_network.Client(
    key=None, hmac_key=None, 
    address=("127.0.0.1", 12345), 
    on_event=lambda event: print(event)
)

# 🚀 Start server and client
server.init()
client.init()
```

## 🎯 Handling Events

Events provide real-time feedback about network status. You can handle them like this:
```python
import secure_network

def on_event(event: secure_network.Event):
    if event.type == secure_network.EventType.CONNECTION_REQUEST:
        event.accept()  # ✅ Accept connection
    elif event.type == secure_network.EventType.CONNECTION_SUCCESS:
        print(f"✅ Client connected: {event.data['address']}")
    elif event.type == secure_network.EventType.RECEIVED:
        print(f"📩 Received data: {event.data['data']}")
    else:
        print(f"ℹ️ Event: {event.type.id} - {event.type.description}")

# Generate secure keys
KEY, HMAC_KEY = secure_network.generate_key(), secure_network.generate_hmac_key() 

# Create server
server = secure_network.Server(
    key=KEY, hmac_key=HMAC_KEY, 
    address=("0.0.0.0", 12345), 
    on_event=on_event, 
    max_clients=10
)

# 🚀 Start server
server.init()

# Keep server running
while server.active:
    pass
```

## 🔥 Event Types

Secure Network provides several event types for handling different network interactions:

| **Event Type**            | **Description**                                      | **Data Fields**                |
|---------------------------|------------------------------------------------------|--------------------------------|
| `CONNECTION_REQUEST`      | Someone is trying to connect                        | `{address, connection}` (can accept/reject) |
| `CONNECTION_SUCCESS`      | A client has successfully connected                 | `{address, connection}`        |
| `CONNECTED`               | The client/server has started communication         | `{}`                           |
| `DISCONNECTED`            | A client/server has disconnected                    | `{}`                           |
| `RECEIVED`                | Data received from a device                         | `{address, connection, data}`  |
| `THREAD_WARNING`          | A thread did not behave as expected                 | `{thread}`                     |
| `ERROR`                   | An error occurred                                  | `{exception}`                   |


# ℹ️ Additional Information

- *event.data* contains event-specific details (e.g., client address, message data).
- *event.accept()* and *event.reject()* can be used for *CONNECTION_REQUEST* events.
- Addresses and connections appear only on the server side (clients do not see them).

# 📜 License
This project is licensed under the MIT License.

# ⭐ Like This Project?
If you find this useful, consider starring it on GitHub and contributing to its development! 🚀
