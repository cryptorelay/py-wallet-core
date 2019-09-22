# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Semux.proto
class SigningInput(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    destination     = Field('string',	2, required=False)
    value           = Field('uint64',	3, required=False)
    fee             = Field('uint64',	4, required=False)
    nonce           = Field('uint64',	5, required=False)
    timestamp       = Field('uint64',	6, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

