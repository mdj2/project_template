from setuptools import setup, find_packages

import sys

MAJOR_VERSION = sys.version_info[0]
MINOR_VERSION = sys.version_info[1]
PY2 = MAJOR_VERSION == 2
PY26 = PY2 and MINOR_VERSION == 6
PY3 = MAJOR_VERSION == 3

install_requires = [
    #'celery',
    'django-arcutils',
    #'django-cas',
    'django-cloak',
    # 'django-perms',
    #'elasticsearch',
    'PyMySQL',
    'pytz',
    # 'python3-ldap',
    'setuptools',
]

if PY2:
    install_requires += [
        'configparser',
    ]
if PY26:
    install_requires += [
        'argparse',
        'django>=1.6,<1.7',
    ]
else:
    install_requires += [
        'django>=1.7',
    ]


setup(
    name='{{ project_name }}',
    version='0.0.0.dev0',
    description='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'dev': [
            'coverage',
            'mock',
            'model-mommy',
            'pep8',
            'pyflakes',
        ]
    },
)
