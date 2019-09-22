# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: EOS.proto
# enum KeyType
LEGACY=0
MODERNK1=1
MODERNR1=2
class Asset(ProtoEntity):
    amount          = Field('int64',	1, required=False)
    decimals        = Field('uint32',	2, required=False)
    symbol          = Field('string',	3, required=False)

class SigningInput(ProtoEntity):
    chain_id        = Field('bytes',	1, required=False)
    reference_block_id = Field('bytes',	2, required=False)
    reference_block_time = Field('sfixed32',	3, required=False)
    currency        = Field('string',	4, required=False)
    sender          = Field('string',	5, required=False)
    recipient       = Field('string',	6, required=False)
    memo            = Field('string',	7, required=False)
    asset           = Field(Asset,	8, required=False)
    private_key     = Field('bytes',	9, required=False)
    private_key_type = Field('enum',	10, required=False)

class SigningOutput(ProtoEntity):
    json_encoded    = Field('string',	1, required=False)

