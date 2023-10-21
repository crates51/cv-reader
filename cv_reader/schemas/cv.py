from marshmallow import fields, Schema


class ExperienceSchema(Schema):
    title = fields.Str()
    company = fields.Str()
    location = fields.Str()
    description = fields.List(fields.Str())


class EducationSchema(Schema):
    location = fields.Str()
    institution = fields.Str()
    degree = fields.Str()
    dates = fields.Str()


class CVSchema(Schema):
    class Meta:
        type_ = 'cv'
    id = fields.UUID()
    skills = fields.Dict(load_default = None)
    personal = fields.Dict(load_default = None)
    education = fields.List(fields.Nested(EducationSchema), dump_default = [])
    experience = fields.List(fields.Nested(ExperienceSchema), dump_default = [])
