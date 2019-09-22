# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Nimiq.proto
class SigningInput(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    destination     = Field('string',	2, required=False)
    value           = Field('uint64',	3, required=False)
    fee             = Field('uint64',	4, required=False)
    validity_start_height = Field('uint32',	5, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

