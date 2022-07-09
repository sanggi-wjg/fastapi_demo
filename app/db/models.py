from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class UserEntity(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = "auto", index = True)

    user_email = Column(String(50), unique = True, nullable = False, index = True)
    user_hashed_password = Column(String(250), nullable = False)
    is_active = Column(Boolean, default = True)

    # 역방향 relation
    items = relationship("ItemEntity", back_populates = "owner")

    def __repr__(self):
        return f"<User(id={self.id}) user_id={self.user_email} is_active={self.is_active}>"


class ItemEntity(Base):
    __tablename__ = 'items'
    __table_args__ = (
        UniqueConstraint('item_name', 'owner_id', name = 'unique_item_by_owner_id'),
    )

    id = Column(Integer, primary_key = True, autoincrement = "auto", index = True)

    item_name = Column(String(100), nullable = False, index = True)
    item_description = Column(String(250), index = True)
    item_price = Column(Numeric(10, 2))
    item_tax = Column(Numeric(10, 2))

    # 정방향 relation
    owner_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    owner = relationship("UserEntity", back_populates = "items")

    def __repr__(self):
        return f"<User(id={self.id}) item_name={self.item_name} item_description={self.item_description} item_price={self.item_price} item_description={self.item_tax}>"


class TTSRecordEntity(Base):
    __tablename__ = 'tts_records'
    __table_args__ = (
        UniqueConstraint('record_text', name = 'unique_tts_records_record_text'),
    )

    id = Column(Integer, primary_key = True, autoincrement = "auto", index = True)
    record_text = Column(String(100), nullable = False, index = True)

    def __repr__(self):
        return f"<TTSRecordEntity (id={self.id}) record_text={self.record_text}>"
