from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = "auto", index = True)
    user_id = Column(String(50), unique = True, nullable = False, index = True)
    user_hashed_password = Column(String, nullable = False)
    is_active = Column(Boolean, default = True)

    def __repr__(self):
        return f"<User(id={self.id}) user_id=${self.user_id} is_active={self.is_active}>"
