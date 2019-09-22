# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Nebulas.proto
class SigningInput(ProtoEntity):
    from_address    = Field('string',	1, required=False)
    chain_id        = Field('bytes',	2, required=False)
    nonce           = Field('bytes',	3, required=False)
    gas_price       = Field('bytes',	4, required=False)
    gas_limit       = Field('bytes',	5, required=False)
    to_address      = Field('string',	6, required=False)
    amount          = Field('bytes',	7, required=False)
    timestamp       = Field('bytes',	8, required=False)
    payload         = Field('string',	9, required=False)
    private_key     = Field('bytes',	10, required=False)

class SigningOutput(ProtoEntity):
    algorithm       = Field('uint32',	1, required=False)
    signature       = Field('bytes',	2, required=False)
    raw             = Field('string',	3, required=False)

class Data(ProtoEntity):
    type            = Field('string',	1, required=False)
    payload         = Field('bytes',	2, required=False)

class RawTransaction(ProtoEntity):
    hash            = Field('bytes',	1, required=False)
    from            = Field('bytes',	2, required=False)
    to              = Field('bytes',	3, required=False)
    value           = Field('bytes',	4, required=False)
    nonce           = Field('uint64',	5, required=False)
    timestamp       = Field('int64',	6, required=False)
    data            = Field(Data,	7, required=False)
    chain_id        = Field('uint32',	8, required=False)
    gas_price       = Field('bytes',	9, required=False)
    gas_limit       = Field('bytes',	10, required=False)
    alg             = Field('uint32',	11, required=False)
    sign            = Field('bytes',	12, required=False)

