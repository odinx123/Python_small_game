from random import randint
from faker import Faker

fake = Faker(locale=['zh_tw'])
NumOfData = 10
gender = ['男', '女']
subj = ['電子系', '資工系', '工管系', '土木系', '美術系']

def press(event):
    with open(file='D:\programfile\Python\Test\dataSerch\\data.txt', mode='w', encoding='utf-8') as file_out:
        for i in range(NumOfData):
            name_gender = [fake.name_male(), fake.name_female()]
            address = str(fake.address()).split(' ')[1]
            phone = '09'+''.join(str(randint(0, 9)) for i in range(8))
            male_female = randint(0, len(gender)-1)
            
            print(fake.ssn(), file=file_out, end=' ')
            print(f'{name_gender[male_female]} {gender[male_female]} {subj[randint(0, len(subj)-1)]}', file=file_out, end=' ')
            print(f'{address} {phone}', file=file_out)

press('<Return>')