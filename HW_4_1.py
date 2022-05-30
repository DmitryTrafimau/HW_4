ELECTRICITY = [
[6,  12, 7,  5,  32, 28, 4,  28, 8,  6,  9, 7,  9,  7,  10, 36, 4,  7,  5,  12, 8,  9,  11, 10],
[7,  20, 4,  48, 5,  10, 10, 8,  28, 12, 7, 36, 9,  6,  5,  16, 9,  12, 11, 4,  16, 11, 28, 4],
[12, 9,  44, 12, 8,  9,  5,  10, 8,  8,  7, 12, 10, 44, 4,  12, 8,  28, 9,  9,  7,  7,  6,  6],
[12, 7,  12, 48, 48, 44, 44, 10, 8,  10, 6, 12, 4,  8,  28, 9,  9,  6,  9,  4,  11, 40, 5,  5],
[44, 11, 48, 12, 12, 40, 7,  9,  7,  9,  5, 10, 4,  8,  7,  6,  4,  12, 12, 8,  12, 8,  11, 5],
[12, 10, 12, 7,  10, 12, 32, 9,  4,  8,  9, 4,  6,  48, 9,  8,  11, 8,  12, 12, 10, 11, 11, 4]
]

HOURS = ['0 ч', '1 ч', '2 ч', '3 ч', '4 ч', '5 ч', '6 ч', '7 ч', '8 ч', '9 ч', '10 ч', '11 ч', '12 ч',
         '13 ч', '14 ч', '15 ч', '16 ч', '17 ч', '18 ч', '19 ч', '20 ч', '21 ч', '22 ч', '23 ч']

WATER = [
[10, 12, 10, 5,  6,  16, 6,  10, 9,  7,  5,  11, 8,  8,  12, 40, 7,  4,  6,  7,  11, 12, 10, 48],
[8,  44, 12, 5,  11, 24, 10, 10, 4,  10, 5,  11, 10, 4,  10, 5,  5,  7,  9,  8,  5,  8,  9,  8],
[11, 5,  32, 11, 5,  7,  4,  6,  9,  8,  5,  48, 8,  7,  10, 8,  40, 9,  10, 10, 12, 4,  6,  9],
[8,  11, 12, 9,  12, 36, 9,  8,  11, 6,  8,  7,  7,  12, 44, 24, 5,  8,  12, 11, 10, 16, 48, 10],
[10, 11, 7,  40, 11, 6,  11, 9,  11, 9,  20, 10, 5,  44, 6,  32, 6,  10, 11, 7,  9,  7,  40, 36],
[5,  4,  6,  12, 4,  16, 6,  7,  10, 5,  8,  7,  5,  12, 12, 32, 12, 4,  7,  7,  9,  10, 12, 12]
]

ABONENTS = ['Ivanov', 'Sergeev', 'Doe', 'Smith', 'Kuznecov', 'Averkin']

for name, e_str, w_str in zip(ABONENTS, ELECTRICITY, WATER):
    for n, (h, e, w) in enumerate(zip(HOURS, e_str, w_str)):
        if e > 20 and w > 20 and 6 < n < 23:
            print(name, 'cтирает в', h, '(расход электричества', e, ', расход воды', w, ')')
print('\n')

debts = {
'Ivanov': {'electricity': '140', 'water': '12', 'debt': '3100'},
'Doe': {'electricity': '280', 'water': '16', 'debt': '1475'},
'Smith': {'electricity': '320', 'water': '9', 'debt': '1600'},
'Kroft': {'electricity': '145', 'water': '12', 'debt': '2856'},
'Tulle': {'electricity': '120', 'water': '8', 'debt': '4550'},
'Yanson': {'electricity': '223', 'water': '4', 'debt': '1600'},
'Kuznetsov': {'electricity': '543', 'water': '12', 'debt': '2300'}
}
names = []
elec = []
wat = []
deb = []
deb_name = {}
for a in debts:
    names.append(a)
for b in debts.values():
   elec.append(b.get('electricity'))
   wat.append(b.get('water'))
   deb.append(b.get('debt'))
for NAME, e, w, d in zip(names, elec, wat, deb):
    e = int(e)
    w = int(w)
    d = int(d)
    if e < 150 and w < 10:
        d = d - e*23 - w*87
        if d > 0:
            deb_name.update({NAME:d})
    elif e < 150:
        d = d - e*23
        if d > 0:
            deb_name.update({NAME:d})
    elif w < 10:
        d = d - w*87
        if d > 0:
            deb_name.update({NAME:d})
    else:
        deb_name.update({NAME:d})
print('Должники и их задолженность', *deb_name.items())






