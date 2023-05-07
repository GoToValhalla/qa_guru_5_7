import csv
import os.path
import property


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    csv_path = os.path.join(property.RESOURCES_PATH, 'eggs.csv')
    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        name = []
        for row in csvreader:
            name.append(row)
        assert name[0] == ['Anna', 'Pavel', 'Peter']
        assert name[1] == ['Alex', 'Serj', 'Yana']