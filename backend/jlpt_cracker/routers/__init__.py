from .kanji import router as kanji_router
from .vocabulary import router as vocabulary_router

ALL_ROUTERS = [
    kanji_router,
    vocabulary_router,
]
