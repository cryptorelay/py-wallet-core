# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Cosmos.proto
class Amount(ProtoEntity):
    denom           = Field('string',	1, required=False)
    amount          = Field('int64',	2, required=False)

class Fee(ProtoEntity):
    amounts         = Field(Amount,	1, repeated=True)
    gas             = Field('uint64',	2, required=False)

class SendCoinsMessage(ProtoEntity):
    from_address    = Field('string',	1, required=False)
    to_address      = Field('string',	2, required=False)
    amounts         = Field(Amount,	3, repeated=True)
    type_prefix     = Field('string',	4, required=False)

class StakeMessage(ProtoEntity):
    delegator_address = Field('string',	1, required=False)
    validator_address = Field('string',	2, required=False)
    amount          = Field(Amount,	3, required=False)
    type_prefix     = Field('string',	4, required=False)

class WithdrawStakeRewardMessage(ProtoEntity):
    delegator_address = Field('string',	1, required=False)
    validator_address = Field('string',	2, required=False)
    type_prefix     = Field('string',	3, required=False)

class Signature(ProtoEntity):
    public_key      = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)

class Transaction(ProtoEntity):
    fee             = Field(Fee,	1, required=False)
    memo            = Field('string',	2, required=False)
    signature       = Field(Signature,	3, required=False)
    send_coins_message = Field(SendCoinsMessage,	4, required=False)
    stake_message   = Field(StakeMessage,	5, required=False)
    unstake_message = Field(StakeMessage,	6, required=False)
    withdraw_stake_reward_message = Field(WithdrawStakeRewardMessage,	7, required=False)

class SigningInput(ProtoEntity):
    account_number  = Field('uint64',	1, required=False)
    chain_id        = Field('string',	2, required=False)
    fee             = Field(Fee,	3, required=False)
    memo            = Field('string',	4, required=False)
    sequence        = Field('uint64',	5, required=False)
    private_key     = Field('bytes',	6, required=False)
    send_coins_message = Field(SendCoinsMessage,	7, required=False)
    stake_message   = Field(StakeMessage,	8, required=False)
    unstake_message = Field(StakeMessage,	9, required=False)
    withdraw_stake_reward_message = Field(WithdrawStakeRewardMessage,	10, required=False)
    type_prefix     = Field('string',	11, required=False)

class SigningOutput(ProtoEntity):
    signature       = Field('bytes',	1, required=False)
    json            = Field('string',	2, required=False)

