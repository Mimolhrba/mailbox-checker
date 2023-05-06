from setuptools import setup

setup(
    name='mailbox-checker',
    version='0.1',
    description='A module for checking a mailbox for new emails.',
    py_modules=['mailbox_checker'],
    entry_points={
        'console_scripts': [
            'check-mailbox=mailbox_checker:check',
        ],
    },
)
