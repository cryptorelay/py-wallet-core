# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Icon.proto
class SigningInput(ProtoEntity):
    from_address    = Field('string',	1, required=False)
    to_address      = Field('string',	2, required=False)
    value           = Field('bytes',	3, required=False)
    step_limit      = Field('bytes',	4, required=False)
    timestamp       = Field('int64',	5, required=False)
    nonce           = Field('bytes',	6, required=False)
    network_id      = Field('bytes',	7, required=False)
    private_key     = Field('bytes',	8, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('string',	1, required=False)
    signature       = Field('bytes',	2, required=False)

