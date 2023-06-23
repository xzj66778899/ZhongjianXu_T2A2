from init import db,ma
from marshmallow import fields


class User_has_hobby(db.Model):
    __tablename__ = 'users_have_hobbies'

    id = db.Column(db.Integer, primary_key=True)
   
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('User', back_populates = 'users_have_hobbies')

    hobby_id = db.Column(db.Integer, db.ForeignKey('hobbies.id'), nullable=False)
    hobbies = db.relationship('Hobby', back_populates = 'users_have_hobbies')


class User_has_hobbySchema(ma.Schema):
    users = fields.Nested('UserSchema', exclude = ['password', 'is_admin'])
    hobbies = fields.Nested('HobbySchema')

    class Meta:
        fields = ('id','hobby_id','users','hobbies')

