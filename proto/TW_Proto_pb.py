# coding: utf-8
from cprotobuf import ProtoEntity, Field
from .google_protobuf_pb import Any
# file: Common.proto
class Result(ProtoEntity):
    success         = Field('bool',	1, required=False)
    error           = Field('string',	2, required=False)
    objects         = Field(Any,	3, repeated=True)

