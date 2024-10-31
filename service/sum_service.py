from models.tt_sum.summary_detector import *



class SummaryService():

    def __init__(self):
        self.summary_object = SummaryDetector()

    def get_summary(self, text: str):
        summary_result = self.summary_object.detection(text)

        return summary_result