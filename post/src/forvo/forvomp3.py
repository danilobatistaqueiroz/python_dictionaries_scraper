import clean_export
import csv

def get_mp3(term):
    if term.strip() == '':
        return ''
    ini = 0
    end = 0
    all_mp3 = []
    while ini > -1:
        ini = term.find('[sound:')
        if ini == -1:
            return ','.join(all_mp3)
        end = term.find('.mp3',ini)
        all_mp3.append(term.substring(ini,end+4))
    return ','.join(all_mp3)

def transform():
    with open(fread) as csv_file:
        csvreade = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        with open(fwrite, mode='w') as csvwrite:
            for row in csvreade:
                writer = csv.writer(csvwrite, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE)
                line=[]
                line.append(row[0])
                line.append(get_mp3(row[12]))
                writer.writerow(line)
                line_count += 1
        print(f'Processed {line_count} lines.')


fread = f'mp3/00001-01000.csv'
fwrite = f'ou/mp3__00001-01000.csv'
clean_export.clear(fread)
transform()