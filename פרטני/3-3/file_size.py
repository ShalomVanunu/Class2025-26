import os

file_size = os.path.getsize("ShahafSetup (1).exe")
client.send(file_size.encode())

msg  : 1024
file : file_size
chat (msg)
dialog_box (file)