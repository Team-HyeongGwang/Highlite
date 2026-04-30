from sqlalchemy import Column, Integer, String, Float, JSON, ForeignKey
from db.database import Base

''' 예시
class User(Base):
    __tablename__ = "users" # Supabase에 생성될 실제 테이블 이름

    id = Column(Integer, primary_key=True, index=True)
    user_id_str = Column(String, unique=True, index=True)
    custom_criteria = Column(String, nullable=True) # "노란색은 1점..." 같은 사용자 설정
'''