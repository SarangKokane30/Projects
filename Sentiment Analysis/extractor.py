from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def extract_comments(video_url):
    # Set up ChromeDriver
    driver = webdriver.Chrome()

    # Open the YouTube video
    driver.get(video_url)
    time.sleep(5)  # Wait for the page to load

    # Scroll down to load comments
    for _ in range(30):  # Scroll 30 times
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)  # Wait for comments to load

    # Extract comments
    comments = [c.text.strip() for c in driver.find_elements(By.CSS_SELECTOR, 'span.yt-core-attributed-string')]

    # Close the browser
    driver.quit()

    # Save to CSV
    pd.DataFrame(comments, columns=["Comment"]).to_csv("youtube_comments.csv", index=False)
    print("Comments saved to youtube_comments.csv")