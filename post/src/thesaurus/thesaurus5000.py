rfile =  open(f'../../../output/5001-6000-thesaurus.csv', 'r')
wfile =  open(f'../../out/5001-6000-thesaurus.out.csv', 'w')
while True:
    line = rfile.readline()
    if not line :
        break
    terms = line.split('\t')
    word = terms[0]
    ipa = terms[4]
    mp3 = terms[8]
    mp3 = mp3.replace('sound:','sound:5001-6000/thesaurus/5001-6000-')
    definitions = terms[6]
    newline = word+'\t'+ipa+'\t'+mp3+'\t'+definitions+'\n'
    wfile.write(newline)
rfile.close()
wfile.close()