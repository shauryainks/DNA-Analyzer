# DNA Sequence Matcher

This Python script is designed to analyze DNA sequences and compare them against a database of individuals to find a match based on Short Tandem Repeats (STRs). The program takes two command-line arguments: the path to the database file (`database.csv`) and the path to the DNA sequence text file (`sequence_textfile`).

## Usage

Ensure you have Python installed and then run the script as follows:

```bash
python filename.py database.csv sequence_textfile
```

Make sure to replace `filename.py` with the actual name of the Python script, `database.csv` with the path to the database file, and `sequence_textfile` with the path to the DNA sequence text file.

## Functionality

1. **Command-line Argument Check:**
   - Ensures that the correct number of command-line arguments (3) is provided. Prints an error message if incorrect usage is detected.

2. **Read Database File:**
   - Reads a CSV file (presumably a database) into a list of dictionaries (`databasefilelist`).

3. **Read DNA Sequence File:**
   - Reads a DNA sequence file (presumably in text format) into a variable (`sequencefile`).

4. **Find Longest Match of Each STR in DNA Sequence:**
   - Iterates over the fieldnames of the database to calculate the longest match of each STR in the provided DNA sequence.

5. **Check Database for Matching Profiles:**
   - Compares the calculated longest matches with each individual in the database. If a match is found, it prints the name of the individual.

6. **Print No Match if Needed:**
   - Prints "No match" if no matching profile is found in the database.

7. **Longest Match Function:**
   - Defines a function `longest_match` that calculates the length of the longest run of a subsequence in a given sequence.

## Dependencies
- `csv` module for handling CSV files.
- `sys` module for interacting with command-line arguments.

## Example
```bash
python dna_matcher.py database.csv sequence.txt
```

## Note
- Ensure that the provided DNA sequence text file contains the relevant genetic information for accurate matching.
- The script assumes a CSV format for the database file with the first column as names and subsequent columns as STRs.
- The program outputs the name of the matched individual or "No match" if no match is found.
