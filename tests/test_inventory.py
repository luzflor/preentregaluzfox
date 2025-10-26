from  selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory(login_in_driver):

    try:
        driver = login_in_driver

        # 1)Criterio mínimo: Valida título de la página de inventario
        header_title = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
        assert header_title == "Products", f"Título inesperado: {header_title}"

        # 2)Criterio mínimo: Valida presencia de productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"

        # 3)Criterio mínimo: Lista nombre/precio del primero.
        first_name  = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        first_price = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
        print(f"Primer producto → {first_name} – {first_price}")
       
        
    except Exception as e:
        print(F"Error en test_inventory {e}")
        raise

    finally: 
        driver.quit() 