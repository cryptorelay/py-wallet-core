from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('walletcore',
                         ['walletcore.pyx'],
                         include_dirs=['wallet-core/include'],
                         extra_objects=[
                             'wallet-core/build/libTrustWalletCore.a',
                             'wallet-core/build/libprotobuf.a',
                             'wallet-core/build/trezor-crypto/libTrezorCrypto.a',
                         ],
                         )]

setup(
    name='walletcore',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
