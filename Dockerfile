# 1. 베이스 이미지 선택 (Python 3.9 버전 사용)
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 파일 복사 및 의존성 설치
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# uvicorn을 개별적으로 설치
RUN pip install uvicorn

# 4. Tesseract 및 Python 개발 도구 설치
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-kor \
    tesseract-ocr-chi-sim \
    tesseract-ocr-jpn \
    tesseract-ocr-spa \
    libgl1 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. 프로젝트의 모든 소스를 컨테이너로 복사
COPY . /app

# 6. uvicorn 설치 확인
RUN pip show uvicorn

# 7. 컨테이너 시작 시 실행할 명령어 지정 (FastAPI 앱 실행)
CMD ["python3", "-m", "uvicorn", "api_app:app", "--host", "0.0.0.0", "--port", "80"]
