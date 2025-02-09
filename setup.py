# 3rd Party Library
from setuptools import find_packages
from setuptools import setup

# general information about package
name = "mersad"
url = "https://gitlab.com/Azadeh-Afzar/Cryptography/Mersad-Cryptography-Library"
license_name = "AGPLv3"
author = "Mohammad Mahdi Baghbani Pourvahid"
author_email = "MahdiBaghbani@protonmail.com"
description = """Azadeh Afzar - mersad Cryptographic Library"""

# filter test directory from packages
packages = {package for package in find_packages() if "test" not in package}

# add stub files to package data
package_data = {
    "mersad": [
        "py.typed", "__init__.pyi"
    ],
    "mersad.classical": [
        "__init__.pyi", "affine_cipher.pyi", "shift_cipher.pyi"
    ],
    "mersad.util": [
        "__init__.pyi", "base_class.pyi", "crypto_math.pyi",
        "string_analyzer.pyi", "string_manipulation.pyi",
        "type_check.pyi"
    ]
}

# dependencies
install_requires = ["ErfanIO"]

setup(
        name=name,
        version="0.0.1",
        packages=packages,
        package_data=package_data,
        url=url,
        license=license_name,
        author=author,
        author_email=author_email,
        description=description,
        install_requires=install_requires
)
