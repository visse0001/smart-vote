from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    Float,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from settings import PostgresConfiguration
from sqlalchemy.dialects.postgresql import UUID

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)
meta = MetaData(engine)
Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description = Column(String)
    public_key = Column(String)
    private_key = Column(String)
    vote_id = relationship("")
    id_person = relationship("Vote", uselist=False, back_populates="answers")


class Vote(Base):
    __tablename__ = 'votes'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    category = Column(String)
    description = Column(String)
    is_active = Column(Boolean)
    person_id = Column(UUID(as_uuid=True), ForeignKey('answers.id'))


