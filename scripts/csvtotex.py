import csv
import os

header = "% Auto-generated file, see csvtotex.py\n"


def parse_csvs(templatesfn, output_dir):
    template_dir = os.path.dirname(templatesfn)
    with open(templatesfn) as inf:
        args = []
        for line in inf.readlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith('%'):
                continue

            args.append(line)
            if len(args) == 3:
                csvfn, outfn_prefix, template = args
                csvfn = os.path.join(template_dir,csvfn)
                parse_csv(csvfn, outfn_prefix, template, output_dir)
                args = []

            


def parse_csv(csvfn, outfn_prefix, template, output_dir):

    with open(csvfn) as inf:
        csvf = csv.reader(inf)
        output_lines = [header]
        current_file = None
        next(csvf)
        for row in csvf:
            row = [x.strip() for x in row]
            if not(any(row)):
                continue
            if row[-1].startswith('###') and not any(row[1:-1]):
                if current_file is not None:
                    outfn = os.path.join(output_dir, outfn_prefix + current_file + '.tex')
                    with open(outfn, 'w') as outf:
                        outf.writelines('\n'.join(output_lines))
                output_lines = [header]
                current_file = row[0]
                continue

            replace_strings = []
            for cell in row:
                cell = cell.replace('&', '\\&')
                cell = cell.replace('%', '\\%')
                cell = cell.replace('\n', '\\newline{}')
                replace_strings.append('{%s}' % cell)
            print(replace_strings)
            output_lines.append(template.format(*replace_strings))
        # End Per-Row Loop
    # End Open CSV

    # Annoying duplication to not lose last group - fix later
    if current_file is not None:
        outfn = os.path.join(output_dir, outfn_prefix + current_file + '.tex')
        with open(outfn, 'w') as outf:
            outf.writelines('\n'.join(output_lines))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        templatesfn, output_dir = sys.argv[1:]
    else:
        templatesfn = '../core/revised/csv-input/csv-input.txt'
        output_dir = '../core/revised/generated'
    parse_csvs(templatesfn, output_dir)
