# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Solana.proto
class Transfer(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    recipient       = Field('string',	2, required=False)
    value           = Field('uint64',	3, required=False)

class Stake(ProtoEntity):
    from_private_key = Field('bytes',	1, required=False)
    stake_private_key = Field('bytes',	2, required=False)
    vote_pubkey     = Field('string',	3, required=False)
    value           = Field('uint64',	4, required=False)

class DeactivateStake(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    vote_pubkey     = Field('string',	2, required=False)

class WithdrawStake(ProtoEntity):
    private_key     = Field('bytes',	1, required=False)
    recipient       = Field('string',	2, required=False)
    value           = Field('uint64',	3, required=False)

class SigningInput(ProtoEntity):
    transfer_transaction = Field(Transfer,	1, required=False)
    stake_transaction = Field(Stake,	2, required=False)
    deactivate_stake_transaction = Field(DeactivateStake,	3, required=False)
    withdraw_transaction = Field(WithdrawStake,	4, required=False)
    recent_blockhash = Field('string',	5, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

