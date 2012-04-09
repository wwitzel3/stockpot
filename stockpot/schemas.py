from colander import (
    MappingSchema,
    SchemaNode,
    String,
    )

class User(MappingSchema):
    username = SchemaNode(String())
    email = SchemaNode(String())
    password = SchemaNode(String())

class Login(MappingSchema):
    email = SchemaNode(String())
    password = SchemaNode(String())

