import clean_export
import csv

def swapfields(row):
    swap=[]
    end = 59
    for ini in range(44,59):
        swap.append(row[ini])
        row[ini]=row[end]
        row[end]=swap[-1]
        end+=1
    return row

def transform():
    with open(fread) as csv_file:
        csvreade = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        with open(fwrite, mode='w') as csvwrite:
            for row in csvreade:
                writer = csv.writer(csvwrite, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE)
                line=[]
                for col in range(0,74):
                    line.append(row[col])
                line = swapfields(line)
                writer.writerow(line)
                line_count += 1
        print(f'Processed {line_count} lines.')


# ini=1001
# end=2000
# for i in range(1,39):
#     word_list=f'{ini:05}-{end:05}'
#     fread = f'in/mostcommon__{word_list}.csv'
#     fwrite = f'ou/mostcommon__{word_list}.csv'
fread = f'in/mostcommon__00001-01000.csv'
fwrite = f'ou/mostcommon__00001-01000.csv'
clean_export.clear(fread)
transform()
#    ini+=1000
#    end+=1000