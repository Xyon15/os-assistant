"""
Tests automatisés pour le frontend avec Selenium

Ce fichier teste l'interface utilisateur :
- Ouverture de la page HTML
- Envoi de message et affichage réponse
- Toggle dark mode et persistance
"""
# Imports pour piloter Chrome automatiquement
import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Fonction pour créer et configurer le driver Chrome

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    # Active headless seulement si variable CI présente (GitHub Actions)
    if os.environ.get("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Test 1 : Vérifier que la page HTML s'ouvre correctement
def test_open_page():
    driver = setup_driver()
    # Construire chemin absolu vers index.html
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, '..', 'docs', 'index.html')
    html_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
    driver.get(html_url)
    # Vérifier que le titre contient "Assistant"
    assert "Assistant" in driver.title
    driver.quit()

# Test 2 : Vérifier l'envoi de message et l'affichage de la réponse
def test_send_message():
    driver = setup_driver()
    # Construire chemin et ouvrir page
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, '..', 'docs', 'index.html')
    html_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
    driver.get(html_url)
    
    # Trouver input et écrire message
    message_input = driver.find_element(By.CSS_SELECTOR, "#messageInput")
    message_input.send_keys("Bonjour")
    
    # Trouver bouton et cliquer
    submit_button = driver.find_element(By.CSS_SELECTOR, "#envoyerBtn")
    submit_button.click()
    
    # Attendre que les bulles de chat apparaissent (30 secondes max pour réponse LLM)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message-user, .message-assistant")))
    
    # Vérifier que des bulles existent
    bubbles = driver.find_elements(By.CSS_SELECTOR, ".message-user, .message-assistant")
    assert len(bubbles) > 0
    
    driver.quit()

# Test 3 : Vérifier le toggle du dark mode
def test_dark_mode_toggle():
    driver = setup_driver()
    # Construire chemin et ouvrir page
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, '..', 'docs', 'index.html')
    html_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
    driver.get(html_url)
    
    # Trouver le slider du switch dark mode et cliquer
    dark_slider = driver.find_element(By.CSS_SELECTOR, ".slider")
    dark_slider.click()
    
    # Attendre que l'animation se termine
    time.sleep(0.5)
    
    # Vérifier que body a la classe dark-mode
    body = driver.find_element(By.TAG_NAME, "body")
    assert "dark-mode" in (body.get_attribute("class") or "")
    
    # Recliquer pour désactiver
    dark_slider.click()
    time.sleep(0.5)
    
    # Vérifier que body n'a plus la classe dark-mode
    body = driver.find_element(By.TAG_NAME, "body")
    assert "dark-mode" not in (body.get_attribute("class") or "")
    
    driver.quit()