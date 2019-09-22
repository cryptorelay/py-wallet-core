# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Nano.proto
class SigningInput(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    parent_block    = Field('bytes',	2, required=False)
    link_block      = Field('bytes',	3, required=False)
    link_recipient  = Field('string',	4, required=False)
    representative  = Field('string',	5, required=False)
    balance         = Field('string',	6, required=False)

class SigningOutput(ProtoEntity):
    signature       = Field('bytes',	1, required=False)
    block_hash      = Field('bytes',	2, required=False)

