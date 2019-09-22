# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Tezos.proto
class SigningOutput(ProtoEntity):
    signed_bytes    = Field('bytes',	1, required=False)

class TransactionOperationData(ProtoEntity):
    destination     = Field('string',	1, required=False)
    amount          = Field('int64',	2, required=False)

class RevealOperationData(ProtoEntity):
    public_key      = Field('bytes',	1, required=False)

class OriginationOperationData(ProtoEntity):
    manager_pubkey  = Field('string',	1, required=False)
    balance         = Field('int64',	2, required=False)

class DelegationOperationData(ProtoEntity):
    delegate        = Field('string',	1, required=False)

class Operation(ProtoEntity):
    # enum OperationKind
    ENDORSEMENT=0
    REVEAL=7
    TRANSACTION=8
    ORIGINATION=9
    DELEGATION=10
    counter         = Field('int64',	1, required=False)
    source          = Field('string',	2, required=False)
    fee             = Field('int64',	3, required=False)
    gas_limit       = Field('int64',	4, required=False)
    storage_limit   = Field('int64',	5, required=False)
    kind            = Field('enum',	7, required=False)
    reveal_operation_data = Field(RevealOperationData,	8, required=False)
    transaction_operation_data = Field(TransactionOperationData,	9, required=False)
    origination_operation_data = Field(OriginationOperationData,	10, required=False)
    delegation_operation_data = Field(DelegationOperationData,	11, required=False)

class OperationList(ProtoEntity):
    branch          = Field('string',	1, required=False)
    operations      = Field(Operation,	2, repeated=True)

class SigningInput(ProtoEntity):
    operation_list  = Field(OperationList,	1, required=False)
    private_key     = Field('bytes',	2, required=False)

