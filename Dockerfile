# 1. 베이스 이미지 선택 (Python 3.9 버전 사용)
FROM python:3.9-slim

# 2. 컨테이너 내에 작업 디렉토리 생성
WORKDIR /app


#도커가 pip 설치된 파일들을 같이 합쳐서 이미지를 만드는지 확인이 안되기 때문에 
#먼저 도커 파일 만들어서 pip파일들을 같이 이미지에 넣는지 확인해보고 밑 코드를 실행할 계획

# # 3. 로컬의 requirements.txt 파일을 컨테이너로 복사
# COPY requirements.txt /app/requirements.txt

# # 4. 의존성 설치
# RUN conda create -n sum_insect python=3.12
# RUN conda activate sum_insect
# RUN conda install -c conda-forge tesseract pytesseract
# RUN conda install -c conda-forge tesseract-data-eng
# RUN conda install -c conda-forge tesseract-data-kor
# RUN pip install -r requirements.txt

# 5. 프로젝트의 모든 소스를 컨테이너로 복사
COPY . /app

# 6. 컨테이너 시작 시 실행할 명령어 지정 (예: main.py 실행)
CMD ["python", "main.py"]