# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Theta.proto
class SigningInput(ProtoEntity):
    chain_id        = Field('string',	1, required=False)
    to_address      = Field('string',	2, required=False)
    theta_amount    = Field('bytes',	3, required=False)
    tfuel_amount    = Field('bytes',	4, required=False)
    sequence        = Field('uint64',	5, required=False)
    fee             = Field('bytes',	6, required=False)
    private_key     = Field('bytes',	7, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)

