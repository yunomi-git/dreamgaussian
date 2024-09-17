# import asyncio
# import logging
# import time
#
# from websockets import connect
#
# class WebsocketConnector:
#     def __init__(self, ip_address, port):
#         """
#         This class is used to create an instance of WebSockerConnector, which can be used to connect to a remote machine
#         and then execute commands on remote machine.
#
#         :param str ip_address: the remote machine's ip_address.
#         :param str port: the port number on which websocket is running on server machine.
#         """
#         self.ip_address = ip_address
#         self.URL = f"ws://{self.ip_address}:{port}"
#         self.conn = None
#         self.loop = asyncio.get_event_loop()
#
#     def get_connection(self):
#         conn = None
#         retry_count = 10
#         while conn is None and retry_count > 0:
#             try:
#                 logging.debug(f"Establishing connection with {self.URL}")
#                 conn = connect(self.URL)
#             except Exception as ex:
#                 logging.warning(f"Failed to establish connection.. retrying again after 1 min. {ex}")
#                 time.sleep(60)
#                 conn = None
#                 retry_count -= 1
#
#         if conn is None:
#             logging.error(f"Failed to establish connection with {self.URL}")
#
#         return conn
#
#     def execute_command(self, command):
#         try:
#             return self.loop.run_until_complete(self.__execute_command(command))
#         except Exception as ex:
#             logging.warning(f"Failed to execute {command =}.")
#         return False
#
#     async def __execute_command(self, command):
#         if self.conn is None:
#             logging.debug(f"Connection object is None. creating connection with {self.URL}")
#             self.conn = await self.get_connection()
#         await self.conn.send(command)
#         return await self.conn.recv()
#
#
# ip_address = '10.29.216.52'
# port='1463'
# wb = WebsocketConnector(ip_address=ip_address, port=port)
#
# command = 'echo "Hello World"'
# exit_code = wb.execute_command(command)
# if exit_code == '0':
#     print(f'Successfully executed command \'{command}\' on machine {ip_address}')
# else:
#     print(f'Could not execute command \'{command}\' on machine {ip_address}')



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("18.10.80.29", 12345)) # here you must past the public external ipaddress of the server machine, not that local address

f = open("test-receive.txt", "wb")
data = None
while True:
    m = s.recv(1024)
    data = m
    if m:
        while m:
            m = s.recv(1024)
            data += m
        else:
            break
f.write(data)
f.close()
print("Done receiving")