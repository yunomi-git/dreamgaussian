#!/usr/bin/env python

# import asyncio
# import websockets
# import subprocess
#
# async def server(websocket):
#     command = await websocket.recv()
#     print(f'Executing command \'{command}\'')
#     (exit_code, output) = subprocess.getstatusoutput(command)
#     if len(output.strip()) > 0:
#         print(output, flush=True)
#     print(f'Executed command\'s exit code: {exit_code}')
#     await websocket.send(str(exit_code))
#
# async def main():
#     async with websockets.serve(server, port= 1463):
#         await asyncio.Future()  # run forever
#
# if __name__ == "__main__":
#     print("Active")
#     asyncio.run(main())
#
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("18.10.80.29", 12345)) #if the clients/server are on different network you shall bind to ('', port)

s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))

f = open("test.txt", "rb")
l = os.path.getsize("test.txt")
m = f.read(l)
c.send_all(m)
f.close()
print("Done sending...")