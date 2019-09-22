# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: ARK.proto
# enum TransactionType
Transfer=0
class SigningInput(ProtoEntity):
    type            = Field('enum',	1, required=False)
    amount          = Field('uint64',	2, required=False)
    fee             = Field('uint64',	3, required=False)
    to_address      = Field('string',	4, required=False)
    timestamp       = Field('uint32',	5, required=False)
    private_key     = Field('bytes',	6, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('string',	1, required=False)
    signature       = Field('bytes',	2, required=False)

