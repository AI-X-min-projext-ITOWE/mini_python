
from service.sum_service import *
from service.tran_service import *
from service.spc_service import *


class TextUsecase():
    
    def __init__(self):
        self.tran_lang_list = ["ko_KR", "zh_CN", "ja_XX", "es_XX", "en_XX"]
        self.spc_lang_list = ["ko", "zh-CN", "ja", "es", "en"]
        self.sum_service = SummaryService()
        self.tran_service = TransService()

    def excute(self, text:str, from_lang:int, to_lang:int, is_summary:bool, is_speech:bool):
        result = ["", ""]
        txt_result = text
        if (is_summary):
           txt_result = self.sum_service.get_summary(txt_result) 
        
        tran_result = self.tran_service.get_translation(txt_result, self.tran_lang_list[from_lang], self.tran_lang_list[to_lang])
        result[1] = tran_result
        
        if(is_speech):
            result[0] = SpeechService.get_speech(tran_result, self.spc_lang_list[to_lang])
        
        return result
