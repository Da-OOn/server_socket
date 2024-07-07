import socket
import subprocess
def get_results_from_script():
    # 'main_cache.py' 스크립트 실행
    result = subprocess.run(['python3', 'main_cache.py'], capture_output=True, text=True)
    # output = result.stdout.strip()  # 결과를 문자열로 변환 및 공백 제거
    return result
def send_data():
    host = '192.168.0.3'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    try:
        result = get_results_from_script()
        s.sendall(result.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()
try:
    send_data()
except KeyboardInterrupt:
    print("Stopped by User")
