# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Aion.proto
class SigningInput(ProtoEntity):
    nonce           = Field('bytes',	1, required=False)
    gas_price       = Field('bytes',	2, required=False)
    gas_limit       = Field('bytes',	3, required=False)
    to_address      = Field('string',	4, required=False)
    amount          = Field('bytes',	5, required=False)
    payload         = Field('bytes',	6, required=False)
    private_key     = Field('bytes',	7, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)

