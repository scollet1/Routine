
import csv
import yaml
import datetime

with open('exer.yaml', 'r') as stream:
    try:
        ex = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print (ex)

work = []
with open('tracker.csv', 'a+') as file:
    csvreader = csv.reader(file)
    csvwriter = csv.writer(file, delimiter=',')
    if sum(1 for row in csvreader) == 0:
        csvwriter.writerow(ex)
    for workout in ex:
        res = input('How many ' + workout + '? : ')
        work.append(res)
    work.append(datetime.date.today())
    csvwriter.writerow(work)

