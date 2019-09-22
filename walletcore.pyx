#cython: language_level=3
from libcpp cimport bool
from libc.stdint cimport uint8_t, uint32_t

cdef extern from "TrustWalletCore/TWString.h":
    ctypedef void TWString;
    TWString *TWStringCreateWithUTF8Bytes(const char *bytes);
    size_t TWStringSize(TWString *string);
    const char *TWStringUTF8Bytes(TWString *string);

cdef extern from "TrustWalletCore/TWData.h":
    ctypedef void TWData;
    TWData *TWDataCreateWithBytes(const uint8_t *bytes, size_t size);
    size_t TWDataSize(TWData *data);
    uint8_t *TWDataBytes(TWData *data);

cdef extern from "TrustWalletCore/TWPublicKey.h":
    struct TWPublicKey:
        pass
    enum TWPublicKeyType:
        TWPublicKeyTypeSECP256k1
        TWPublicKeyTypeSECP256k1Extended
        TWPublicKeyTypeNIST256p1
        TWPublicKeyTypeNIST256p1Extended
        TWPublicKeyTypeED25519
        TWPublicKeyTypeED25519Blake2b
        TWPublicKeyTypeCURVE25519

    TWPublicKey *TWPublicKeyCreateWithData(TWData *data, TWPublicKeyType type);
    void TWPublicKeyDelete(TWPublicKey *pk);
    bool TWPublicKeyIsValid(TWData *data, TWPublicKeyType type);
    TWData *TWPublicKeyData(TWPublicKey *pk);
    bool TWPublicKeyVerify(TWPublicKey *pk, TWData *signature, TWData *message);
    bool TWPublicKeyVerifySchnorr(TWPublicKey *pk, TWData *signature, TWData *message);
    TWPublicKeyType TWPublicKeyKeyType(TWPublicKey *publicKey);
    TWString *TWPublicKeyDescription(TWPublicKey *publicKey);
    TWPublicKey *TWPublicKeyRecover(TWData *signature, TWData *message);
    bool TWPublicKeyIsCompressed(TWPublicKey *pk);
    TWPublicKey *TWPublicKeyCompressed(TWPublicKey *_from);
    TWPublicKey *TWPublicKeyUnCompressed(TWPublicKey *_from);

cdef extern from "TrustWalletCore/TWPrivateKey.h":
    struct TWPrivateKey:
        pass
    TWPrivateKey *TWPrivateKeyCreate();
    TWPrivateKey *TWPrivateKeyCreateWithData(TWData *data);
    TWPrivateKey *TWPrivateKeyCreateCopy(TWPrivateKey *key);
    void TWPrivateKeyDelete(TWPrivateKey *pk);
    bool TWPrivateKeyIsValid(TWData *data, TWCurve curve);
    TWData *TWPrivateKeyData(TWPrivateKey *pk);
    TWData *TWPrivateKeySign(TWPrivateKey *pk, TWData *digest, TWCurve curve);
    TWData *TWPrivateKeySignAsDER(TWPrivateKey *pk, TWData *digest, TWCurve curve);
    TWData *TWPrivateKeySignSchnorr(TWPrivateKey *pk, TWData *message, TWCurve curve);
    TWPublicKey *TWPrivateKeyGetPublicKeySecp256k1(TWPrivateKey *pk, bool compressed);
    TWPublicKey *TWPrivateKeyGetPublicKeyNist256p1(TWPrivateKey *pk);
    TWPublicKey *TWPrivateKeyGetPublicKeyEd25519(TWPrivateKey *pk);
    TWPublicKey *TWPrivateKeyGetPublicKeyEd25519Blake2b(TWPrivateKey *pk);
    TWPublicKey *TWPrivateKeyGetPublicKeyCurve25519(TWPrivateKey *pk);

