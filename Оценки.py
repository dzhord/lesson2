

ocenki = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
          {'school_class': '4b', 'scores': [2,2,3,4,3]},
          {'school_class': '4v', 'scores': [4,5,3,2,4]},
          {'school_class': '4g', 'scores': [5,5,5,3,5]}
          ]

#for i in ocenki:
#    print(i)
s = 0
count = 0

for item in ocenki:
    # здесь в item будет лежат словарь вида {'school_class': '4a', 'scores': [4,5,4,5,5]}
    print(sum(item['scores']))
    s += sum(item['scores'])
    count += 1

print(s/count)

slovar = []

for item in ocenki:
    print(item['school_class'] + ' ' + str(sum((item['scores']))/len(item['scores'])))


print('\n\n\n\n')
print(slovar)


