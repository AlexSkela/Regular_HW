from pprint import pprint

import csv

import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def correct_contact(contact_list):
    phonebook = []

    phonebook.append(contacts_list[0])

    for i in contacts_list[1:]:
        fio = re.findall('\w+', str(i[:3]))
        lastname = fio[0]
        firstname = fio[1]
        if len(fio) > 2:
            surname = fio[2]
        else:
            surname = ''
        tel = re.sub('[^0-9]', '', i[5])
        tel = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})(\d{4})', r'+7(\2)-\3-\4-\5 доб.\6', tel)
        tel = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})', r'+7(\2)-\3-\4-\5', tel)
        new_line = []
        new_line.extend([lastname, firstname, surname, i[3], i[4], tel, i[6]])

        phonebook.append(new_line)


    pprint(phonebook)



correct_contact(contacts_list)