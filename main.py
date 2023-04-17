import pytesseract
import os

from googletrans import Translator
from PIL import Image


# import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# text = "Hello, world!"
# url = "https://translate.google.com/m?hl=en&sl=en&tl=es&ie=UTF-8&prev=_m&q=" + text
# response = requests.get(url, headers=headers)
# print(response.content)
def formater(text: str, leter=1):
    while "\nO" in text:
        text = text.replace("\nO", f"\n{leter}) ", 1)
        leter += 1

    while "\n©" in text:
        text = text.replace("\n©", f"\n{leter}) ", 1)
        leter += 1

    return text


PATH_FOTO = "C:\\Users\\ERICK\\Pictures\\Screenpresso"
files = os.listdir(PATH_FOTO)
files = sorted(files, key=lambda x: os.path.getmtime(
    os.path.join(PATH_FOTO, x)), reverse=True)

img = Image.open(os.path.join(PATH_FOTO, files[1]))

texto = pytesseract.image_to_string(img)
texto1 = formater(texto)
print("----")
print("")
print("-----INGLES-----")
print(texto1)

traductor = Translator()
texto_traducido = traductor.translate(texto1, dest='es').text

print("")
print("")
print("++++++")

print("---ESPA---")
print(texto_traducido)
