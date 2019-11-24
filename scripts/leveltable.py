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


def make_tablerows(outputfn, perpage):
    entries = generate_entries()

    # Rows per page -> entries per page - probably should do better
    perpage *= 3

    while(len(entries) % 3 != 0):
        entries.append(("","",""))

    output_lines = []

    while entries:
        output_lines += one_page(entries[:perpage])
        entries = entries[perpage:]

    with open(outputfn,'w') as outf:
        outf.writelines(output_lines)

def one_page(entries):

    # All this mess is splitting it into 3 vert columns 

    n = len(entries)
    n1 = n//3
    n2 = n//3 * 2

    col1 = entries[:n1]
    col2 = entries[n1:n2]
    col3 = entries[n2:]

    output_lines = []

    for a,b,c in zip(col1,col2,col3):
        output_lines.append(' & '.join(a + b + c) + ' \\\\\n')
    return output_lines




if __name__ == "__main__":
    import sys
    # Should probably actually use optparser for this ...
    perpage = int(sys.argv[1]) if len(sys.argv) > 1 else 46
    outputfn = sys.argv[2] if len(sys.argv) > 2 else '../core/revised/generated/xp-table.tex'
    
    make_tablerows(outputfn,perpage)
