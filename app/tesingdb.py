from app import db

db.create_all()

# user_1 = User(username='Becky',email='becky@mail.com',password='password')
# db.session.add(user_1)
#
# user_2 = User(username='JohnDoe',email='jd@mail.com',password='password')
# db.session.add(user_2)
# db.session.commit()
#
# post_1 = Post(title='Post 1', content='First Post Content',user_id=user.id)
# post_2 = Post(title='Post 2', content='Second Post Content',user_id=user.id)
# db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()