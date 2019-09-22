# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Ontology.proto
class SigningInput(ProtoEntity):
    contract        = Field('string',	1, required=False)
    method          = Field('string',	2, required=False)
    owner_private_key = Field('bytes',	3, required=False)
    to_address      = Field('string',	4, required=False)
    amount          = Field('uint64',	5, required=False)
    payer_private_key = Field('bytes',	6, required=False)
    gas_price       = Field('uint64',	7, required=False)
    gas_limit       = Field('uint64',	8, required=False)
    query_address   = Field('string',	9, required=False)
    nonce           = Field('uint32',	10, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

