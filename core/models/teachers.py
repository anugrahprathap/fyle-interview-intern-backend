from core import db
from core.libs import helpers
# from core.models.users import User

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id
    @classmethod
    def get_all_teachers_principal(cls):
        # Join the Teacher and User tables on user_id
        # query = db.session.query(cls).all()
        # query = (
        #     db.session.query(cls, User.username, User.email)
        #     .join(User, cls.user_id == User.id)
        #     .all()
        # )
        # teachers_data = [
        #     {
        #         'id': teacher.id,
        #         'user_id': teacher.user_id,
        #         'created_at': teacher.created_at,
        #         'updated_at': teacher.updated_at,
        #         'username': username,
        #         'email': email
        #     }
        #     for teacher, username, email in query
        # ]

        return cls.query.all()

     
        

