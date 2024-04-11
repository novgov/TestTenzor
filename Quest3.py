#для запуска pytest -n 2 .\Quest2.py
from lib import *
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=*") 
    chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Users\\sidvs\\Downloads" ,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def testFirstSbisPage(driver):
    driver.get(link1)
    clickscrol('a[href *= "/download"]', driver)

def testDownloadPage(driver):
    driver.get("https://sbis.ru/download?tab=plugin&innerTab=default")
    click('a[href = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]',driver)
    time.sleep(10)
    file_size_site = 8.30
    downloaded_file_path = os.path.join(os.getcwd(), 'C:\\Users\\sidvs\\Downloads\\sbisplugin-setup-web.exe')
    if not os.path.exists(downloaded_file_path):
        pytest.fail("Файл не был скачан.")
    file_size_downloaded = round((((os.path.getsize(downloaded_file_path)/1024))/1024),1)
    if file_size_downloaded == file_size_site:
        print("Размеры файлов совпадают.")
    else:
        pytest.fail("Размеры файлов не совпадают.")
