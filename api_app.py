from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from service.ocr_service import *
from service.txt_to_speech import *
from service.tran_service import *
from service.sum_service import *

# .env 파일의 환경 변수 불러오기
load_dotenv()

# 환경 변수 사용하기
host = os.getenv('FRONT_HOST')
host = host if host != 'localhost' else 'localhost'
translate_service = TransService()
sum_service = SummaryService()

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
# 텍스트,이미지 : 내용, 요약, 음성

#1. 이미지를 뽑아 내용을 요약하고 번역해서 읽어준다. -텍스트
@app.post("/ocr-sum-spc")
async def create_speech(file:UploadFile, lang: str, tran_lang:str):
    contents = await file.read()

    ocr_result = OcrService.ocr_text(contents, lang)
    sum_result = sum_service.get_summary(ocr_result)
    tran_result = translate_service.get_translation(sum_result)
    speech_result = TxtSpeech.get_speech(tran_result, lang)
    
    return {
        "result": speech_result
        }   

#2. 이미지를 뽑아 내용을 번역해서 읽어준다. -요약 -텍스트
@app.post("/ocr-spc")
async def create_speech(file:UploadFile, lang: str, tran_lang:str):
    contents = await file.read()
    
    ocr_result = OcrService.ocr_text(contents, lang)
    tran_result = translate_service.get_translation(ocr_result)
    speech_result = TxtSpeech.get_speech(tran_result, tran_lang)    

    return {
        "result": speech_result
        }
#3. 이미지를 뽑아 내용을 번역해서 읽어준다. -요약 -음성
@app.post("/ocr-tran")
async def create_speech(file:UploadFile, lang: str, tran_lang:str):
    contents = await file.read()
    
    ocr_result = OcrService.ocr_text(contents, lang)
    tran_result = translate_service.get_translation(ocr_result) 

    return {
        "result": tran_result
        }

#4. 텍스트 내용을 번역한다. -이미지 -요약 -음성
@app.post("/txt")
async def create_text(text: str, lang):
    # 번역 언어 선택을 좀 더 자유롭게 하도록 수정
    tran_result = translate_service.get_translation(text)

    return {
        "result" : tran_result
    }

#5. 텍스트 내용을 요약하고 번역한다. -이미지 -음성
@app.post("/txt-sum")
async def create_file(text: str):
    
    sum_result = sum_service.get_summary(text)
    tran_result = translate_service.get_translation(sum_result)
    
    return {
        "result" : tran_result
    }