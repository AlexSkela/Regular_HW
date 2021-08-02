from pprint import pprint

import csv

import re

new_contacts_list = []

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def correct_contact(contact_list):
    for element in contact_list:
        # new_element = element[0:3]
        new_element = [' '.join(element[0:3])]
        for el in new_element:
            new_list = el.split()
            new_contact = new_list + element[3:7]
        new_contacts_list.append(new_contact)
    pprint(new_contacts_list)

    for person in new_contacts_list:
        for elem in person:
            pattern_phone = r"(\+7|8)?\s*\W*(\d+)\W*\s*(\d+)[-|s*](\d+)[-|s*](\d+)\s*\W*(\w*\.*)\s*(\d+)\W*"
            phone = re.match(pattern_phone, elem)
            pprint(phone)
            new_pattern_phone = r"+7(\2)-\3-\4-\5\6\7"
            result = phone.sub(new_pattern_phone, elem)
            pprint(result)

    # final_contact = []
    # for new_name in new_contacts_list:
    #     if new_name[0:1] == new_name[0:1]:
    #         set_1 = new_name | new_name
    #         person_list.append(set_1)
    #     pprint(person_list)





correct_contact(contacts_list)