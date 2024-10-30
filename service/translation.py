from models.tt_tran.tran_detector import TranDetector


class Translation():
    def __init__(self):
        self.tran_detector = TranDetector()
    
    def get_translation(self, text:str):
        model = self.tran_detector.get_model()
        tokenizer = self.tran_detector.get_tokenizer()
        result = self.tran_detector.detection(text)
        print(result)
        return result
