from models.ocr.ocr_detector import *
from models.tt_sum.summary_detector import *


class OcrService():
    
    @staticmethod
    def ocr_text(contents, lang):
        ocr_result = OcrDetector.detection(contents, lang)

        return ocr_result