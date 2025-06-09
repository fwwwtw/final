# 0609 看你家附近的 CCTV https://data.gov.tw/dataset/166140

# 安裝 OpenCV 模組 ( pip install opencv-python )
import cv2

# 臺南市交通攝影機串流網址 -  https://trafficopendata.tainan.gov.tw/opendata/json/cctv/latest 善化區 178線與南科北路口西桿(向
url = 'https://trafficvideo.tainan.gov.tw/172023003100'

# 嘗試開啟串流
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("🚫 無法開啟攝影機串流，請檢查網路連線或 URL 是否有效")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("⚠️ 串流中斷，重新連線中...")
        cap.release()
        cap = cv2.VideoCapture(url)
        continue

    cv2.imshow('Tainan CCTV - oxxostudio', frame)  

    # 每毫秒更新畫面，按下 'q' 鍵可結束
    if cv2.waitKey(1) == ord('q'):
        print("🛑 已結束串流觀看")
        break