
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def main():
    options = Options()

    # Chromium 브라우저 위치
    options.binary_location = "/usr/bin/chromium"

    # 서버용 브라우저 설정
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # ChromeDriver 위치
    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    try:
        driver.get("https://www.google.com")

        print("크롬 실행 성공!")
        print("페이지 제목:", driver.title)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
