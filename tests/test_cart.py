from selenium.webdriver.common.by import By

import time

def test_cart(login_in_driver):

    try:
        driver = login_in_driver
             
        driver.implicitly_wait(5)
    # 1) Criterio mínimo: Agregar al carrito el primer producto
        first_item       = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        first_item_name  = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        first_item.find_element(By.TAG_NAME, "button").click()   # botón “Add to cart”
        time.sleep(15)

     # 2) Verificar que el contador del carrito se incremente correctamente
        badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        assert badge == "1", f"El contador del carrito es {badge} (se esperaba 1)" 


     # 3)Criterio mínimo: Verifica ítem en carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_name = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        assert cart_name == first_item_name, "El producto del carrito no coincide"
         

     
    except Exception as e:
        print(F"Error en test_cart {e}")
        raise

    finally: 
        driver.quit() 
