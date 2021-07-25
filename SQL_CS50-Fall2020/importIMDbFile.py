import csv

#open TSV file for reading
with open("data/title.basics.tsv","r") as titles:

    # since the file is a TSV file, we can use the CSV reader and change
    # the separator to a tab.
    reader = csv.DictReader(titles, delimiter = "\t")

    # open new CSV file for writing
    with open("show0.csv", "w") as shows:

        # create writer
        writer = csv.writer(shows)

        # write header of the columns we want
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])
        # iterate over TSV file
        for row in reader:
            # if non-adult TV show
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
                # write row
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])

# if year not missing (we need to escape the backlash too)
if row["startYear"] != "\\N":
    #if since 1970
    if int(row["startYear"]) >= 1970:
        #write row
        writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])

