import json
from database import Base, engine, SessionLocal
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    db = SessionLocal()
    with open("demo_data.json", "r",encoding="utf-8") as f:
        data = json.load(f)


    # Users larni kriting

    users = data['users']

    user_data = []
    for item in users:
        user = User(
            username = item['username'],
            email = item['email']
        )
        user_data.append(user)

    
    db.bulk_save_objects(user_data)
    db.commit()

    # Posts larni kriting
    posts = data['posts']
    post_data = []

    for item in posts:
        post = Post(
            title = item['title'],
            body = item['body'],
            user_id = item['user_id']
        )

        post_data.append(post)
    db.bulk_save_objects(post_data)
    db.commit()

    # Comments larni kriting
    comments = data['comments']

    comment_data = []
    for item in comments:
        comment = Comment(
            text = item['text'],
            user_id = item['user_id'],
            post_id = item['post_id']
        )
        comment_data.append(comment)

    db.bulk_save_objects(comment_data)
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    print("✅ Database initialized and demo data loaded!")
