import csv
import redis
import json

hostname = 'localhost'
portnumber = 6379
r = redis.Redis(host=hostname, port=portnumber, decode_responses=True)


def main():
    r.set('test', 'foo')
    csv_file = "results.csv"


def get_as_json():
    pass


def read_csv(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            json.dump()


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
