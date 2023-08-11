
from selenium import webdriver


def test_scores_service(app_url):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # You can use other WebDriver options as well
    driver.get(app_url)
    # Locate and check the score element
    score_element = driver.find_element("score")
    score = int(score_element.text)
    is_valid_score = 1 <= score <= 1000
    # Clean up
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

