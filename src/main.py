# -*- coding: utf-8 -*-
import csv

from populate_verb import present_terminal, populate_regular_verbs

verbs_fr = []
verbs_sp = []

f = open("output.csv", "w")
f.truncate()
f.close()


with open('input.csv', mode='r') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        verbs_fr.append(row[1])
        verbs_sp.append(row[0])
        print(f'\t{row[0]} - {row[1]}')
        line_count += 1
    print(verbs_fr,verbs_sp)





with open('output.csv', mode='w') as output_file:
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for index,verb in enumerate(verbs_fr):
        for person,term in enumerate(present_terminal):
            res = populate_regular_verbs(verbs_sp[index],verb,person,term)
            writer.writerow(res)



