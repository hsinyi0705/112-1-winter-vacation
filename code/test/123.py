import cv2

# 開啟影片檔案
cap = cv2.VideoCapture('images\\f3.mp4')

# 初始化追蹤器
tracker = cv2.TrackerKCF_create()

# 選擇初始框
ret, frame = cap.read()
bbox = cv2.selectROI("Select Coin Cup", frame, fromCenter=False, showCrosshair=True)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)
    if success:
        # 追蹤成功，繪製追蹤框
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Coin Cup", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Coin Cup Tracking", frame)

    if cv2.waitKey(3) & 0xFF == 27:  # 按下Esc退出
        break

cap.release()
cv2.destroyAllWindows()
