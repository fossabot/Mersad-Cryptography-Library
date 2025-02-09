# Stubs for mersad.test.classical.testShiftCipher (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# Python Standard Library
import unittest
from typing import Any

class TestBasics(unittest.TestCase):
    ShiftCipher: Any = ...
    def setUp(self) -> None: ...
    def test_encrypt(self) -> None: ...
    def test_decrypt(self) -> None: ...
    def test_config(self) -> None: ...
    def test_config_reset(self) -> None: ...
    def test_config_bad_type(self) -> None: ...

class TestEncryption(unittest.TestCase):
    ShiftCipher: Any = ...
    base_path: Any = ...
    plain_text: Any = ...
    def setUp(self) -> None: ...
    def test_encrypt_without_shuffle(self) -> None: ...
