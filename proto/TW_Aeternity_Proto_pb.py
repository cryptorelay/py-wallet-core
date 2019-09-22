# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Aeternity.proto
class SigningInput(ProtoEntity):
    from_address    = Field('string',	1, required=False)
    to_address      = Field('string',	2, required=False)
    amount          = Field('bytes',	3, required=False)
    fee             = Field('bytes',	4, required=False)
    payload         = Field('string',	5, required=False)
    ttl             = Field('uint64',	6, required=False)
    nonce           = Field('uint64',	7, required=False)
    private_key     = Field('bytes',	8, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('string',	1, required=False)
    signature       = Field('string',	2, required=False)

