from db import demo_db

class UserType(demo_db.Model):
    __tablename__ = 'user_types'
    id = demo_db.Column(demo_db.Integer, primary_key=True)
    user_type_name = demo_db.Column(demo_db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return '<UserType %r>' % self.user_type_name