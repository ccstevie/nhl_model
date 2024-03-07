from get_results import getResults
from datetime import date, timedelta
import pandas as pd

def getRecord():
    df = pd.read_csv('record.csv')
    wins = 0
    losses = 0
    for index, row in df.iterrows():
        x_winner = row['X Winner']
        winner = row['Winner']
        if winner in x_winner:
            wins += 1
        else:
            losses += 1

    return wins, losses

def main():
    wins, losses = getRecord()
    print(wins)
    print(losses)

if __name__ == '__main__':
    main()
