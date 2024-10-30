from models.detection_model import DetectionModel
import numpy as np
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


class OcrDetector(DetectionModel):

    @staticmethod
    def detection(contents, lang): # -> vision.FaceDetector: 리턴 타입이 뭔지 미리 알려줌
        binary = np.fromstring(contents, np.uint8)
        cv_mat= cv2.imdecode(binary, cv2.IMREAD_COLOR)
        # lang = 'eng' or 'kor'
        text = pytesseract.image_to_string(cv_mat, lang)
        return text