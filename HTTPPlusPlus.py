# Copyright (C) 2022 Justin Marwad. All rights reserved.

import sys, socket, threading, logging, time
from colorama import Fore #GREY, YELLOW, GREEN, RED, BLUE, RESET

class HTTPPlusPlus:
    def __init__(self, host=sys.argv[1], port=sys.argv[2], type_file=sys.argv[3], filename=sys.argv[4]):
        logging.basicConfig(filename="HTTPPlusPlus.log", format="%(asctime)s: %(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")
        
        self.host = host
        self.port = int(port)
        self.type = type_file
        self.file = filename                    

        self.sock = socket.socket()    

    def result(self, text, color=Fore.BLACK): 
        """ Base method. Pretty print out results to terminal. """
        print(f"{color} {text} {Fore.RESET}")
        logging.info(text) 
    

    def listen(self, conns=10): 
        """ Run the server. """

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.host, self.port))
            sock.listen(conns)

            while True:
                try:
                    conn, addr = sock.accept()
                    self.result(f"[*] SERVER INFO - New connection from {conn} on port {addr}", Fore.BLUE)
                    data = conn.recv(1024).decode()

                    self.result(f"[+] SERVER INFO - Data received: {repr(data)}", Fore.BLUE)

                    if "PUT" in repr(data):
                        self.result(f"[+] SERVER INFO - PUT mode selected", Fore.BLUE)

                        with open("recv" + self.file, "wb") as writer:
                            while True:
                                recv = conn.recv(1024)
                                if "GET_DONE_STATUS" in recv.decode(): 
                                    break
                            
                                writer.write(recv)

                        self.result(f"[+] SERVER INFO - File written", Fore.BLUE)
                        conn.sendall(b"HTTP/1.0 200 OK File Created")

                    elif "GET" in repr(data):
                        self.result(f"[+] SERVER INFO - GET mode selected", Fore.BLUE)
                        conn.sendall(b"HTTP/1.0 200 OK\n\n Hello World!")

                    self.result("[*] SERVER INFO - Closing connection", Fore.BLUE)
                    conn.close()
                
                except Exception as E:
                    self.result(f"[-] Error: {E}", Fore.RED)

    def connect(self):
        """ Connect to the server via a connection-orieted socket. """ 
        self.result(f"[*] INFO: Client connecting to {self.host}:{self.port}...", Fore.YELLOW)
        
        # Submit a valid HTTP/1.0 GET request for the supplied URL.  ```GET /index.html HTTP/1.0``` (end with extra CR/LF) 
        if self.type == "GET":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: 
                sock.connect((self.host, self.port))
                sock.sendall(str.encode(f"GET /{self.file} HTTP/1.0\r\nHost: {self.host}\r\n\r\n"))

                response=""
                while True:
                    recv = sock.recv(1024)
                    if recv==b'':
                        break
                    
                    try: 
                        response += recv.decode()
                    except UnicodeDecodeError:
                        self.result("[-] Client UnicodeDecodeError: Page did not respond with valid information.", Fore.RED)

        elif self.type == "PUT":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: 
                sock.connect((self.host, self.port))
                sock.sendall(str.encode(f"PUT /{self.file} HTTP/1.0\r\nHost: {self.host}\r\n\r\n"))

                with open(self.file, "rb") as file_data:
                    send_data = file_data.read(1024)
                    while send_data:
                        sock.sendall(send_data)
                        self.result(f"[*] CLIENT INFO: Sending {repr(send_data)}", Fore.YELLOW)
                        send_data = file_data.read(1024)

                sock.send(b"GET_DONE_STATUS")

                response=""
                while True:
                    recv = sock.recv(1024)
                    if recv == b'':
                        break

                    response += recv.decode()

        else: 
            self.result("[-] CLIENT ERROR - Invalid HTTP type", Fore.RED)
        
        self.result(f"[+] Client - Response recieved: {response}", Fore.YELLOW)

if __name__ == "__main__": 
    server = HTTPPlusPlus(host="127.0.0.1", port=8080)
    client = HTTPPlusPlus()

    server_thread = threading.Thread(target=server.listen)
    client_thread = threading.Thread(target=client.connect)

    server_thread.start()
    client_thread.start()
