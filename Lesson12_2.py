import socket
import asyncio
import json

async def plus(a, b):
    print('plus started work')
    await asyncio.sleep(1)
    c = a + b
    print('plus finished work')
    return c

async def minus(a, b):
    print('minus started work')
    await asyncio.sleep(2)
    c = a - b
    print('minus finished work')
    return c

async def multiply(a, b):
    print('multiply started work')
    await asyncio.sleep(3)
    c = a * b
    print('multiply finished work')
    return c

async def handle_connection(conn):
    print('connected:', addr)
    data = conn.recv(1024).decode()
    parsed_data = json.loads(data)
    a = float(parsed_data["a"])
    b = float(parsed_data["b"])
    print(a, b)
    result = {
        "a+b": await plus(a, b),
        "a-b": await minus(a, b),
        "a*b": await multiply(a, b)
    }
    response = json.dumps(result)
    conn.send(response.encode())
    conn.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    asyncio.run(handle_connection(conn))
