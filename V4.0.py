import cv2
import numpy as np

class MotionDetector:
    def __init__(self, w=1200, error=30, pc=100, interval=1, layer=10, camera_width=48, fps=20):
        self.W, self.H = w, int(w*0.75)
        self.ERROR = error
        self.PC = pc
        self.INTERVAL = interval
        self.LAYER = layer
        self.CAMERA_WIDTH = camera_width
        self.CAMERA_HEIGHT = int(camera_width * 0.75)
        self.BLOCK_WIDTH = int(self.W / self.CAMERA_WIDTH)
        self.FPS = fps
        self.DEFAULT = np.full((self.CAMERA_HEIGHT, self.CAMERA_WIDTH, 3), 0, dtype=np.uint8)
        self.img1 = self.DEFAULT
        self.img2 = self.DEFAULT
        self.imagebox = [self.DEFAULT.copy() for _ in range(self.PC)]
        self.cap = cv2.VideoCapture(0)

    def read(self):
        ret, frame = self.cap.read()
        return cv2.resize(frame, (self.CAMERA_WIDTH, self.CAMERA_HEIGHT))

    def detect(self):
        move = np.abs(self.img1 - self.img2)
        mask = np.all((self.ERROR > move) | (move > 255 - self.ERROR), axis=2)
        move[~mask] = [255, 255, 255]
        move[mask] = [0, 0, 0]
        self.imagebox.append(move)
        del self.imagebox[0]

    def add_img(self):
        start = max(0, len(self.imagebox) - (self.INTERVAL * self.LAYER))
        img = self.imagebox[start::self.INTERVAL]

        sum_img = self.DEFAULT.copy()
        for i in range(self.LAYER):
            sum_img = cv2.addWeighted(img[i], 1, sum_img, 0.9, 0)

        return np.fliplr(cv2.resize(sum_img, (self.W, self.H), interpolation=cv2.INTER_NEAREST))

    def run(self):
        while True:
            self.img1 = self.read()
            self.detect()
            cv2.imshow("Output", self.add_img())

            if cv2.waitKey(int(1000 / self.FPS)) & 0xFF == ord("q"):
                break

            self.img2 = self.img1

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_detector = MotionDetector()
    motion_detector.run()
