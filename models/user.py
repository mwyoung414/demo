from db import demo_db

class User(demo_db.Model):
    __tablename__ = 'users'
    id = demo_db.Column(demo_db.Integer, primary_key=True)
    user_name = demo_db.Column(demo_db.String(80), unique=True, nullable=False)
    user_email = demo_db.Column(demo_db.String(255), unique=True, nullable=False)
    user_password = demo_db.Column(demo_db.String(255), nullable=False)
    last_login = demo_db.Column(demo_db.DateTime, nullable=False, default=demo_db.func.current_timestamp())
    user_type = demo_db.Column(demo_db.models.Integer, nullable=False)
    

    
