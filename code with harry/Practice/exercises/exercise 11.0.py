
from win10toast import ToastNotifier
import time
from PIL import Image 

repeat_interval=10
# sec=time.strftime('%S')
# print(sec)

# to convert .png into .ico
icon=Image.open("C:\\Users\\tohid kazi\\OneDrive\\ドキュメント\\My programmes\\own programes\\nature.jpg")
icon.save("insta_logo.ico")

while True:
    t=ToastNotifier()
    t.show_toast(
        "Drink water",
        "Hey Tohid now it's time to drink water",
        duration=1,
        icon_path="insta_logo.ico",
        threaded=True
    )
    time.sleep(repeat_interval)
    





