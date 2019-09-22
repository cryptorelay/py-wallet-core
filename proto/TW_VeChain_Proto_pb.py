# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: VeChain.proto
class Clause(ProtoEntity):
    to              = Field('string',	1, required=False)
    value           = Field('bytes',	2, required=False)
    data            = Field('bytes',	3, required=False)

class SigningInput(ProtoEntity):
    chain_tag       = Field('uint32',	1, required=False)
    block_ref       = Field('uint64',	2, required=False)
    expiration      = Field('uint32',	3, required=False)
    clauses         = Field(Clause,	4, repeated=True)
    gas_price_coef  = Field('uint32',	5, required=False)
    gas             = Field('uint64',	6, required=False)
    depends_on      = Field('bytes',	7, required=False)
    nonce           = Field('uint64',	8, required=False)
    private_key     = Field('bytes',	9, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)

