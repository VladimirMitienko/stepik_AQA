import time
from selenium.webdriver.common.by import By



languages = [
    ("ar", 'العربيّة', 'أضف الى سلة التسوق'),
    ("ca", 'català', 'Afegeix a la cistella'),
    ("cs", 'česky', 'Vložit do košíku'),
    ("da", 'dansk', 'Læg i kurv'),
    ("de", 'Deutsch', 'In Warenkorb legen'),
    ("en-gb", 'English', 'Add to basket'),
    ("el", 'Ελληνικά', 'Προσθήκη στο καλάθι'),
    ("es", 'español', 'Añadir al carrito'),
    ("fi", 'suomi', 'Lisää koriin'),
    ("fr", 'français', 'Ajouter au panier'),
    ("it", 'italiano', 'Aggiungi al carrello'),
    ("ko", '한국어', '장바구니 담기'),
    ("nl", 'Nederlands', 'Voeg aan winkelmand toe'),
    ("pl", 'polski', 'Dodaj do koszyka'),
    ("pt", 'Português', 'Adicionar ao carrinho'),
    ("pt-br", 'Português Brasileiro', 'Adicionar à cesta'),
    ("ro", 'Română', 'Adauga in cos'),
    ("ru", 'Русский', 'Добавить в корзину'),
    ("sk", 'Slovensky', 'Pridať do košíka'),
    ("uk", 'Українська', 'Додати в кошик'),
    ("zh-cn", '简体中文', 'Add to basket'),
]

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert True
