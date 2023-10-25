import os

PATH_FOTO = "C:\\Users\\ERICK\\Pictures\\Screenpresso"
files = os.listdir(PATH_FOTO)
files = sorted(files, key=lambda x: os.path.getmtime(
    os.path.join(PATH_FOTO, x)), reverse=True)
print(os.path.join(PATH_FOTO, files[1]))
print("----")
print(type(files[0]))
print(type(files[2]))
# print(files[:8])
# print(files[1])
