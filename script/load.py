from sqlalchemy import cast, Float, Integer, delete, String
from sqlalchemy.dialects.postgresql import insert
from common.base import session
from common.tables import GenreRawAll, GenreCleanAll


def insert_tracks():
    # select track id
    clean_track_id = session.query(GenreCleanAll.track_id)

    # select columns and cast appropriate type when needed
    tracks_to_insert = session.query(
        cast(GenreRawAll.danceability, Float),
        cast(GenreRawAll.energy, Float),
        cast(GenreRawAll.key, Integer),
        cast(GenreRawAll.loudness, Float),
        cast(GenreRawAll.mode, Integer),
        cast(GenreRawAll.acousticness, Float),
        cast(GenreRawAll.instrumentalness, Float),
        cast(GenreRawAll.liveness, Float),
        cast(GenreRawAll.valence, Float),
        cast(GenreRawAll.tempo, Float),
        cast(GenreRawAll.type, String),
        cast(GenreRawAll.id, String),
        cast(GenreRawAll.uri, String),
        cast(GenreRawAll.track_href, String),
        cast(GenreRawAll.analysis_url, String),
        cast(GenreRawAll.duration_ms, Integer),
        cast(GenreRawAll.time_signature, Integer),
        cast(GenreRawAll.genre, String),
    ).filter(~GenreRawAll.track_id.in_(clean_track_id))

    # print number of transactions to insert
    print("Tracks to insert: ", tracks_to_insert.count())

    columns = [
        'danceability', 'energy', 'key', 'loudness', 'mode', 'acousticness', 'instrumentalness', 'liveness', 'valence',
        'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature', 'genre'
    ]

    stmt = insert(GenreCleanAll).from_select(columns, tracks_to_insert)

    session.execute(stmt)
    session.commit()


def delete_tracks():
    """
        Delete operation: delete any row not present in the last snapshot
    """
    raw_track_id = session.query(GenreRawAll.track_id)

    tracks_to_delete = session.query(GenreCleanAll).filter(~GenreCleanAll.track_id.in_(raw_track_id))

    # print number of transactions to delete
    print("Tracks to delete: ", tracks_to_delete.count())

    tracks_to_delete.delete(synchronize_session=False)
    session.commit()


def main():
    print("[Load] Start")
    print("[Load] Inserting new rows")
    insert_tracks()
    print("[Load] Deleting rows not available in the new transformed data")
    delete_tracks()
    print("[Load] End")
