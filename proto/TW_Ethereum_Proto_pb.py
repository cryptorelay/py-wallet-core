# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Ethereum.proto
class SigningInput(ProtoEntity):
    chain_id        = Field('bytes',	1, required=False)
    nonce           = Field('bytes',	2, required=False)
    gas_price       = Field('bytes',	3, required=False)
    gas_limit       = Field('bytes',	4, required=False)
    to_address      = Field('string',	5, required=False)
    amount          = Field('bytes',	6, required=False)
    payload         = Field('bytes',	7, required=False)
    private_key     = Field('bytes',	8, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)
    v               = Field('bytes',	2, required=False)
    r               = Field('bytes',	3, required=False)
    s               = Field('bytes',	4, required=False)

