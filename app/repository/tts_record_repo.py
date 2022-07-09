from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.db.models import TTSRecordEntity


def is_exist_tts_record(db: Session, text: str) -> bool:
    try:
        db.query(TTSRecordEntity).filter(
            TTSRecordEntity.record_text == text
        ).one()
        return True
    except NoResultFound:
        return False


def create_tts_record(db: Session, text: str) -> TTSRecordEntity:
    new_tts_record = TTSRecordEntity(record_text = text)
    db.add(new_tts_record)
    db.commit()
    db.refresh(new_tts_record)
    return new_tts_record
