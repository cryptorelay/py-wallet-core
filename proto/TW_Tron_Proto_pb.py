# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Tron.proto
class TransferContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    to_address      = Field('string',	2, required=False)
    amount          = Field('int64',	3, required=False)

class TransferAssetContract(ProtoEntity):
    asset_name      = Field('string',	1, required=False)
    owner_address   = Field('string',	2, required=False)
    to_address      = Field('string',	3, required=False)
    amount          = Field('int64',	4, required=False)

class FreezeBalanceContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    frozen_balance  = Field('int64',	2, required=False)
    frozen_duration = Field('int64',	3, required=False)
    resource        = Field('string',	10, required=False)
    receiver_address = Field('string',	15, required=False)

class UnfreezeBalanceContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    resource        = Field('string',	10, required=False)
    receiver_address = Field('string',	15, required=False)

class UnfreezeAssetContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)

class VoteAssetContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    vote_address    = Field('string',	2, repeated=True)
    support         = Field('bool',	3, required=False)
    count           = Field('int32',	5, required=False)

class VoteWitnessContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    votes           = Field('Vote',	2, repeated=True)
    support         = Field('bool',	3, required=False)

class WithdrawBalanceContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)

class TriggerSmartContract(ProtoEntity):
    owner_address   = Field('string',	1, required=False)
    contract_address = Field('string',	2, required=False)
    call_value      = Field('int64',	3, required=False)
    data            = Field('bytes',	4, required=False)
    call_token_value = Field('int64',	5, required=False)
    token_id        = Field('int64',	6, required=False)

class BlockHeader(ProtoEntity):
    timestamp       = Field('int64',	1, required=False)
    tx_trie_root    = Field('bytes',	2, required=False)
    parent_hash     = Field('bytes',	3, required=False)
    number          = Field('int64',	7, required=False)
    witness_address = Field('bytes',	9, required=False)
    version         = Field('int32',	10, required=False)

class Transaction(ProtoEntity):
    timestamp       = Field('int64',	1, required=False)
    expiration      = Field('int64',	2, required=False)
    block_header    = Field(BlockHeader,	3, required=False)
    transfer        = Field(TransferContract,	10, required=False)
    transfer_asset  = Field(TransferAssetContract,	11, required=False)
    freeze_balance  = Field(FreezeBalanceContract,	12, required=False)
    unfreeze_balance = Field(UnfreezeBalanceContract,	13, required=False)
    unfreeze_asset  = Field(UnfreezeAssetContract,	14, required=False)
    withdraw_balance = Field(WithdrawBalanceContract,	15, required=False)
    vote_asset      = Field(VoteAssetContract,	16, required=False)
    vote_witness    = Field(VoteWitnessContract,	17, required=False)
    trigger_smart_contract = Field(TriggerSmartContract,	18, required=False)

class SigningInput(ProtoEntity):
    transaction     = Field(Transaction,	1, required=False)
    private_key     = Field('bytes',	2, required=False)

class SigningOutput(ProtoEntity):
    id              = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)
    ref_block_bytes = Field('bytes',	3, required=False)
    ref_block_hash  = Field('bytes',	4, required=False)

