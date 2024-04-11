#для запуска pytest -n 2 .\Quest2.py
from lib import *

@pytest.fixture

def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    prefs = {
        'profile.default_content_setting_values': {
            'geolocation': 1
    },
        'profile.content_settings.exceptions.geolocation': {
            'BaseUrls.Root.AbsoluteUri': {
                'last_modified': '13160237885099795',
                'setting': '1'
        }
    }
}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def testFirstSbisPage(driver):
    driver.get(link1)
    click('a[href *= "/contacts"]', driver)

def testContactsSbisPage(driver):
    driver.get(link4)
#     script = """
#      new Promise(function(resolve, reject) {
#      navigator.geolocation.getCurrentPosition(function(position) {
#          resolve(position);
#      }, function(error) {
#          reject(error);
#      });
#      });
#  """
#     location = driver.execute_script(script)
    # Хотел через вызов скрипта геолокацию определить и сравнить, но не сработало, пытался сверху закинуть настройки на разрещение геолокации... При необходимости можно допилить и раскомментировать
    istext(text ('span[class *= sbis_ru-Region-Chooser__text]', driver), 'Московская обл.')
    istext(text ('div [id *= city-id-2]', driver), 'Москва')
    click('span [class="sbis_ru-Region-Chooser__text sbis_ru-link"]', driver)
    click('span[title = "Камчатский край"]', driver)
    time.sleep(1)
    istext(text ('span[class *= sbis_ru-Region-Chooser__text]', driver), 'Камчатский край')
    istext(text ('div [id *= city-id-2]', driver), 'Петропавловск-Камчатский')