from trustwallet/wallet-core as wallet-core

WORKDIR /wallet-core
RUN set -ex; \
    export PATH="$HOME/.rbenv/bin:$PATH"; \
    eval "$(rbenv init -)"; \
    export PREFIX=/usr/local; \
    tools/generate-files; \
    cmake -H. -Bbuild -DCMAKE_BUILD_TYPE=Release; \
    make -Cbuild install

from python:3.7.4-slim

COPY --from=wallet-core /wallet-core/include /usr/local/include/wallet-core
COPY --from=wallet-core /wallet-core/build/libTrustWalletCore.a /usr/local/lib
COPY --from=wallet-core /wallet-core/build/libprotobuf.a /usr/local/lib
COPY --from=wallet-core /wallet-core/build/trezor-crypto/libTrezorCrypto.a /usr/local/lib

COPY . /src
WORKDIR /src
RUN pip install cython wheel && python setup.py bdist_wheel
