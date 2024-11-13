Reverse Shell Client-Server
This repository contains a reverse shell client-server program designed for ethical security testing and research. It allows a server to establish a remote command-line session with a connected client.

Warning: This tool is intended for use only on systems where you have explicit authorization. Unauthorized access to any network or device is illegal and punishable by law. This tool should only be used for ethical hacking or cybersecurity training on systems you own or have permission to test.

Features
Command Execution: Remotely execute shell commands on the client machine and retrieve the output.
Cross-Platform Compatibility: Works on Linux, Windows, and macOS with Python installed.
Customizable Connection: Easily change the IP and port settings for different network environments.
Prerequisites
Python 3.x: Ensure Python 3.x is installed on both the client and server machines.
Networking Knowledge: A basic understanding of TCP/IP networking and firewalls is recommended.
Installation
Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/ReesTheBeast/reverse-shell-client-server.git
cd reverse-shell-client-server
Configure Server and Client

Update the IP address and port settings as needed in the start_listener (server) and connect_to_server (client) functions.
Install Required Libraries
Install any dependencies with:

pip install colormath
Usage
Step 1: Start the Server
Run the server to start listening for incoming connections:

python server.py
The server will output a message when a client connects.
Step 2: Start the Client
On the client machine, run:

python client.py
The client will attempt to connect to the server. Upon a successful connection, the server can begin sending commands.

Step 3: Execute Commands
The server prompts you to enter commands. Enter any shell command (e.g., ls, whoami, ipconfig) and press Enter.
The client will execute the command and send the output back to the server.
Step 4: Close the Connection
To close the connection, type exit or quit on the server-side. This will terminate the session.
Example Commands
Here are some example commands to try:


ls           # Lists files in the current directory
whoami       # Prints the username on the client machine
systeminfo   # (Windows) Shows system information
uname -a     # (Linux/macOS) Prints system information
Security Considerations
Restricted Environments: Run in secure, authorized environments to prevent unauthorized access.
Firewall Settings: Ensure ports are securely configured to avoid unauthorized external access.
Legal Compliance: Use only on systems you own or have explicit permission to test.
Troubleshooting
Connection Errors: Double-check the IP address, port number, and firewall settings if the client cannot connect to the server.
Command Execution Issues: Some commands may not execute if permissions or environment settings differ.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Developed by ReesTheBeast
