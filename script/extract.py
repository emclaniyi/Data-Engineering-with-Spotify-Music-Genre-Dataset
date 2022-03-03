import csv
import os
import tempfile
from zipfile import ZipFile
import pandas as pd

base_path = "C:\\Users\\EM\\PycharmProjects\\SpotifyMusicRecommendation-Genre"
source_path = "C:\\Users\\EM\\Desktop\\NEWMOVE\\genres_v2.csv.zip"
raw_path = f"{base_path}/raw/data"


def create_directory_if_not_exist(path):
    """
    :param path:
    :return:
    """
    os.makedirs(os.path.dirname(path), exist_ok=False)


def extract_csv(source, raw):
    create_directory_if_not_exist(raw)
    with ZipFile(source, mode='r') as f:
        name_list = f.namelist()
        csv_file_path = f.extract(name_list[0], path=raw)
        csv_file = pd.read_csv(csv_file_path, low_memory=False)
        csv_file = csv_file.drop(['song_name', 'Unnamed: 0', 'title'], axis=1)
        csv_file.to_csv(f'{raw_path}/genres.csv')


#def save_new_raw_data():


def main():
    print("[Extract] start")
    print("[Extarct] create directory")
    extract_csv(source_path, raw_path)
    print(f"[Extract] saving data to '{raw_path}'")
    print("[Extract] end")
