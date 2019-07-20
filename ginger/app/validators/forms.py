'''
 Created by skywalkeryin on 7/15/19
'''


from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.base import db
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(),
                                     # password can only include letters , numbers and "_"
                                     Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
                                     ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("There already is a email in the system.")

    def validate_nickname(self, value):
        # ignore the status
        if User.query.filter(User.nickname == value.data).first():
            raise ValidationError("Please user another nickname.")