import pyautogui
import math

screen_w, screen_h = pyautogui.size()

class GestureController:
    def __init__(self):
        self.prev_x, self.prev_y = 0, 0
        self.smoothening = 5   # lower = faster, higher = smoother

    def distance(self, p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    def process(self, hand, frame):
        index = hand[8][1:]
        thumb = hand[4][1:]
        middle = hand[12][1:]

        frame_h, frame_w, _ = frame.shape

        # 🔥 Create a smaller detection box (for better scaling)
        margin = 100
        x1 = margin
        y1 = margin
        x2 = frame_w - margin
        y2 = frame_h - margin

        # Clamp inside box
        x = max(x1, min(index[0], x2))
        y = max(y1, min(index[1], y2))

        # 🎯 Map to full screen
        screen_x = (x - x1) * screen_w / (x2 - x1)
        screen_y = (y - y1) * screen_h / (y2 - y1)

        # ⚡ Smooth movement
        curr_x = self.prev_x + (screen_x - self.prev_x) / self.smoothening
        curr_y = self.prev_y + (screen_y - self.prev_y) / self.smoothening

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x, self.prev_y = curr_x, curr_y

        # 🖱️ Left Click
        if self.distance(index, thumb) < 30:
            pyautogui.click()
            return "LEFT_CLICK"

        # 🖱️ Right Click
        if self.distance(index, middle) < 30:
            pyautogui.rightClick()
            return "RIGHT_CLICK"

        return "MOVE"
# import pyautogui
# import math

# screen_w, screen_h = pyautogui.size()

# class GestureController:
#     def __init__(self):
#         self.prev_x, self.prev_y = 0, 0

#     def distance(self, p1, p2):
#         return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

#     def process(self, hand, frame):
#         index = hand[8][1:]   # index finger tip
#         thumb = hand[4][1:]   # thumb tip
#         middle = hand[12][1:]

#         frame_h, frame_w, _ = frame.shape

#         # Convert to screen coordinates
#         x = int(index[0] * screen_w / frame_w)
#         y = int(index[1] * screen_h / frame_h)

#         # Move mouse
#         pyautogui.moveTo(x, y)

#         # Left Click (thumb close to index)
#         if self.distance(index, thumb) < 30:
#             pyautogui.click()

#         # Right Click (middle close to index)
#         if self.distance(index, middle) < 30:
#             pyautogui.rightClick()