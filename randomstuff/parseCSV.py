import csv


userinputfile = input("Enter the path of the file that needs parsing:")
# Open the CSV file
with open(userinputfile, 'r') as csvfile:
    # Create a `csv.reader` object with a pipe delimiter
    reader = csv.reader(csvfile, delimiter='|')

    # Skip the header row
    next(reader)

    # Iterate through the rows in the CSV file
    for row in reader:
        # Extract the data from each row
        data = {
            'id': row[0],
            'is_pb': row[1],
            'wpm': row[2],
            'acc': row[3],
            'raw_wpm': row[4],
            'consistency': row[5],
            'char_stats': row[6],
            'mode': row[7],
            'mode2': row[8],
            'quote_length': row[9],
            'restart_count': row[10],
            'test_duration': row[11],
            'afk_duration': row[12],
            'incomplete_test_seconds': row[13],
            'punctuation': row[14],
            'numbers': row[15],
            'language': row[16],
            'funbox': row[17],
            'difficulty': row[18],
            'lazy_mode': row[19],
            'blind_mode': row[20],
            'bailed_out': row[21],
            'tags': row[22],
            'timestamp': row[23]
        }

        # print(f"{data}\n")
        for key, value in data.items():
            print(f"{key}: {value}")
            print("-----------------------------------------------------")
            if key == 'consistency':
                print("\n")


"""
  data = {
            'id': row[0],
            'is_pb': row[1],
            'wpm': row[2],
            'acc': row[3],
            'raw_wpm': row[4],
            'consistency': row[5],
            'char_stats': row[6],
            'mode': row[7],
            'mode2': row[8],
            'quote_length': row[9],
            'restart_count': row[10],
            'test_duration': row[11],
            'afk_duration': row[12],
            'incomplete_test_seconds': row[13],
            'punctuation': row[14],
            'numbers': row[15],
            'language': row[16],
            'funbox': row[17],
            'difficulty': row[18],
            'lazy_mode': row[19],
            'blind_mode': row[20],
            'bailed_out': row[21],
            'tags': row[22],
            'timestamp': row[23]
        }
"""
