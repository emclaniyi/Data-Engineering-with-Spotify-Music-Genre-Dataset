from sqlalchemy import Column, Float, Integer, String
import common.base as b
from sqlalchemy.orm import column_property


class GenreRawAll(b.Base):
    __tablename__ = "genre_raw_all"
    dancebility = Column(String(55))
    energy = Column(String(55))
    key = Column(String(55))
    loudness = Column(String(55))
    mode = Column(String(55))
    acousticness = Column(String(55))
    instrumentalness = Column(String(55))
    liveness = Column(String(55))
    valence = Column(String(55))
    tempo = Column(String(55))
    type = Column(String(55))
    id = Column(String(500), primary_key=True, nullable=True)
    uri = Column(String(500))
    track_href = Column(String(500))
    analysis_url = Column(String(500))
    duration_ms = Column(String(50))
    time_signature = Column(String(255))
    genre = Column(String(255))
    track_id = column_property(
        uri + "_" + track_href + "_" + analysis_url
    )


class GenreCleanAll(b.Base):
    __tablename__ = "genre_clean_all"
    dancebility = Column(Float)
    energy = Column(Float)
    key = Column(Integer)
    loudness = Column(Float)
    mode = Column(Integer)
    acousticness = Column(Float)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    valence = Column(Float)
    tempo = Column(Float)
    type = Column(String(255))
    id = Column(String(500), primary_key=True, nullable=True)
    uri = Column(String(500))
    track_href = Column(String(500))
    analysis_url = Column(String(500))
    duration_ms = Column(Integer)
    time_signature = Column(Integer)
    genre = Column(String(255))
    track_id = column_property(
        uri + "_" + track_href + "_" + analysis_url
    )