cdef extern from "TrustWalletCore/TWCoinType.h":
    enum TWBlockchain:
        TWBlockchainBitcoin
        TWBlockchainEthereum
        TWBlockchainWanchain
        TWBlockchainVechain
        TWBlockchainTron
        TWBlockchainIcon
        TWBlockchainBinance
        TWBlockchainRipple
        TWBlockchainTezos
        TWBlockchainNimiq
        TWBlockchainStellar
        TWBlockchainAion
        TWBlockchainCosmos
        TWBlockchainTheta
        TWBlockchainOntology
        TWBlockchainZilliqa
        TWBlockchainIoTeX
        TWBlockchainArk
        TWBlockchainEOS
        TWBlockchainIOST
        TWBlockchainSemux
        TWBlockchainNano
        TWBlockchainNEO
        TWBlockchainSteem
        TWBlockchainWaves
        TWBlockchainAeternity
        TWBlockchainNebulas
        TWBlockchainFIO
        TWBlockchainSolana
        TWBlockchainHarmony

    enum TWCoinType:
        TWCoinTypeAeternity
        TWCoinTypeAion
        TWCoinTypeBinance
        TWCoinTypeBitcoin
        TWCoinTypeBitcoinCash
        TWCoinTypeBravoCoin
        TWCoinTypeCallisto
        TWCoinTypeCosmos
        TWCoinTypeDash
        TWCoinTypeDecred
        TWCoinTypeDigiByte
        TWCoinTypeDogecoin
        TWCoinTypeEllaism
        TWCoinTypeEOS
        TWCoinTypeEthereum
        TWCoinTypeEthereumClassic
        TWCoinTypeEthersocial
        TWCoinTypeFIO
        TWCoinTypeGoChain
        TWCoinTypeGroestlcoin
        TWCoinTypeICON
        TWCoinTypeIOST
        TWCoinTypeIoTeX
        TWCoinTypeKin
        TWCoinTypeLitecoin
        TWCoinTypeMonacoin
        TWCoinTypeNebulas
        TWCoinTypeLux
        TWCoinTypeNano
        TWCoinTypeNEO
        TWCoinTypeNimiq
        TWCoinTypeOntology
        TWCoinTypePOANetwork
        TWCoinTypeQtum
        TWCoinTypeXRP
        TWCoinTypeSolana
        TWCoinTypeSteem
        TWCoinTypeStellar
        TWCoinTypeTezos
        TWCoinTypeTheta
        TWCoinTypeThunderToken
        TWCoinTypeTomoChain
        TWCoinTypeTron
        TWCoinTypeVeChain
        TWCoinTypeViacoin
        TWCoinTypeWanchain
        TWCoinTypeXDai
        TWCoinTypeZcash
        TWCoinTypeZcoin
        TWCoinTypeZilliqa
        TWCoinTypeSemux
        TWCoinTypeDEXON
        TWCoinTypeZelcash
        TWCoinTypeARK
        TWCoinTypeRavencoin
        TWCoinTypeWaves
        TWCoinTypeTerra
        TWCoinTypeHarmony

    enum TWPurpose:
        TWPurposeBIP44
        TWPurposeBIP49  # Derivation scheme for P2WPKH-nested-in-P2SH
        TWPurposeBIP84  # Derivation scheme for P2WPKH

    enum TWCurve:
        TWCurveSECP256k1              # /* "secp256k1" */,
        TWCurveED25519                # /* "ed25519" */,
        TWCurveED25519Blake2bNano     # /* "ed25519-blake2b-nano" */,
        TWCurveCurve25519             # /* "curve25519" */,
        TWCurveNIST256p1              # /* "nist256p1" */,

    TWBlockchain TWCoinTypeBlockchain(TWCoinType coin);
    TWPurpose TWCoinTypePurpose(TWCoinType coin);
    TWCurve TWCoinTypeCurve(TWCoinType coin);
    TWString *TWCoinTypeDeriveAddress(TWCoinType coin,
                                      TWPrivateKey *privateKey);
    TWString *TWCoinTypeDeriveAddressFromPublicKey(TWCoinType coin,
                                                   TWPublicKey *publicKey);
    uint8_t TWCoinTypeStaticPrefix(TWCoinType coin);

