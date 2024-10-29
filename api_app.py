from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# .env 파일의 환경 변수 불러오기
load_dotenv()

# 환경 변수 사용하기
host = os.getenv('FRONT_HOST')
host = host if host != 'localhost' else 'localhost'

app = FastAPI()
print(host)

# 허용할 도메인 목록 설정
origins = [
    "http://localhost",
    "http://localhost:3000",
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



@app.post("/image-to-text/")
async def create_file(file:UploadFile , is_summary:bool):
    pass


@app.post("/image-to-speech/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}