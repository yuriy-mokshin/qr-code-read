import cv2


def qr_read(image):
    picture = cv2.imread(image)
    detect = cv2.QRCodeDetector()
    link, _, _, = detect.detectAndDecode(picture)
    return link


def main():
    print(f' [+] - link = {qr_read("qr.png")}')


if __name__ == "__main__":
    main()
