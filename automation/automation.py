import re

with open('assets/potential-contacts.txt', 'r') as file:
    text = file.read().replace('\n', '')

def extract_phone_num(file):
    phoneRe = re.compile(r'((\(?\d{3}\)?)(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))? )', re.VERBOSE)
    matches_phones = []
    for groups in phoneRe.findall(file):
        num = [groups[1], groups[3], groups[5]]
        phoneNum = '-'.join(num)
        phoneNum = re.sub(r'[(|)]', '', phoneNum)
        if phoneNum not in matches_phones:
            matches_phones.append(phoneNum)
    
    matches_phones.sort()
    return matches_phones


def extract_emails(file):
    emailRe = re.compile(r'([a-zA-Z0-9._%+-] + @[a-zA-Z0-9.-] + (\.[a-zA-Z]{2,4}))', re.VERBOSE)
    matches_emails = []
    for groups in emailRe.findall(file):
        if groups[0] not in matches_emails:
            matches_emails.append(groups[0])

    matches_emails.sort()
    return matches_emails

def save_to_files(phones,emails):
    with open("phone_numbers.txt", "w+") as f:
        for element in phones:
            f.write(element + "\n")

    with open("emails.txt", "w+") as f:
        for element in emails:
            f.write(element + "\n")


if __name__ == '__main__':
    emails = extract_phone_num(text)
    phones = extract_emails(text)
    save_to_files(phones,emails)

    print(emails)
    print("-"*50)
    print(phones)