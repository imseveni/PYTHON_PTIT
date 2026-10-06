import re
a = ''
while True:
    try: a += input()
    except: break

sentences = re.split('[.?!]', a)
for sen in sentences:
    if len(sen) == 0: continue
    sen = sen.lower().split()
    sen[0] = sen[0][:1].upper() + sen[0][1:]
    print(' '.join(sen))