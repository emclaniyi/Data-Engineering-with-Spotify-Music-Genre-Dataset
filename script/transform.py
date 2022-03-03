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


def transform_new_data():
    with open(raw_path, mode='r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        genre_raw_objects = []

        for row in reader:

            genre_raw_objects.append(
                GenreRawAll(
                    danceability = row['danceability'],
                    energy = row['energy'],
                    key=row['key'],
                    loudness=row['loudness'],
                    mode=row['mode'],
                    acousticness=row['acousticness'],
                    instrumentalness=row['instrumentalness'],
                    liveness=row['liveness'],
                    valence=row['valence'],
                    tempo=row['tempo'],
                    type=row['type'],
                    id=row['id'],
                    uri=row['uri'],
                    track_href=row['track_href'],
                    analysis_url=row['analysis_url'],
                    duration_ms=row['duration_ms'],
                    time_signature=row['time_signature'],
                    genre=transform_case(row['genre']),


                )
            )
            session.bulk_save_objects(genre_raw_objects)
            session.commit()


def main():
    print("[Transform] start")
    print("[Transform] remove any old data from genre_raw_all table")
    #truncate_table('genre_raw_all')
    print("[Transform] transform new data available run transformation")
    transform_new_data()
    print("[Transform] end")

