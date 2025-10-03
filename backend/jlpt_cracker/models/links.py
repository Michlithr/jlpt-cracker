from typing import Optional

from sqlmodel import Field, SQLModel


class KanjiVocabularyLink(SQLModel, table=True):
    kanji_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="kanji.id"
    )
    vocabulary_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="vocabulary.id"
    )