cdef extern from "TrustWalletCore/TWHDWallet.h":
    struct TWHDWallet:
        pass

    enum TWHDVersion:
        TWHDVersionNone

        # Bitcoin
        TWHDVersionXPUB
        TWHDVersionXPRV
        TWHDVersionYPUB
        TWHDVersionYPRV
        TWHDVersionZPUB
        TWHDVersionZPRV

        # Litecoin
        TWHDVersionLTUB
        TWHDVersionLTPV
        TWHDVersionMTUB
        TWHDVersionMTPV

        # Decred
        TWHDVersionDPUB
        TWHDVersionDPRV

        # Dogecoin
        TWHDVersionDGUB
        TWHDVersionDGPV

    bool TWHDWalletIsValid(TWString *mnemonic);
    TWHDWallet* TWHDWalletCreate(int strength, TWString *passphrase);
    TWHDWallet* TWHDWalletCreateWithMnemonic(TWString *mnemonic, TWString *passphrase);
    TWHDWallet* TWHDWalletCreateWithData(TWData *seed, TWString *passphrase);
    void TWHDWalletDelete(TWHDWallet *wallet);
    TWString *TWHDWalletMnemonic(TWHDWallet *wallet);
    TWData *TWHDWalletSeed(TWHDWallet *wallet);

    TWPrivateKey *TWHDWalletGetKeyForCoin(TWHDWallet *wallet, TWCoinType coin);
    TWPrivateKey *TWHDWalletGetKey(TWHDWallet *wallet, TWString *derivationPath);
    TWPrivateKey *TWHDWalletGetKeyBIP44(TWHDWallet *wallet, TWCoinType coin, uint32_t account, uint32_t change, uint32_t address);
    TWString *TWHDWalletGetExtendedPrivateKey(TWHDWallet *wallet, TWPurpose purpose, TWCoinType coin, TWHDVersion version);
    TWString *TWHDWalletGetExtendedPublicKey(TWHDWallet *wallet, TWPurpose purpose, TWCoinType coin, TWHDVersion version);
    TWPublicKey *TWHDWalletGetPublicKeyFromExtended(TWString *extended, TWString *derivationPath);

cdef extern from "TrustWalletCore/TWEthereumChainID.h":
    enum TWEthereumChainID:
        TWEthereumChainIDEthereum
        TWEthereumChainIDGo
        TWEthereumChainIDPOA
        TWEthereumChainIDCallisto
        TWEthereumChainIDEllaism
        TWEthereumChainIDEthereumClassic
        TWEthereumChainIDEthersocial
        TWEthereumChainIDVeChain
        TWEthereumChainIDThunderToken
        TWEthereumChainIDTomoChain
        TWEthereumChainIDXDai
        TWEthereumChainIDDEXON

cdef extern from "TrustWalletCore/TWEthereumSigner.h":
    TWData *TWEthereumSignerSign(TWData* input);
cdef extern from "TrustWalletCore/TWBitcoinTransactionSigner.h":
    struct TWBitcoinTransactionSigner:
        pass
    TWBitcoinTransactionSigner* TWBitcoinTransactionSignerCreate(TWData* input);
    TWBitcoinTransactionSigner *TWBitcoinTransactionSignerCreateWithPlan(TWData *input, TWData *plan);
    void TWBitcoinTransactionSignerDelete(TWBitcoinTransactionSigner *signer);
    TWData *TWBitcoinSignerSign(TWData* input);

BLOCKCHAIN_TYPES = {
    'Bitcoin': TWBlockchainBitcoin,
    'Ethereum': TWBlockchainEthereum,
    'Wanchain': TWBlockchainWanchain,
    'Vechain': TWBlockchainVechain,
    'Tron': TWBlockchainTron,
    'Icon': TWBlockchainIcon,
    'Binance': TWBlockchainBinance,
    'Ripple': TWBlockchainRipple,
    'Tezos': TWBlockchainTezos,
    'Nimiq': TWBlockchainNimiq,
    'Stellar': TWBlockchainStellar,
    'Aion': TWBlockchainAion,
    'Cosmos': TWBlockchainCosmos,
    'Theta': TWBlockchainTheta,
    'Ontology': TWBlockchainOntology,
    'Zilliqa': TWBlockchainZilliqa,
    'IoTeX': TWBlockchainIoTeX,
    'Ark': TWBlockchainArk,
    'EOS': TWBlockchainEOS,
    'IOST': TWBlockchainIOST,
    'Semux': TWBlockchainSemux,
    'Nano': TWBlockchainNano,
    'NEO': TWBlockchainNEO,
    'Steem': TWBlockchainSteem,
    'Waves': TWBlockchainWaves,
    'Aeternity': TWBlockchainAeternity,
    'Nebulas': TWBlockchainNebulas,
    'FIO': TWBlockchainFIO,
    'Solana': TWBlockchainSolana,
    'Harmony': TWBlockchainHarmony,
}

