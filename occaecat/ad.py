import csv

# Example CSV data
csv_data = '''"a","b","c"
1,2,3
4,5,6'''

# Read the CSV data
reader = csv.reader(csv_data.splitlines())
for row in reader:
    print(row)

# Output:
# ['a', 'b', 'c']
# ['1', '2', '3']
# ['4', '5', '6']
