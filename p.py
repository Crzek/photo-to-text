import os

PATH_FOTO = "C:\\Users\\ERICK\\Pictures\\Screenpresso"
files = os.listdir(PATH_FOTO)
files = sorted(files, key=lambda x: os.path.getmtime(
    os.path.join(PATH_FOTO, x)), reverse=True)
print(os.path.join(PATH_FOTO, files[1]))
