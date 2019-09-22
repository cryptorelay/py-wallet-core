# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: IOST.proto
# enum Algorithm
UNKNOWN=0
SECP256K1=1
ED25519=2
class Action(ProtoEntity):
    contract        = Field('string',	1, required=False)
    action_name     = Field('string',	2, required=False)
    data            = Field('string',	3, required=False)

class AmountLimit(ProtoEntity):
    token           = Field('string',	1, required=False)
    value           = Field('string',	2, required=False)

class Signature(ProtoEntity):
    algorithm       = Field('enum',	1, required=False)
    signature       = Field('bytes',	2, required=False)
    public_key      = Field('bytes',	3, required=False)

class Transaction(ProtoEntity):
    time            = Field('int64',	1, required=False)
    expiration      = Field('int64',	2, required=False)
    gas_ratio       = Field('double',	3, required=False)
    gas_limit       = Field('double',	4, required=False)
    delay           = Field('int64',	5, required=False)
    chain_id        = Field('uint32',	6, required=False)
    actions         = Field(Action,	7, repeated=True)
    amount_limit    = Field(AmountLimit,	8, repeated=True)
    signers         = Field('string',	9, repeated=True)
    signatures      = Field(Signature,	10, repeated=True)
    publisher       = Field('string',	11, required=False)
    publisher_sigs  = Field(Signature,	12, repeated=True)

class AccountInfo(ProtoEntity):
    name            = Field('string',	1, required=False)
    active_key      = Field('bytes',	2, required=False)
    owner_key       = Field('bytes',	3, required=False)

class SigningInput(ProtoEntity):
    account         = Field(AccountInfo,	1, required=False)
    transaction_template = Field(Transaction,	2, required=False)
    transfer_destination = Field('string',	3, required=False)
    transfer_amount = Field('string',	4, required=False)
    transfer_memo   = Field('string',	5, required=False)

class SigningOutput(ProtoEntity):
    transaction     = Field(Transaction,	1, required=False)

