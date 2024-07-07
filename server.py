import socket

def start_server():
    host = '0.0.0.0'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("Server is listening...")
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    buffer = b''  # 버퍼 초기화

    while True:
        data = conn.recv(1024)
        if not data:
            break
        buffer += data

    result = buffer.decode('utf-8', errors='ignore')  # 받은 데이터를 문자열로 변환
    print("Received result: ", result)

    conn.close()
    s.close()

try:
    start_server()
except KeyboardInterrupt:
    print("Server stopped by User")
