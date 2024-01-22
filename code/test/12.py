import cv2

# 設置 KCF 追蹤器
tracker = cv2.TrackerKCF_create()

# 讀取影片
video = cv2.VideoCapture("images\\f3.mp4")
if not video.isOpened():
    print("無法打開影片")
    exit()

# 讀取第一幀
ok, frame = video.read()
if not ok:
    print('無法讀取影片文件')
    exit()

# 選擇 ROI
bbox = cv2.selectROI("roi", frame, False)

# 使用第一幀和 ROI 初始化追蹤器
tracker.init(frame, bbox)

# 打開影片寫入器
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("test123.mov", cv2.VideoWriter_fourcc(*'MP4V'), 25, (frame_width, frame_height))

while True:
    # 讀取新的一幀
    ok, frame = video.read()
    if not ok:
        break

    # 更新追蹤器
    ok, bbox = tracker.update(frame)

    # 畫出邊界框
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        cv2.putText(frame, "追蹤失敗", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # 顯示追蹤器類型和 FPS 於畫面上
    fps = video.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, f"KCF 追蹤器 | FPS: {int(fps)}", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # 顯示結果
    cv2.imshow("追蹤", frame)
    out.write(frame)

    if (cv2.waitKey(5) == ord('q')):#
        break

video.release()#

cv2.destroyAllWindows()#
