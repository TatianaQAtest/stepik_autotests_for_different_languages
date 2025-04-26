from selenium.webdriver.common.by import By
import time

# Запуск теста:   pytest --language=es test_items.py (тест выполняется только в chrome)

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestPage:
    def test_running_for_different_languages(self, browser):        
        browser.get(link)        
    
        # Установлено время принудительной задержки браузера после открытия страницы
        # для визуального контроля       
        time.sleep(10)

        # Проверяем наличие кнопки добавления товара в корзину
        assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Ошибка: кнопка добавления товара в корзину не найдена"

if __name__ == "__main__":
    pytest.main()