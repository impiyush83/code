from collections import defaultdict

records = defaultdict(lambda: 0)

def reconcilation(item1, item2):
    item1dict = {}
    item2dict = {}
    for key in records.keys():
        if item1.strip() in key:
            item1dict[''.join(key.split('*')[1:])] = records[key]
        if item2.strip() in key:
            item2dict[''.join(key.split('*')[1:])] = records[key]
    matched = 0
    print(item1dict, item2dict)
    for key in item1dict:
        if item2dict.get(key) and item2dict[key] > 0:
            matched += 1
            item2dict[key] -= 1
    return len(item1dict.keys()) - matched +


with open('input', 'r+') as f:
    for line in f.readlines():
        record = line.split(',')
        if len(record) == 4:
            if record[0] == 'AKUNA':
                records[record[0] + '*' + record[1] + '*' + record[2]] += 1

            else:
                if records.get('AKUNA'+'*'+ record[1]+ '*' + record[2]):
                    records[record[0] + '*' + record[1] + '*' + record[2]] += 1
            print(record[2])
        else:
            print(reconcilation(record[1], record[2]))

