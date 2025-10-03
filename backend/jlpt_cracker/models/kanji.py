from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Field, Relationship, SQLModel

from .links import KanjiVocabularyLink

if TYPE_CHECKING:
    from .vocabulary import Vocabulary


class KanjiBase(SQLModel):
    character: str = Field(index=True, unique=True, nullable=False)
    meaning: List[str] = Field(sa_column=Column(ARRAY(String)), default_factory=list)
    level: str
    onyomi: List[str] = Field(sa_column=Column(ARRAY(String)), default_factory=list)
    kunyomi: List[str] = Field(sa_column=Column(ARRAY(String)), default_factory=list)


class Kanji(KanjiBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vocabulary: List["Vocabulary"] = Relationship(
        back_populates="kanji", link_model=KanjiVocabularyLink
    )


class KanjiRead(KanjiBase):
    id: int


class KanjiCreate(KanjiBase):
    pass
