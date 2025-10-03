from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    # column larni yarating
    id = Column(Integer,primary_key=True,index=True)

    username = Column(String,nullable=False,unique=True)
    email = Column(String,nullable=False)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    # column larni yarating
    id = Column(Integer,primary_key=True,index=True)

    title = Column(String,nullable=False)
    body = Column(String,nullable=False)
    user_id = Column(ForeignKey("users.id"),nullable=False)

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    # column larni yarating
    id = Column(Integer,primary_key=True,index=True)

    text = Column(String,nullable=False)
    
    user_id = Column(ForeignKey("users.id"),nullable=False)
    post_id = Column(ForeignKey('posts.id'),nullable=False)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
