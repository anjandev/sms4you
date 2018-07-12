from setuptools import setup, find_packages

setup(
    name='sms4you',
    version='0.0.1',
    description='Easy gateway to send and receive SMS via email',
    long_description='Easy gateway to send and receive SMS via email.',
    url='https://github.com/xamanu/sms4you',
    license='MIT',
    keywords='sms email gateway',
    author='Various collaborators: https://github.com/xamanu/sms4you',

    install_requires=['python-dotenv', 'python-gammu'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sms4you = sms4you.sms4you:main'
        ]
    },
)
