from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

def getGames():
    url = 'https://www.rotowire.com/hockey/nhl-lineups.php'
    options = EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)

    driver.get(url)
    
    # return values
    matchups = []
    path = '/html/body/div/div/main/div[3]'
    lineups = driver.find_element(By.CLASS_NAME, 'lineups').find_elements(By.CLASS_NAME, 'lineup')
    for index, lineup in enumerate(lineups[:-1]):
        # print(index)
        if index == 3 or index == 5 or index == len(lineups[:-1])-1:
            continue
        awayTeam = lineup.find_element(By.XPATH, f'{path}/div[{index+1}]/div[2]/div[2]/a[1]').text
        homeTeam = lineup.find_element(By.XPATH, f'{path}/div[{index+1}]/div[2]/div[2]/a[2]').text
        awayTeam = awayTeam.split(' (')[0]
        homeTeam = homeTeam.split(' (')[0]
        matchups.append((awayTeam, homeTeam))

    driver.quit()

    return matchups

def main():
    matchups = getGames()

    with open('NHL_SLATE.csv','w') as f:
        for matchup in matchups:
            f.write(matchup[0] + ',' + matchup[1])
            f.write('\n\n')

if __name__ == '__main__':
    main()
