import openpyxl, csv
from collections import defaultdict

def main():
    counts = defaultdict(int)
    workbook = openpyxl.load_workbook(f'data/american/data.xlsx')
    ws = workbook.active
    for i in range(2, ws.max_row + 1):
        words = ws[f'Q{i}'].value.split()
        for word in words:
            counts[word] += 1
    filename = open('data/keywords.csv') 
    file = csv.DictReader(filename)
    for word, count in counts.items():
        file.append([word, count])

if __name__=="__main__":
    main()
