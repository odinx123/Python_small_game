from faker import Faker
from googletrans import Translator

translator = Translator()
fake = Faker()
NumOfData = 10

def press(event):
    with open(file='D:\programfile\Python\Test\guessEnglish\\t.txt', mode='w', encoding='utf-8') as file_out:
        for i in range(NumOfData):
            word = fake.word()
            result = translate(word)
            print(f'{word} {result}', file=file_out)

def translate(scr):
    results = translator.detect(scr).lang
    if (results == 'zh-tw' or results == 'zh-cn'):
        results = translator.translate(scr, dest='en').text
    else:
        results = translator.translate(scr, dest='zh-tw').text
    return results

press('<Return>')