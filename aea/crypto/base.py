# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Abstract module wrapping the public and private key cryptography and ledger api."""

from abc import ABC, abstractmethod
from typing import Any, BinaryIO, Dict, Optional, Union

from aea.mail.base import Address

AddressLike = Union[str, bytes]


class Crypto(ABC):
    """Base class for a crypto object."""

    identifier = "base"

    @property
    @abstractmethod
    def entity(self) -> Any:
        """
        Return an entity object.

        :return: an entity object
        """

    @property
    @abstractmethod
    def public_key(self) -> str:
        """
        Return a public key.

        :return: a public key string
        """

    @property
    @abstractmethod
    def address(self) -> str:
        """
        Return the address.

        :return: an address string
        """

    @classmethod
    @abstractmethod
    def get_address_from_public_key(cls, public_key: str) -> str:
        """
        Get the address from the public key.

        :param public_key: the public key
        :return: str
        """

    @abstractmethod
    def sign_message(self, message: bytes) -> bytes:
        """
        Sign a message in bytes string form.

        :param message: the message we want to send
        :return: Signed message in bytes
        """

    @abstractmethod
    def recover_message(self, message: bytes, signature: bytes) -> Address:
        """
        Recover the address from the hash.

        :param message: the message we expect
        :param signature: the transaction signature
        :return: the recovered address
        """

    @classmethod
    @abstractmethod
    def load(cls, fp: BinaryIO) -> "Crypto":
        """
        Deserialize binary file `fp` (a `.read()`-supporting file-like object containing a private key).

        :param fp: the input file pointer. Must be set in binary mode (mode='rb')
        :return: None
        """

    @abstractmethod
    def dump(self, fp: BinaryIO) -> None:
        """
        Serialize crypto object as binary stream to `fp` (a `.write()`-supporting file-like object).

        :param fp: the output file pointer. Must be set in binary mode (mode='wb')
        :return: None
        """


class LedgerApi(ABC):
    """Interface for ledger APIs."""

    identifier = "base"  # type: str

    @property
    @abstractmethod
    def api(self) -> Any:
        """
        Get the underlying API object.

        This can be used for low-level operations with the concrete ledger APIs.
        If there is no such object, return None.
        """

    @abstractmethod
    def get_balance(self, address: AddressLike) -> int:
        """
        Get the balance of a given account.

        This usually takes the form of a web request to be waited synchronously.

        :param address: the address.
        :return: the balance.
        """

    @abstractmethod
    def send_transaction(
        self,
        crypto: Crypto,
        destination_address: AddressLike,
        amount: int,
        tx_fee: int,
        **kwargs
    ) -> Optional[str]:
        """
        Submit a transaction to the ledger.

        If the mandatory arguments are not enough for specifying a transaction
        in the concrete ledger API, use keyword arguments for the additional parameters.

        :param crypto: the crypto object associated to the payer.
        :param destination_address: the destination address of the payee.
        :param amount: the amount of wealth to be transferred.
        :param tx_fee: the transaction fee.
        :return: tx digest if successful, otherwise None
        """

    @abstractmethod
    def is_transaction_settled(self, tx_digest: str) -> bool:
        """
        Check whether a transaction is settled or not.

        :param tx_digest: the digest associated to the transaction.
        :return: True if the transaction has been settled, False o/w.
        """

    @abstractmethod
    def validate_transaction(self, tx_digest: str, seller: Address, client: Address, tx_nonce: str, amount: int) -> bool:
        """
        Check whether a transaction is valid or not.

        :param seller: the address of the seller.
        :param client: the address of the client.
        :param tx_nonce: the transaction nonce.
        :param amount: the amount we expect to get from the transaction.
        :param tx_digest: the transaction digest.

        :return: True if the random_message is equals to tx['input']
        """
    @abstractmethod
    def generate_tx_nonce(self, seller: Address, client: Address) -> str:
        """
        Generate a random str message.

        :param seller: the address of the seller.
        :param client: the address of the client.
        :return: return the hash in hex.
        """
