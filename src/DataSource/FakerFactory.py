import csv

from faker import Faker


def fakeCSVFile(rows, columns):
    faking = Faker()
    filePath = '../resource/Entities/FakerGeneratedData.csv'

    with open(filePath, 'w', newline='') as fakeFile:
        writer = csv.DictWriter(fakeFile, fieldnames=columns)
        writer.writeheader()
        for i in range(rows):
            writer.writerow({
                "emailAddress": faking.email(),
                "firstName": faking.first_name(),
                "lastName": faking.last_name(),
                "password": faking.password(),
            })


if __name__ == '__main__':
    rows = 10
    columns = ["emailAddress", "firstName", "lastName", "password"]
    fakeCSVFile(rows, columns)
