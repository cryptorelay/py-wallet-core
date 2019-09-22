# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Zilliqa.proto
class SigningInput(ProtoEntity):
    version         = Field('uint32',	1, required=False)
    nonce           = Field('uint64',	2, required=False)
    to_address      = Field('string',	3, required=False)
    amount          = Field('bytes',	4, required=False)
    gas_price       = Field('bytes',	5, required=False)
    gas_limit       = Field('uint64',	6, required=False)
    private_key     = Field('bytes',	7, required=False)
    code            = Field('bytes',	10, required=False)
    data            = Field('bytes',	11, required=False)

class SigningOutput(ProtoEntity):
    signature       = Field('bytes',	1, required=False)

