import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Where is command line arguments?")
        print("||you should run python filename.py database.csv sequence_textfile||")
        return

    databasefilelist = []
    with open(sys.argv[1], "r") as csv_file:
        databasefile = csv.DictReader(csv_file)
        for i in databasefile:
            databasefilelist.append(i)

    with open(sys.argv[2], "r") as csv_file:
        sequencefile = csv_file.readline()

        a = {}
        for i in databasefile.fieldnames[1:]:
            a[i] = longest_match(sequencefile, i)

        for person in databasefilelist:
            fflag = False
            for key, value in a.items():
                if value != int(person[key]):
                    fflag = True
                    break
            namee = person['name']
            if fflag == False:
                print(namee)
                break
        if fflag == True:
            print("No match")

def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0

        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

main()
