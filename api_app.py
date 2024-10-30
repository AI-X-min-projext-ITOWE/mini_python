from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import base64
from dotenv import load_dotenv
from service.ocr_to_summary import *
from service.txt_to_speech import *
from service.translation import *
# .env 파일의 환경 변수 불러오기
load_dotenv()

# 환경 변수 사용하기
host = os.getenv('FRONT_HOST')
host = host if host != 'localhost' else 'localhost'

app = FastAPI()

# 허용할 도메인 목록 설정
origins = [
    "http://{0}:3000".format(host),
    "http://{0}".format(host)
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # 허용할 도메인들
    allow_credentials=True,       # 쿠키 등의 자격 증명 허용 여부
    allow_methods=["*"],          # 모든 HTTP 메소드 허용
    allow_headers=["*"],          # 모든 HTTP 헤더 허용
)



@app.post("/summary")
async def create_file(file:UploadFile , is_summary:bool, lang:str):
    contents = await file.read()
    result = OcrSummaryService.ocr_summary(contents, lang)
    
    return {
        "결과 : " : result
    }

@app.post("/text")
async def create_text(file:UploadFile):
    lang = 'en'
    pass

@app.post("/translate")
async def create_text(text:str):
    translate_service = Translation()
    translate_txt = translate_service.get_translation(text)

    return {
        "번역 : " : translate_txt
    }

@app.post("/speech")
async def create_speech(file:UploadFile, lang: str):
    contents = await file.read()
    text = OcrSummaryService.ocr_summary(contents, lang)
    print(text)
    result = TxtSpeech.get_speech(text, lang)
    # speech_list의 각 바이트 데이터를 Base64로 인코딩
    encoded_audio = base64.b64encode(b"".join(result)).decode('utf-8')

    return {"audio_base64": encoded_audio}