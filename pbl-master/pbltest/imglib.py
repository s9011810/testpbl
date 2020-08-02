import cv2
import numpy as np

class Picture_part:
    def __init__(self,filename):
        self.filename = filename

    def horizontal(self):
        orginal_img = cv2.imdecode(np.fromfile(self.filename, np.uint8), cv2.IMREAD_COLOR)
        h,w,c = orginal_img.shape
        #橫式處理
        if h<w :
            new_w_start= int(w /30*16)
            new_w_end = int(w /30*28)
            new_h_start = int(h /21*4)
            new_h_end = int(h /21*16)
            img = orginal_img[new_h_start:new_h_end,new_w_start:new_w_end ]
            return img
        else :
            return orginal_img

    def vertical(self):
        orginal_img = cv2.imdecode(np.fromfile(self.filename, np.uint8), cv2.IMREAD_COLOR)
        h, w, c = orginal_img.shape
        # 橫式處理
        if w < h:
            new_w_start = int(w / 21 * 4)
            new_w_end = int(w / 21 * 20)
            new_h_start = int(h / 30 * 5)
            new_h_end = int(h / 30 * 16)
            img = orginal_img[new_h_start:new_h_end, new_w_start:new_w_end]
            return img
        else:
            return orginal_img
