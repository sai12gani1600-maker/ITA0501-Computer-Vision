
import cv2

path = r"C:\Users\DELL\OneDrive\ドキュメント\lab exp\video.mp4"

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Video not found! Check the path.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30

speed = 1

print("F = Fast Motion")
print("S = Slow Motion")
print("N = Normal Motion")
print("Q = Quit")

while True:
    ret, frame = cap.read()

    # Loop video when it reaches the end
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("Experiment 7 - Video Motion", frame)

    # Control playback speed
    if speed == 4:
        delay = 1
        skip_frames = 5
    elif speed == 0.5:
        delay = int(2000 / fps)
        skip_frames = 0
    else:
        delay = max(1, int(1000 / fps))
        skip_frames = 0

    # Skip frames for faster playback
    for _ in range(skip_frames):
        if not cap.grab():
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('f'):
        speed = 4
        print("FAST MOTION: 4x speed")

    elif key == ord('s'):
        speed = 0.5
        print("SLOW MOTION")

    elif key == ord('n'):
        speed = 1
        print("NORMAL MOTION")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
