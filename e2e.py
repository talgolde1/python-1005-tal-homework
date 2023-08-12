from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scores_service(app_url):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(app_url)
    try:
        wait = WebDriverWait(driver, 10)
        score_element = wait.until(EC.presence_of_element_located((By.ID, "score")))
        score = int(score_element.text)
        is_valid_score = 1 <= score <= 1000
    except Exception as e:
        print("An error occurred:", e)
        is_valid_score = False
    driver.quit()
    return is_valid_score


def main_function(app_url):
    if test_scores_service(app_url):
        return 0
    else:
        return -1


if __name__ == "__main__":
    app_url = "http://localhost:8777/"
    exit_code = main_function(app_url)
    exit(exit_code)
