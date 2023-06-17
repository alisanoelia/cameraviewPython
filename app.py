import cv2

url = "https://192.168.0.102:8080/video"
cap = cv2.VideoCapture(url)

while(cap.isOpened()):
    camera, frame = cap.read()
    try:
        cv2.imshow('Image',
                   cv2.resize(frame,
                             (600,400)))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except cv2.error:
        print('siiiiiiii')
        break

cv2.destroyAllWindows()
