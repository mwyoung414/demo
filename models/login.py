from db import demo_db

class Login(demo_db.Model):
    __tablename__ = 'login'
    id = demo_db.Column(demo_db.Integer, primary_key=True)
    user_name = demo_db.Column(demo_db.String(80), unique=True, nullable=False)
    pass_word_salt = demo_db.Column(demo_db.String(255), nullable=False)
    pass_word_hash = demo_db.Column(demo_db.String(255), nullable=False)
    user_id = demo_db.Column(demo_db.Integer, demo_db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Login %r>' % self.username