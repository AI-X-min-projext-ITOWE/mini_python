from models.ocr.ocr_detector import *
from models.tt_sum.summary_detector import *


class OcrSummaryService():
    
    @staticmethod
    def ocr_summary(contents, lang):
        text = OcrDetector.detection(contents, lang)
        summary = SummaryDetector()
        result = summary.detection(text)
        
        return result