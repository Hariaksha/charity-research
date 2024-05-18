import openpyxl, datetime, pandas as pd
from collections import Counter

def main():
    # Get start time
    start = datetime.datetime.now()

    # Load the data
    df = pd.read_excel('data/american/data.xlsx')
    print("Made dataframe")

    # Count words
    words = df['Preprocessed Mission'].str.split(expand=True).stack()
    counts = Counter(words)
    print("Finished counting")
    print("Number of words: ", len(counts))

    # Open output workbook
    workbook = openpyxl.load_workbook(f'data/american/keywords.xlsx', read_only=False)
    ws = workbook.active
    print("Opened keywords spreadsheet")

    # Print word counts
    for word, count in counts.items():
        ws.append([word, count])
    print("Printed words and counts")

    # Save workbook and finish
    workbook.save('data/american/keywords.xlsx')
    print("Saved")
    print("Start:", start.strftime("%d %b, %I:%M%p"), "\nLast:", datetime.datetime.now().strftime("%d %b, %I:%M%p"))

if __name__=="__main__":
    main()
