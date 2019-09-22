# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Bravo.proto
class SigningInput(ProtoEntity):
    chain_id        = Field('bytes',	1, required=False)
    sender          = Field('string',	2, required=False)
    recipient       = Field('string',	3, required=False)
    amount          = Field('double',	4, required=False)
    testnet         = Field('bool',	5, required=False)
    memo            = Field('string',	6, required=False)
    reference_block_id = Field('bytes',	7, required=False)
    reference_block_time = Field('sfixed32',	8, required=False)
    private_key     = Field('bytes',	9, required=False)

class SigningOutput(ProtoEntity):
    json_encoded    = Field('string',	1, required=False)

