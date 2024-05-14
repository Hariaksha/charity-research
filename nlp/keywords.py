import openpyxl, datetime
from collections import defaultdict

def main():
    start = last = datetime.datetime.now()
    counts = defaultdict(int)
    workbook = openpyxl.load_workbook(f'data/american/data.xlsx', read_only=True)
    ws = workbook.active
    print("Opened data spreadsheet")
    for i in range(2, ws.max_row + 1):
        if i % 1000 == 0:
            print(i)
        if ws[f'Q{i}'].value != None:
            for word in ws[f'Q{i}'].value.split():
                counts[word] += 1
    workbook = openpyxl.load_workbook(f'data/american/keywords.xlsx', read_only=False)
    ws = workbook.active
    print("Opened keywords spreadsheet")
    print("Number of words: ", len(counts))
    for word, count in counts.items():
        ws.append([word, count])
    last = datetime.datetime.now()
    workbook.save('data/american/keywords.xlsx')
    print("Saved")
    print("Start:", start.strftime("%d %b, %I:%M%p"), "\nLast:", last.strftime("%d %b, %I:%M%p"))

if __name__=="__main__":
    main()
