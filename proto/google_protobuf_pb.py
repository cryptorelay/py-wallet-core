# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: google/protobuf/any.proto
class Any(ProtoEntity):
    type_url        = Field('string',	1, required=False)
    value           = Field('bytes',	2, required=False)

