import clean_export
import csv

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
                line[59] = line[44]
                line[44] = ''
                writer.writerow(line)
                line_count += 1
        print(f'Processed {line_count} lines.')


# ini=1001
# end=2000
# for i in range(1,39):
#     word_list=f'{ini:05}-{end:05}'
#     fread = f'in/mostcommon__{word_list}.csv'
#     fwrite = f'ou/mostcommon__{word_list}.csv'
fread = f'in/common__03001-04000.csv'
fwrite = f'ou/common__03001-04000.csv'
clean_export.clear(fread)
transform()
#    ini+=1000
#    end+=1000