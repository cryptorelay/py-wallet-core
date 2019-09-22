# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: Stellar.proto
class MemoVoid(ProtoEntity):
    pass

class MemoText(ProtoEntity):
    text            = Field('string',	1, required=False)

class MemoId(ProtoEntity):
    id              = Field('int64',	1, required=False)

class MemoHash(ProtoEntity):
    hash            = Field('bytes',	1, required=False)

class SigningInput(ProtoEntity):
    # enum OperationType
    CREATE_ACCOUNT=0
    PAYMENT=1
    amount          = Field('int64',	1, required=False)
    fee             = Field('int32',	2, required=False)
    sequence        = Field('int64',	3, required=False)
    account         = Field('string',	4, required=False)
    destination     = Field('string',	5, required=False)
    private_key     = Field('bytes',	6, required=False)
    memo_void       = Field(MemoVoid,	7, required=False)
    memo_text       = Field(MemoText,	8, required=False)
    memo_id         = Field(MemoId,	9, required=False)
    memo_hash       = Field(MemoHash,	10, required=False)
    memo_return_hash = Field(MemoHash,	11, required=False)
    operation_type  = Field('enum',	12, required=False)
    passphrase      = Field('string',	13, required=False)

class SigningOutput(ProtoEntity):
    signature       = Field('string',	1, required=False)

