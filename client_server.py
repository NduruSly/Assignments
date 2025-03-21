import socket
import threading
import time

def run_server():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is running...")
        try:
            conn, addr = s.accept()
            with conn:
                conn.sendall(b"Hello from server!")
                print(f"Server sent message to {addr}")
        except Exception as e:
            print(f"Server error: {e}")

def run_client():
    HOST = '127.0.0.1'
    PORT = 65432

    time.sleep(0.5)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            print("Client received:", data.decode())
    except ConnectionRefusedError:
        print("Client could not connect to server.")

if __name__ == "__main__":

    server_thread = threading.Thread(target=run_server)
    server_thread.start()


    run_client()


    server_thread.join()
    print("Program completed.")