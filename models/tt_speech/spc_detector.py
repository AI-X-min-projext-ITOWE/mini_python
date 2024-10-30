from models.detection_model import DetectionModel
from gtts import gTTS

class SpcDetector(DetectionModel):

    @staticmethod
    def detection(text: str, lang:str):
        speech_list = []
        lang = 'en' if lang == 'eng' else lang
        # print("speeck lang : {}".format(lang))
        tts = gTTS(text=text, lang=lang)

        try:
            for idx, decoded in enumerate(tts.stream()):
                speech_list.append(decoded)
        except (AttributeError, TypeError) as e:
            raise TypeError(
                "'fp' is not a file-like object or it does not take bytes: %s" % str(e)
            )

        return speech_list

