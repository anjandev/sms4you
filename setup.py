from setuptools import setup, find_packages

setup(
    name='sms4you',
    version='0.0.1',
    description='',
    long_description='',
    url='https://github.com/xamanu/sms4you',
    license='GPLv3',
    keywords='',
    author='Various collaborators: https://github.com/xamanu/sms4you',

    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sms4you = sms4you.sms4you:main'
        ]
    },
)
