import csv
import os
import itertools as it

header = "% Auto-generated file, see csvtotex.py\n"


def generate_entries():
    level = 0
    value = 0
    xp = 0
    entries = []
    while value <= 255:
        entries.append(('\\numprint{{{}}}'.format(level),
                        '\\numprint{{{}}}'.format(value),
                        '\\numprint{{{}}}'.format(xp)))
        xp += 1 + 2 * level
        value += 1
        level = value // 10
    return entries





def make_tablerows(outputfn):
    entries = generate_entries()

    # All this mess is splitting it into 3 vert columns 

    while(len(entries) % 3 != 0):
        entries.append(("","",""))

    n = len(entries)
    n1 = n//3
    n2 = n//3 * 2
    
    col1 = entries[:n1]
    col2 = entries[n1:n2]
    col3 = entries[n2:]

    output_lines = []

    for a,b,c in zip(col1,col2,col3):
        output_lines.append(' & '.join(a + b + c) + ' \\\\\n')
    
    with open(outputfn,'w') as outf:
        outf.writelines(output_lines)




if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        outputfn = sys.argv[1]
    else:
        outputfn = '../core/revised/generated/xp-table.tex'
    make_tablerows(outputfn)
