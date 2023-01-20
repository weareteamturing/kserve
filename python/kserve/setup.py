# Copyright 2021 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pathlib

import setuptools

TESTS_REQUIRES = [
    'pytest',
    'pytest-xdist',
    'pytest-cov',
    'pytest-asyncio',
    'pytest-tornasync',
    'mypy',
    'portforward',
]

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

with open(pathlib.Path(__file__).parent.parent / 'VERSION') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='kserve-mathking',
    version=version,
    author="teamturing",
    author_email='admin-developers@teamturing.com',
    license="Apache License Version 2.0",
    url="https://github.com/kserve/kserve/tree/master/python/kserve",
    description="KServe Python SDK",
    long_description="Python SDK for KServe Server and Client.",
    python_requires='>=3.9',
    packages=[
        'kserve',
        'kserve.api',
        'kserve.constants',
        'kserve.models',
        'kserve.handlers',
        'kserve.utils',
        'kserve.grpc'
    ],
    package_data={'': ['requirements.txt']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require={'test': TESTS_REQUIRES}
)
