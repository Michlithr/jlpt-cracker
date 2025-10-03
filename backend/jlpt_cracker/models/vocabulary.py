from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Field, Relationship, SQLModel

from .links import KanjiVocabularyLink

if TYPE_CHECKING:
    from .kanji import Kanji


class VocabularyBase(SQLModel):
    word: str = Field(index=True, unique=True, nullable=False)
    reading: str
    meaning: List[str] = Field(sa_column=Column(ARRAY(String)), default_factory=list)
    level: str


class Vocabulary(VocabularyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    kanji: List["Kanji"] = Relationship(
        back_populates="vocabulary",
        link_model=KanjiVocabularyLink,
    )


class VocabularyRead(VocabularyBase):
    id: int


class VocabularyCreate(VocabularyBase):
    pass
