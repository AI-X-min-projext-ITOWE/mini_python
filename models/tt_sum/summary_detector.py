
from transformers import pipeline

class SummaryDetector():
    def __init__(self):
        self.summarizer = None

    def get_detector(self):
        if self.summarizer == None:
            self.summarizer = pipeline(
                "summarization",
                model="stevhliu/my_awesome_billsum_model")
        
        return self.summarizer
    
    
    def detection(self, text: str):
        summarizer =self.get_detector()
        summary = summarizer(text)

        return summary[0]['summary_text']