from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..database import get_session
from ..models import Kanji, KanjiCreate, KanjiRead

router = APIRouter(prefix="/kanji", tags=["Kanji"])


@router.post("/", response_model=KanjiRead, status_code=status.HTTP_201_CREATED)
async def create_kanji(
    kanji: KanjiCreate, session: AsyncSession = Depends(get_session)
):
    db_kanji = Kanji.model_validate(kanji)

    session.add(db_kanji)
    await session.commit()
    await session.refresh(db_kanji)
    return db_kanji


@router.get("/", response_model=List[KanjiRead])
async def read_kanji_list(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Kanji))
    kanji_list = result.all()
    return kanji_list
