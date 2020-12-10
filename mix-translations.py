import re 

def mix_fields_pt(line):
    return mix_fields(line,1,2,2,3)

def mix_fields_es(line):
    return mix_fields(line,3,4,4,5)

def mix_fields(line,ini_google,end_google,ini_yandex,end_yandex):
    ini_pos = [r.start() for r in re.finditer(r"\t",line)][ini_google]
    end_pos = [r.start() for r in re.finditer(r"\t",line)][end_google]
    google = line[ini_pos:end_pos]
    google = google.replace('\t','').replace(', ',',')

    ini_pos = [r.start() for r in re.finditer(r"\t",line)][ini_yandex]
    end_pos = [r.start() for r in re.finditer(r"\t",line)][end_yandex]
    yandex = line[ini_pos:end_pos]
    yandex = yandex.replace('\t','').replace(', ',',')

    if google.lower() == yandex.lower():
        return ''.join([yandex,'\t'])
    else:
        return ''.join([google+','+yandex,'\t'])

def word_and_ipa(line):
    second_tab = [r.start() for r in re.finditer(r"\t",line)][1]
    return line[:second_tab+1]

def readFile():
    file = open("5001-6000-translated.txt","r")
    lines = []
    for line in file:
        fields = word_and_ipa(line)
        fields += mix_fields_pt(line)
        fields += mix_fields_es(line)
        lines.append(fields)
    file.close()
    return lines

def writeFile(lines):
    file = open("5001-6000-mixed.txt","w")
    file.write('\n'.join(lines))

lines = readFile()
writeFile(lines)