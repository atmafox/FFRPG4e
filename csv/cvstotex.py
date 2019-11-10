import csv
import os

def parse_csv(templatefn, inputfn):

  with open(templatefn) as inf:
    outfn_prefix, template = (x.strip() for x in inf.readlines())
  with open(inputfn) as inf:
    csvf = csv.reader(inf)
    output_lines = ["% Auto-generated file, see cvstotex.py"]
    current_file = None
    next(csvf)
    for row in csvf:
      row = [x.strip() for x in row]
      if not(any(row)):
        continue
      if row[-1].startswith('###') and not any(row[1:-1]):
        if current_file is not None:
          with open(outfn_prefix + current_file + '.tex', 'w') as outf:
            outf.writelines('\n'.join(output_lines))
        output_lines = []
        current_file = row[0]
        continue

      replace_strings = []
      for cell in row:
        cell = cell.replace('&','\\&')
        cell = cell.replace('%','\\%')
        cell = cell.replace('\n','\\newline{}')
        replace_strings.append('{%s}' % cell)

      output_lines.append(template.format(*replace_strings))
    # End Per-Row Loop
  # End Open CSV

if __name__ == "__main__":
  import sys
  templatefn, inputfn = sys.argv[1:]
  parse_csv(templatefn, inputfn)
      

