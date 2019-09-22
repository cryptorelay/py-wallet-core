# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Ripple.proto
class SigningInput(ProtoEntity):
    amount          = Field('int64',	1, required=False)
    fee             = Field('int64',	2, required=False)
    sequence        = Field('int32',	3, required=False)
    last_ledger_sequence = Field('int32',	4, required=False)
    account         = Field('string',	5, required=False)
    destination     = Field('string',	6, required=False)
    destination_tag = Field('int64',	7, required=False)
    flags           = Field('int64',	8, required=False)
    private_key     = Field('bytes',	9, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

