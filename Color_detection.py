import cv2

cap = cv2.VideoCapture(0)

while True:

    _, frame, = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    height, width, _ = frame.shape
    frameX= int(width / 2)
    frameY= int(height / 2)

    target_pixel = hsv_frame[frameX, frameY]

    hue_value = target_pixel[0]

    color= " "
    if hue_value < 6:
        color = "RED"
    elif hue_value < 12:
        color = "Red Orange"
    elif hue_value < 17:
        color = "Orange"
    elif hue_value < 23:
        color = "YELLOW Orange"
    elif hue_value < 34:
        color = "YELLOW"
    elif hue_value < 48:
        color = "YELLOW Green"
    elif hue_value < 65:
        color = "Green"
    elif hue_value < 78:
        color = "Blue GREEN"
    elif hue_value < 95:
        color = "Cyan"
    elif hue_value < 106:
        color = "Sky Blue"
    elif hue_value < 95:
        color = "Cyan"
    elif hue_value < 129:
        color = "Blue"
    elif hue_value < 135:
        color = "Violet"
    elif hue_value < 160:
        color = "Pink"
    elif hue_value < 173:
        color = "Coral"
    else:
        color = "RED"

    target_pixel_BGR = frame[frameX, frameY]
    b, g, r =int (target_pixel_BGR[0]), int (target_pixel_BGR[1]), int (target_pixel_BGR[2])

    textX = frameX -60
    textY = frameY -150

    cv2.putText(frame, color, (textX, textY), 1, 3, (b, g, r), 2)
    print(target_pixel)
    cv2.circle(frame, (frameX, frameY), 7, (0, 225, 0), 2)

    cv2.imshow('Color detection', frame)

    keypress= cv2.waitKey(1)
    if keypress & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()