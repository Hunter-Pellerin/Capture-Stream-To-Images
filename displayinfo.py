import cv2

def drawTextOnFeed(img, text, pos, bg_color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.7
    color = (255,255,255)
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font, scale, color, 2, cv2.LINE_AA)