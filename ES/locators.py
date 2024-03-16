from selenium.webdriver.common.by import By

class LocatorsClass():
    COOKIES_ES                  = (By.XPATH, '//button[@title="Rechazar cookies opcionales"]')
    COOKIES_CA                  = (By.XPATH, '//button[@title="Rebutjar cookies opcionals"]')
    COOKIES_EN                  = (By.XPATH, '//button[@title="Reject optional cookies"]')
    LOGIN_EMAIL                 = (By.ID, "email")
    LOGIN_PASS                  = (By.ID, "pass")
    LOGIN_BTN                   = (By.XPATH, "//button[@name='login']")
    LOGIN_FORGOTTEN_PASS_LINK   = (By.CLASS_NAME, '_97w4')
    LOGIN_ERR_MSG               = (By.CLASS_NAME, '_9ay7')
    GROUPS_BTN                  = (By.XPATH, '//a[@aria-label="Grupos" or @aria-label="Groups" or @href="https://www.facebook.com/groups/?ref=bookmarks"]')
    GROUP_WRITE_STG_LINEBOX     = (By.XPATH, '//span[contains(text(), "Escribe algo")]')
    WARNING_LINK_POPUP          = (By.XPATH, '//span[text()="Compartir de todas formas"]')
    POST_WRITE_BOX              = (By.XPATH, '//div[contains(@class, "_1mf") and contains(@class, "_1mj")]')
    POST_BTN                    = (By.XPATH, '//div[@aria-label="Publicar"]')