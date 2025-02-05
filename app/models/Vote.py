from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Vote(Base):
    __tablename__='votes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    