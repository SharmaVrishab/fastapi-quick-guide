from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    hero = Hero(name="Deadpond", secret_name="Dive Wilson")
    session.add(hero)
    session.commit()
