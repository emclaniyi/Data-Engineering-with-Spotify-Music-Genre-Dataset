import re
import csv

from common.tables import GenreRawAll
from common.base import session
from sqlalchemy import text

base_path = "C:\\Users\\EM\\PycharmProjects\\SpotifyMusicRecommendation-Genre"
raw_path = f"{base_path}/raw/data/genres.csv"


def transform_case(string):
    return string.lower()


def clean_text(string_input):
    new_text = re.sub("['\"\[\]_()*$\d+/]", "", string_input)
    return new_text


def truncate_table(table):
    session.execute(
        text(f'TRUNCATE TABLE {table} RESTART IDENTITY CASCADE;')
    )
    session.commit()

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        print("length", len(l))
        yield l[i:i + n]

def transform_new_data():
    with open(raw_path, mode='r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        lines = list(reader)
        print(list(divide_chunks(list(reader), 1000)))
        genre_raw_objects = []

        for row in list(divide_chunks(lines, 1000)):
            print(row)
            genre_raw_objects.append(
                GenreRawAll(
                    danceability = row[0],
                    energy = row[1],
                    key=row[2],
                    loudness=row[3],
                    mode=row[4],
                    acousticness=row[5],
                    instrumentalness=row[6],
                    liveness=row[7],
                    valence=row[8],
                    tempo=row[9],
                    type=row[10],
                    id=row[11],
                    uri=row[12],
                    track_href=row[13],
                    analysis_url=row[14],
                    duration_ms=row[15],
                    time_signature=row[16],
                    genre=row[17],
                )
            )
        print("len", len(genre_raw_objects))
        session.bulk_save_objects(genre_raw_objects)
        session.commit()


def main():
    print("[Transform] start")
    print("[Transform] remove any old data from genre_raw_all table")
    truncate_table('genre_raw_all')
    print("[Transform] transform new data available run transformation")
    transform_new_data()
    print("[Transform] end")

