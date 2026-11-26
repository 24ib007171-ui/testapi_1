
FROM python:3.11-slim

# Chromium 브라우저와 ChromeDriver 설치
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# 작업 폴더 생성
WORKDIR /app

# Python 라이브러리 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# 프로그램 실행
CMD ["python", "main.py"]
