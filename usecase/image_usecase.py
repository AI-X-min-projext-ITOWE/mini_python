from service.ocr_service import *
from service.sum_service import *
from service.tran_service import *
from service.spc_service import *


class ImageUsecase():
    
    def __init__(self):
        self.ocr_lang_list = ["kor", "chi_sim", "jpn", "spa", "eng"]
        self.tran_lang_list = ["ko_KR", "zh_CN", "ja_XX", "es_XX", "en_XX"]
        self.spc_lang_list = ["ko", "zh-CN", "ja", "es", "en"]
        self.sum_service = SummaryService()
        self.tran_service = TransService()

    def excute(self, contents:str, from_lang:int, to_lang:int, is_summary:bool, is_speech:bool):
        result = ["", ""]
        txt_result = OcrService.ocr_text(contents, self.ocr_lang_list[from_lang])
        result[1] = self.tran_service.get_translation(txt_result, self.tran_lang_list[from_lang], self.tran_lang_list[to_lang])
        if (is_summary):
            # 요약
            txt_result = self.sum_service.get_summary(txt_result)
            # 요약 내용 저장
            result[0] = self.tran_service.get_translation(txt_result, self.tran_lang_list[from_lang], self.tran_lang_list[to_lang])
            
        if(is_speech):
            speech_text = result[0] if is_summary else result[1] 
            result[0] = SpeechService.get_speech(speech_text, self.spc_lang_list[to_lang])

        return result

