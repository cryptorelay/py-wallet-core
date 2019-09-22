# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Binance.proto
class Transaction(ProtoEntity):
    msgs            = Field('bytes',	1, repeated=True)
    signatures      = Field('bytes',	2, repeated=True)
    memo            = Field('string',	3, required=False)
    source          = Field('int64',	4, required=False)
    data            = Field('bytes',	5, required=False)

class Signature(ProtoEntity):
    pub_key         = Field('bytes',	1, required=False)
    signature       = Field('bytes',	2, required=False)
    account_number  = Field('int64',	3, required=False)
    sequence        = Field('int64',	4, required=False)

class TradeOrder(ProtoEntity):
    sender          = Field('bytes',	1, required=False)
    id              = Field('string',	2, required=False)
    symbol          = Field('string',	3, required=False)
    ordertype       = Field('int64',	4, required=False)
    side            = Field('int64',	5, required=False)
    price           = Field('int64',	6, required=False)
    quantity        = Field('int64',	7, required=False)
    timeinforce     = Field('int64',	8, required=False)

class CancelTradeOrder(ProtoEntity):
    sender          = Field('bytes',	1, required=False)
    symbol          = Field('string',	2, required=False)
    refid           = Field('string',	3, required=False)

class SendOrder(ProtoEntity):
    inputs          = Field('Input',	1, repeated=True)
    outputs         = Field('Output',	2, repeated=True)

class TokenFreezeOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    symbol          = Field('string',	2, required=False)
    amount          = Field('int64',	3, required=False)

class TokenUnfreezeOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    symbol          = Field('string',	2, required=False)
    amount          = Field('int64',	3, required=False)

class HTLTOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    to              = Field('bytes',	2, required=False)
    recipient_other_chain = Field('string',	3, required=False)
    sender_other_chain = Field('string',	4, required=False)
    random_number_hash = Field('bytes',	5, required=False)
    timestamp       = Field('int64',	6, required=False)
    amount          = Field('Token',	7, repeated=True)
    expected_income = Field('string',	8, required=False)
    height_span     = Field('int64',	9, required=False)
    cross_chain     = Field('bool',	10, required=False)

class DepositHTLTOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    amount          = Field('Token',	2, repeated=True)
    swap_id         = Field('bytes',	3, required=False)

class ClaimHTLOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    swap_id         = Field('bytes',	2, required=False)
    random_number   = Field('bytes',	3, required=False)

class RefundHTLTOrder(ProtoEntity):
    from            = Field('bytes',	1, required=False)
    swap_id         = Field('bytes',	2, required=False)

class SigningInput(ProtoEntity):
    chain_id        = Field('string',	1, required=False)
    account_number  = Field('int64',	2, required=False)
    sequence        = Field('int64',	3, required=False)
    source          = Field('int64',	4, required=False)
    memo            = Field('string',	5, required=False)
    private_key     = Field('bytes',	6, required=False)
    trade_order     = Field(TradeOrder,	8, required=False)
    cancel_trade_order = Field(CancelTradeOrder,	9, required=False)
    send_order      = Field(SendOrder,	10, required=False)
    freeze_order    = Field(TokenFreezeOrder,	11, required=False)
    unfreeze_order  = Field(TokenUnfreezeOrder,	12, required=False)
    htlt_order      = Field(HTLTOrder,	13, required=False)
    depositHTLT_order = Field(DepositHTLTOrder,	14, required=False)
    claimHTLT_order = Field(ClaimHTLOrder,	15, required=False)
    refundHTLT_order = Field(RefundHTLTOrder,	16, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)

