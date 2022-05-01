import csv

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Bob', '87711769900'])
    writer.writerow(['Asa', '80000000000'])
    writer.writerow(['Ken', '87711111100'])