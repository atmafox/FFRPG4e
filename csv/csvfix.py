import csv
import os

def fix_csv(inputfn, outputfn):
  output_rows = []
  lastrow = None
  first = False
  with open(inputfn) as inf:
    csvf = csv.reader(inf)
    for row in csvf:
      combined = False
      if first:
        # This is dumb
        first=True
        continue
      if lastrow:
        if lastrow[0].strip() and lastrow[1].strip():
          # print(lastrow)
          # print(row)
          
          if not row[1].strip() and not row[2].strip():
            combined = True
            lastrow[0] += " " + row[0]
            if row[3].strip():
              lastrow[3] += '\n'+row[3]
            if len(row) > 4 and row[4].strip():
              lastrow[4] += '\n'+row[4]
            if len(row) > 5 and row[5].strip():
              lastrow[5] += '\n'+row[5]    
        # print(lastrow)
        # print("---") 
        output_rows.append(lastrow)
        if combined:
          lastrow = None
        else:
          lastrow=row
      else:
        lastrow=row
  
  with open(outputfn, 'w', encoding="utf8") as outf:
    writer = csv.writer(outf)
    writer.writerows(output_rows)
    




  # with open(outputfn, 'w') as outf:
  #   outf.writelines(output_rows)

  
if __name__ == "__main__":
  import sys
  inputfn, outputfn = sys.argv[1:]

  fix_csv(inputfn, outputfn)
      