COIN_TYPES = {
    'Aeternity': TWCoinTypeAeternity,
    'Aion': TWCoinTypeAion,
    'Binance': TWCoinTypeBinance,
    'Bitcoin': TWCoinTypeBitcoin,
    'BitcoinCash': TWCoinTypeBitcoinCash,
    'BravoCoin': TWCoinTypeBravoCoin,
    'Callisto': TWCoinTypeCallisto,
    'Cosmos': TWCoinTypeCosmos,
    'Dash': TWCoinTypeDash,
    'Decred': TWCoinTypeDecred,
    'DigiByte': TWCoinTypeDigiByte,
    'Dogecoin': TWCoinTypeDogecoin,
    'Ellaism': TWCoinTypeEllaism,
    'EOS': TWCoinTypeEOS,
    'Ethereum': TWCoinTypeEthereum,
    'EthereumClassic': TWCoinTypeEthereumClassic,
    'Ethersocial': TWCoinTypeEthersocial,
    'FIO': TWCoinTypeFIO,
    'GoChain': TWCoinTypeGoChain,
    'Groestlcoin': TWCoinTypeGroestlcoin,
    'ICON': TWCoinTypeICON,
    'IOST': TWCoinTypeIOST,
    'IoTeX': TWCoinTypeIoTeX,
    'Kin': TWCoinTypeKin,
    'Litecoin': TWCoinTypeLitecoin,
    'Monacoin': TWCoinTypeMonacoin,
    'Nebulas': TWCoinTypeNebulas,
    'Lux': TWCoinTypeLux,
    'Nano': TWCoinTypeNano,
    'NEO': TWCoinTypeNEO,
    'Nimiq': TWCoinTypeNimiq,
    'Ontology': TWCoinTypeOntology,
    'POANetwork': TWCoinTypePOANetwork,
    'Qtum': TWCoinTypeQtum,
    'XRP': TWCoinTypeXRP,
    'Solana': TWCoinTypeSolana,
    'Steem': TWCoinTypeSteem,
    'Stellar': TWCoinTypeStellar,
    'Tezos': TWCoinTypeTezos,
    'Theta': TWCoinTypeTheta,
    'ThunderToken': TWCoinTypeThunderToken,
    'TomoChain': TWCoinTypeTomoChain,
    'Tron': TWCoinTypeTron,
    'VeChain': TWCoinTypeVeChain,
    'Viacoin': TWCoinTypeViacoin,
    'Wanchain': TWCoinTypeWanchain,
    'XDai': TWCoinTypeXDai,
    'Zcash': TWCoinTypeZcash,
    'Zcoin': TWCoinTypeZcoin,
    'Zilliqa': TWCoinTypeZilliqa,
    'Semux': TWCoinTypeSemux,
    'DEXON': TWCoinTypeDEXON,
    'Zelcash': TWCoinTypeZelcash,
    'ARK': TWCoinTypeARK,
    'Ravencoin': TWCoinTypeRavencoin,
    'Waves': TWCoinTypeWaves,
    'Terra': TWCoinTypeTerra,
    'Harmony': TWCoinTypeHarmony,
}


cdef blockchain_type(str name):
    return BLOCKCHAIN_TYPES[name]


cdef coin_type(str name):
    return COIN_TYPES[name]


cdef str string_to_str(TWString *s):
    return TWStringUTF8Bytes(s)[:TWStringSize(s)].decode('utf-8')


cdef bytes data_to_bytes(TWData *data):
    return TWDataBytes(data)[:TWDataSize(data)]


def is_valid_mnemonic(str mnemonic):
    return TWHDWalletIsValid(TWStringCreateWithUTF8Bytes(mnemonic.encode()))


def curve_type(str coin):
    return TWCoinTypeCurve(coin_type(coin))


