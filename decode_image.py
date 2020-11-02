from PIL import Image

try:
    im = Image.open("court_secret.png")
    print(im.text['Riddle'])
except:
    print("What images have you seen so far? Try to run the code with them.")
