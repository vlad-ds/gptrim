from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='gptrim',
    version='0.1.2',
    description='Reduce the size of GPT inputs by 40-60% without losing most of the information.',
    long_description=long_description,
    url='https://github.com/vlad-ds/gptrim',
    author='Vlad Gheorghe',
    author_email='vlad.datapro@gmail.com',
    packages=['gptrim'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
