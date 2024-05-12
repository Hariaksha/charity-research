import spacy, openpyxl, datetime

def main():
    start = last = datetime.datetime.now()
    nlp = spacy.load('en_core_web_lg')
    print("Loaded model")

    workbook = openpyxl.load_workbook('data/american/data.xlsx', read_only=False)
    ws = workbook.active
    print("Opened workbook")

    for i in range(2, ws.max_row + 1):
        mission = str(ws[f'P{i}'].value)
        doc = nlp(mission) # turn mission into a spaCy document
        preprocessed_text = " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]) # take lemmas of words while lowercasing text and removing punctuation and stop words
        ws[f'Q{i}'].value = str(preprocessed_text)
        if i % 10000 == 0:
            print("Finished", i)
    last = datetime.datetime.now()
    workbook.save('data/american/data.xlsx')
    print("Saved")
    print("Start:", start.strftime("%d %b, %I:%M%p"), "\nLast:", last.strftime("%d %b, %I:%M%p"))

if __name__=="__main__":
    main()
