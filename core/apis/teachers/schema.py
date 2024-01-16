from marshmallow import  EXCLUDE,  post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher
# from core.libs.helpers import GeneralObject

# from marshmallow import fields

class TeacherSchema(SQLAlchemyAutoSchema):
   
    # username = fields.String(dump_only=True)
    # email = fields.String(dump_only=True)

    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    user_id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Teacher(**data_dict)
     # Exclude the 'user' field during serialization
    # def pre_dump(self, data, **kwargs):
    #     data.pop('user', None)
    #     return data