cdef class PrivateKey:
    cdef TWPrivateKey* _key;

    def public_key(self, TWCurve curve, bool compressed=False):
        cdef PublicKey pub = PublicKey();
        if curve == TWCurveSECP256k1:
            pub._key = TWPrivateKeyGetPublicKeySecp256k1(self._key, compressed)
        elif curve == TWCurveED25519:
            pub._key = TWPrivateKeyGetPublicKeyEd25519(self._key)
        elif curve == TWCurveED25519Blake2bNano:
            pub._key = TWPrivateKeyGetPublicKeyEd25519Blake2b(self._key)
        elif curve == TWCurveCurve25519:
            pub._key = TWPrivateKeyGetPublicKeyCurve25519(self._key)
        elif curve == TWCurveNIST256p1:
            pub._key = TWPrivateKeyGetPublicKeyNist256p1(self._key)
        else:
            assert False, 'invalid curve %d' % curve
        return pub

    def address(self, str coin):
        return string_to_str(TWCoinTypeDeriveAddress(coin_type(coin), self._key))

    def sign(self, bytes digest, TWCurve curve):
        return data_to_bytes(TWPrivateKeySign(self._key, TWDataCreateWithBytes(digest, len(digest)), curve))

    def sign_as_der(self, bytes digest, TWCurve curve):
        return data_to_bytes(TWPrivateKeySignAsDER(self._key, TWDataCreateWithBytes(digest, len(digest)), curve))

    def sign_schnorr(self, bytes digest, TWCurve curve):
        return data_to_bytes(TWPrivateKeySignSchnorr(self._key, TWDataCreateWithBytes(digest, len(digest)), curve))

    @property
    def data(self):
        return data_to_bytes(TWPrivateKeyData(self._key))

    def __dealloc__(self):
        if self._key:
            TWPrivateKeyDelete(self._key)


cdef class PublicKey:
    cdef TWPublicKey* _key;

    def address(self, str coin):
        return string_to_str(TWCoinTypeDeriveAddressFromPublicKey(coin_type(coin), self._key))

    @property
    def data(self):
        return data_to_bytes(TWPublicKeyData(self._key))

    def __dealloc__(self):
        if self._key:
            TWPublicKeyDelete(self._key)


cdef class HDWallet:
    cdef TWHDWallet* _wallet;

    cdef _create(self, int strength, str passphrase):
        self._wallet = TWHDWalletCreate(
            strength,
            TWStringCreateWithUTF8Bytes(passphrase.encode('utf-8'))
        )

    cdef _recover(self, str mnemonic, str passphrase):
        self._wallet = TWHDWalletCreateWithMnemonic(
            TWStringCreateWithUTF8Bytes(mnemonic.encode('utf-8')),
            TWStringCreateWithUTF8Bytes(passphrase.encode('utf-8'))
        )

    cdef _recover_seed(self, bytes seed, str passphrase):
        self._wallet = TWHDWalletCreateWithData(
            TWDataCreateWithBytes(seed, len(seed)),
            TWStringCreateWithUTF8Bytes(passphrase.encode('utf-8'))
        )

    def __cinit__(self, str mnemonic=None, bytes seed=None, int strength=10, str passphrase=''):
        if mnemonic is not None:
            self._recover(mnemonic, passphrase)
        elif seed is not None:
            self._recover_seed(seed, passphrase)
        else:
            self._create(strength, passphrase)
        assert self._wallet, 'wallet create failed'

    def __dealloc__(self):
        if self._wallet:
            TWHDWalletDelete(self._wallet)

    @property
    def mnemonic(self):
        return string_to_str(TWHDWalletMnemonic(self._wallet))

    @property
    def seed(self):
        return data_to_bytes(TWHDWalletSeed(self._wallet))

    def key_for_coin(self, str coin):
        cdef PrivateKey key = PrivateKey()
        key._key = TWHDWalletGetKeyForCoin(self._wallet, coin_type(coin))
        return key

    def key_for_path(self, path):
        cdef PrivateKey key = PrivateKey()
        key._key = TWHDWalletGetKey(self._wallet, TWStringCreateWithUTF8Bytes(path.encode('utf-8')))
        return key

    def key_for_bip44(self, str coin, int account=0, int change=0, int index=0):
        cdef PrivateKey key = PrivateKey()
        key._key = TWHDWalletGetKeyBIP44(self._wallet, coin_type(coin), account, change, index)
        return key
