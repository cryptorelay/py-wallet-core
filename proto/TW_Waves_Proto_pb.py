# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Waves.proto
class SigningInput(ProtoEntity):
    amount          = Field('int64',	1, required=False)
    asset           = Field('string',	2, required=False)
    fee             = Field('int64',	3, required=False)
    fee_asset       = Field('string',	4, required=False)
    to              = Field('string',	5, required=False)
    attachment      = Field('bytes',	6, required=False)
    timestamp       = Field('int64',	7, required=False)
    private_key     = Field('bytes',	8, required=False)

class SigningOutput(ProtoEntity):
    signature       = Field('bytes',	1, required=False)
    json            = Field('string',	2, required=False)

