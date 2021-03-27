import clean_export
import csv

def remove_all_frequencies(col):
    terms = col.split(',')
    clean = []
    for term in terms:
        clean.append(remove_frequency(term))
    return ','.join(clean)

def remove_frequency(term):
    ini = term.find(')')
    if term.strip() == '':
        return ''
    if ini == -1:
        return term
    return term[ini+1:]

def transform():
    with open(fread) as csv_file:
        csvreade = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        with open(fwrite, mode='w') as csvwrite:
            for row in csvreade:
                writer = csv.writer(csvwrite, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE)
                line=[]
                line.append(row[0])
                col = remove_all_frequencies(row[5]).split(',')
                col.extend(remove_all_frequencies(row[6]).split(','))
                col = list(set(col))
                line.append('<i><u><font color="#aa4444">'+','.join(col)+'</font></u></i>')
                writer.writerow(line)
                line_count += 1
        print(f'Processed {line_count} lines.')


# ini=1001
# end=2000
# for i in range(1,39):
#     word_list=f'{ini:05}-{end:05}'
#     fread = f'in/mostcommon__{word_list}.csv'
#     fwrite = f'ou/mostcommon__{word_list}.csv'
fread = f'in/common__01001-02000.csv'
fwrite = f'ou/common__01001-02000.csv'
clean_export.clear(fread)
transform()
#    ini+=1000
#    end+=1000