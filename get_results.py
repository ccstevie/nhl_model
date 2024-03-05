from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from datetime import date, timedelta
import pandas as pd

def getResults(d):
    options = EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)

    url = f'https://www.espn.com/nhl/scoreboard/_/date/{d}'
    driver.get(url)
    
    rows = []
    table = driver.find_element(By.CSS_SELECTOR, '#fittPageContainer > div:nth-child(3) > div > div > div:nth-child(1) > div > section > div')
    cards = table.find_elements(By.TAG_NAME, 'section')
    path = "/html/body/div[1]/div/div/div/div/main/div[3]/div/div/div[1]/div/section/div"
    for i, game in enumerate(cards):
        away = game.find_element(By.XPATH, f'{path}/section[{i+1}]/div[1]/div/div[1]/div/div/ul/li[1]/div[1]/div[1]/a/div').text
        home = game.find_element(By.XPATH, f'{path}/section[{i+1}]/div[1]/div/div[1]/div/div/ul/li[2]/div[1]/div[1]/a/div').text
        away_score = game.find_element(By.XPATH, f'{path}/section[{i+1}]/div[1]/div/div[1]/div/div/ul/li[1]/div[3]').text
        home_score = game.find_element(By.XPATH, f'{path}/section[{i+1}]/div[1]/div/div[1]/div/div/ul/li[2]/div[3]').text
        winner = home if home_score > away_score else away
        rows.append({'Date': date.today() - timedelta(days=1), 'Home Team': home, 'Away Team': away, 'Home Goals': home_score, 'Away Goals': away_score, 'Winner': winner})

    driver.quit()
    df = pd.DataFrame(rows)

    return df

def main():
    d = str(date.today() - timedelta(days=1))
    # scores = dataFrame
    scores = getResults(''.join(d.split('-')))

if __name__ == '__main__':
    main()
