#для запуска pytest -n 3 .\Quest1.py
from lib import *

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def testSbisPage (driver):
    driver.get(link1)
    click('a[href *= "/contacts"]', driver)
    click('img[src *= "/static/resources/SabyRuPages/_contacts/images/logo.svg?x_module=5b9d5b6e50868d3f66c89076282b3b2d"]', driver)
    link(driver, link2)


def testContactPage (driver):
    driver.get(link2)
    istext(text("div[class *= tensor_ru-Index__block4-content] p[class*= tensor_ru-Index__card-title]",driver), case = 'Сила в людях')
    clickscrol('p[class *=tensor_ru-Index] a[href *= "/about"]', driver)
    link(driver, link3)


def testAboutPage (driver):
    driver.get(link3)
    WidhtHeight('tensor_ru-About__block3-image-filter', driver, width = 272, height = 192)

