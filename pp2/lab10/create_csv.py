import csv

with open('data_1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Mother', '87071231231'])
    writer.writerow(['Sister', '80000000001'])
    writer.writerow(['Me', '87072542536'])