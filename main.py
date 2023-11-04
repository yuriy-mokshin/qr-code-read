import cv2
import pyautogui
import time


def get_screenshot(image_name):
    image = pyautogui.screenshot(region=(1375, 840, 200, 200))
    image.save(image_name)


def qr_read(image_name):
    picture = cv2.imread(image_name)
    detect = cv2.QRCodeDetector()
    link, _, _, = detect.detectAndDecode(picture)
    return link


def processing_document():
    time.sleep(5)
    print(' [+] - start - ')
    for i in range(1):
        print(f' [+] - step #{str(i)}')
        get_screenshot(f"qr{str(i)}.png")
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        print(f' [+] - link = {qr_read(f"qr{str(i)}.png")}')
    print(' [+] - finish - ')


def main():
    processing_document()


if __name__ == "__main__":
    main()
