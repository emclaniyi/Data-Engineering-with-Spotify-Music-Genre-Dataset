from base import Base, engine
from tables import GenreRawAll, GenreCleanAll

for table in Base.metadata.tables:
    print(table)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
