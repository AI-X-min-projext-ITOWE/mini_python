
from transformers import pipeline
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class SummaryDetector():
    def __init__(self):
        self.model = None

    def get_detector(self):
        if self.model == None:
            self.model = AutoModelForSeq2SeqLM.from_pretrained('eenzeenee/t5-base-korean-summarization')
    
        return self.model
    
    
    def detection(self, text: str):
        model =self.get_detector()
        tokenizer = AutoTokenizer.from_pretrained('eenzeenee/t5-base-korean-summarization')

        prefix = "summarize: "
        sample = text
        inputs = [prefix + sample]

        inputs = tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
        output = model.generate(**inputs, num_beams=3, do_sample=True, min_length=10, max_length=512)
        decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

        return nltk.sent_tokenize(decoded_output.strip())[0]