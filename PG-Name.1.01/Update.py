import csv

# ====== CONFIGURATION ======
LOOKUP_FILE = 'custom.csv'
LOCALIZATION_FILE = 'Localization.txt'

OUTPUT_FILE = 'Localization_updated.txt'

# Column indexes (0-based)
KEY_COLUMN = 0          # Column with the key in both files
LOOKUP_VALUE_COLUMN = 1 # Column with the English text in lookup.csv
TARGET_VALUE_COLUMN = 5 # Column to update in Localization.txt
# ============================

# Step 1: Build key → value map from lookup.csv
lookup = {}
with open(LOOKUP_FILE, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        if len(row) > max(KEY_COLUMN, LOOKUP_VALUE_COLUMN):
            key = row[KEY_COLUMN].strip()
            value = row[LOOKUP_VALUE_COLUMN].strip()
            if( not key or not value):
                print(f"Skipping empty key or value in row: {row}")
                continue
            lookup[key] = value
            print(f"Loaded key: {key} with value: {value}")

# Step 2: Process Localization.txt and replace column value where keys match
with open(LOCALIZATION_FILE, newline='', encoding='utf-8') as infile, \
     open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) > max(KEY_COLUMN, TARGET_VALUE_COLUMN):
            key = row[KEY_COLUMN].strip()
            #print(f"Processing key: {key}")
            if key in lookup:
                row[TARGET_VALUE_COLUMN] = lookup[key]
                print(f"Updated {key} to {row[TARGET_VALUE_COLUMN]}")
        writer.writerow(row)

print(f"Done. Output written to {OUTPUT_FILE}")
