from sqlalchemy.orm import Session
from models import User, Post, Comment


# CRUD
def create_user(db: Session, username: str, email: str):
    new_user = User(
        username = username,
        email = email
    )

    db.add(new_user)
    db.commit()

    return new_user

def create_post(db: Session, user_id: int, title: str, body: str):
    new_post = Post(
        user_id = user_id,
        title = title,
        body = body
    )

    db.add(new_post)
    db.commit()

    return new_post

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    new_comment = Comment(
        user_id = user_id,
        post_id = post_id,
        text = text
    )
    db.add(new_comment)
    db.commit()

    return new_comment

def update_post(db: Session, post_id: int, title: str, body: str):
    post = db.query(Post).filter(Post.post_id == post_id).first()

    if post:
        post.title = title,
        post.body = body

        db.commit()
        db.refresh(post)

        return post

    else:
        raise ValueError("Bunday post mavjud emas?")

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.post_id == post_id).first()

    if post:
        db.delete(post)
        db.commit()
    else:
        raise ValueError('Bunday id dagi post mavjud emas!')
    

# Queries
def get_user_posts(db: Session, user_id: int):
    post = db.query(Post).filter(Post.user_id == user_id)

    if post:
        return post
    else:
        raise ValueError('Bunday id dagi post yoq')

def get_post_comment_count(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id)

    if post:
        return(len(post.comments))
    else:
        raise ValueError('bu postda comment mavjud emas!')

def get_latest_posts(db: Session, limit: int = 5):
    pass

def search_posts_by_title(db: Session, keyword: str):
    pass

def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    pass
