# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Bitcoin.proto
class OutPoint(ProtoEntity):
    hash            = Field('bytes',	1, required=False)
    index           = Field('uint32',	2, required=False)
    sequence        = Field('uint32',	3, required=False)

class TransactionInput(ProtoEntity):
    previousOutput  = Field(OutPoint,	1, required=False)
    sequence        = Field('uint32',	2, required=False)
    script          = Field('bytes',	3, required=False)

class TransactionOutput(ProtoEntity):
    value           = Field('int64',	1, required=False)
    script          = Field('bytes',	2, required=False)

class Transaction(ProtoEntity):
    version         = Field('sint32',	1, required=False)
    lockTime        = Field('uint32',	2, required=False)
    inputs          = Field(TransactionInput,	3, repeated=True)
    outputs         = Field(TransactionOutput,	4, repeated=True)

class UnspentTransaction(ProtoEntity):
    out_point       = Field(OutPoint,	1, required=False)
    script          = Field('bytes',	2, required=False)
    amount          = Field('int64',	3, required=False)

class SigningInput(ProtoEntity):
    hash_type       = Field('uint32',	1, required=False)
    amount          = Field('int64',	2, required=False)
    byte_fee        = Field('int64',	3, required=False)
    to_address      = Field('string',	4, required=False)
    change_address  = Field('string',	5, required=False)
    private_key     = Field('bytes',	10, repeated=True)
    scripts         = Field('ScriptsEntry',	11, repeated=True)
    utxo            = Field(UnspentTransaction,	12, repeated=True)
    use_max_amount  = Field('bool',	13, required=False)
    coin_type       = Field('uint32',	14, required=False)

class TransactionPlan(ProtoEntity):
    amount          = Field('int64',	1, required=False)
    available_amount = Field('int64',	2, required=False)
    fee             = Field('int64',	3, required=False)
    change          = Field('int64',	4, required=False)
    utxos           = Field(UnspentTransaction,	5, repeated=True)

class SigningOutput(ProtoEntity):
    transaction     = Field(Transaction,	1, required=False)
    encoded         = Field('bytes',	2, required=False)
    fee             = Field('int64',	3, required=False)
    max_amount      = Field('int64',	4, required=False)
    transaction_id  = Field('string',	5, required=False)

