# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Decred.proto
class TransactionInput(ProtoEntity):
    previousOutput  = Field(OutPoint,	1, required=False)
    sequence        = Field('uint32',	2, required=False)
    valueIn         = Field('int64',	3, required=False)
    blockHeight     = Field('uint32',	4, required=False)
    blockIndex      = Field('uint32',	5, required=False)
    script          = Field('bytes',	6, required=False)

class TransactionOutput(ProtoEntity):
    value           = Field('int64',	1, required=False)
    version         = Field('uint32',	2, required=False)
    script          = Field('bytes',	3, required=False)

class Transaction(ProtoEntity):
    serializeType   = Field('uint32',	1, required=False)
    version         = Field('uint32',	2, required=False)
    inputs          = Field(TransactionInput,	3, repeated=True)
    outputs         = Field(TransactionOutput,	4, repeated=True)
    lockTime        = Field('uint32',	5, required=False)
    expiry          = Field('uint32',	6, required=False)

class SigningOutput(ProtoEntity):
    transaction     = Field(Transaction,	1, required=False)
    encoded         = Field('bytes',	2, required=False)
    fee             = Field('int64',	3, required=False)
    max_amount      = Field('int64',	4, required=False)
    transaction_id  = Field('string',	5, required=False)

