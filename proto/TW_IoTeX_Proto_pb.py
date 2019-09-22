# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: IoTeX.proto
class Transfer(ProtoEntity):
    amount          = Field('string',	1, required=False)
    recipient       = Field('string',	2, required=False)
    payload         = Field('bytes',	3, required=False)

class Execution(ProtoEntity):
    amount          = Field('string',	1, required=False)
    contract        = Field('string',	2, required=False)
    data            = Field('bytes',	3, required=False)

class ActionCore(ProtoEntity):
    version         = Field('uint32',	1, required=False)
    nonce           = Field('uint64',	2, required=False)
    gasLimit        = Field('uint64',	3, required=False)
    gasPrice        = Field('string',	4, required=False)
    transfer        = Field(Transfer,	10, required=False)
    execution       = Field(Execution,	12, required=False)

class Action(ProtoEntity):
    core            = Field(ActionCore,	1, required=False)
    senderPubKey    = Field('bytes',	2, required=False)
    signature       = Field('bytes',	3, required=False)

class SigningInput(ProtoEntity):
    version         = Field('uint32',	1, required=False)
    nonce           = Field('uint64',	2, required=False)
    gasLimit        = Field('uint64',	3, required=False)
    gasPrice        = Field('string',	4, required=False)
    privateKey      = Field('bytes',	5, required=False)
    transfer        = Field(Transfer,	10, required=False)
    execution       = Field(Execution,	12, required=False)

class SigningOutput(ProtoEntity):
    encoded         = Field('bytes',	1, required=False)
    hash            = Field('bytes',	2, required=False)

