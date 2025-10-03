from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..database import get_session
from ..models import Vocabulary, VocabularyCreate, VocabularyRead

router = APIRouter(prefix="/vocabulary", tags=["Vocabulary"])


@router.post("/", response_model=VocabularyRead, status_code=status.HTTP_201_CREATED)
async def create_vocabulary(
    vocabulary: VocabularyCreate, session: AsyncSession = Depends(get_session)
):
    db_vocabulary = Vocabulary.model_validate(vocabulary)

    session.add(db_vocabulary)
    await session.commit()
    await session.refresh(db_vocabulary)
    return db_vocabulary


@router.get("/", response_model=List[VocabularyRead])
async def read_vocabulary_list(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Vocabulary))
    vocabulary_list = result.all()
    return vocabulary_list
