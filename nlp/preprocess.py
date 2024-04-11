import spacy, openpyxl

def main():
    nlp = spacy.load('en_core_web_lg')
    print("Loaded model")

    workbook = openpyxl.load_workbook('data/american/data.xlsx', read_only=False)
    ws = workbook.active
    print("Opened workbook")

    for i in range(2, ws.max_row + 1):
        if i % 100 == 0:
            break
        mission = str(ws[f'P{i}'].value)
        doc = nlp(mission) # turn mission into a spaCy document
        preprocessed_text = " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]) # take lemmas of words while lowercasing text and removing punctuation and stop words
        ws[f'Q{i}'].value = str(preprocessed_text)

    workbook.save('data/american/data.xlsx')
    print("saved")

if __name__=="__main__":
    main()
