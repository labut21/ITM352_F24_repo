import csv

total = 0
count = 0
max_value = float('-inf')
min_value = float('inf')

with open('/Users/lanceabut/Downloads/survey_1000.csv', mode='r') as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        realinc = float(row['REALINC'])
        if realinc > 0:
            total += realinc
            count += 1
            if realinc > max_value:
                max_value = realinc
            if realinc < min_value:
                min_value = realinc

average = total / count if count > 0 else 0

print(f'Count of REALINC > 0: {count}')
print(f'Average REALINC > 0: {average}')
print(f'Maximum REALINC > 0: {max_value if count > 0 else "N/A"}')
print(f'Minimum REALINC > 0: {min_value if count > 0 else "N/A"}')