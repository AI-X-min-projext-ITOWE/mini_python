from models.tt_tran.tran_detector import TranDetector


class TransService():
    def __init__(self):
        self.tran_detector = TranDetector()
    
    def get_translation(self, text:str, from_lang:str, to_lang:str):
        model = self.tran_detector.get_model()
        tokenizer = self.tran_detector.get_tokenizer()
        translate_result = self.tran_detector.detection(text, from_lang, to_lang)

        return translate_result
