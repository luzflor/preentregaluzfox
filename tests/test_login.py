from  selenium.webdriver.common.by import By
from selenium import webdriver


def test_login_validation(login_in_driver):

    try:
        driver = login_in_driver
        # 1) Criterio mínimo: validación de /inventory.html
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"
        # 2) Criterio mínimo: validación de “Products/Swag Labs”.
        assert driver.title == "Swag Labs", "Título inesperado"  

    except Exception as e:
        print(F"Error en test_login {e}")
        raise
    finally: 
        driver.quit()    
