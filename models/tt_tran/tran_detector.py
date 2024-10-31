
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

class TranDetector():
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def get_model(self):
        if self.model == None:
            self.model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        
        return self.model
    
    def get_tokenizer(self):
        if self.tokenizer == None:
            self.tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        
        return self.tokenizer

    def detection(self, text:str):
        
        #step4
        self.tokenizer.src_lang = "en_XX"
        encoded_hi = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(
            **encoded_hi,
            forced_bos_token_id=self.tokenizer.lang_code_to_id["ko_KR"]
        )
        self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        #step5
        result = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return result[0]
        
