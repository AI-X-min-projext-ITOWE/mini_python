from models.tt_speech.spc_detector import SpcDetector

class TxtSpeech():

    def get_speech(text:str, lang:str):
        return SpcDetector.detection(text, lang)
    
    