import socket
import json

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 55000))

        a, b = input().split()
        data = {'a': a, 'b': b}
        serialized_data = json.dumps(data).encode('utf-8')
        sock.send(serialized_data)

        received_data = sock.recv(1024)
        decoded_data = received_data.decode('utf-8')
        result = json.loads(decoded_data)
        print("a+b=",result["a+b"],"a-b=",result["a-b"],"a*b=",result["a*b"])

        sock.close()
    except Exception as e:
        print("Error:", e)

