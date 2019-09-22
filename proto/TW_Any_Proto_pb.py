# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Any.proto
class SigningInput(ProtoEntity):
    coin_type       = Field('uint32',	1, required=False)
    transaction     = Field('string',	2, required=False)
    private_key     = Field('string',	3, required=False)

class SigningOutput(ProtoEntity):
    error           = Field('Error',	1, required=False)
    success         = Field('bool',	2, required=False)
    output          = Field('string',	4, required=False)

