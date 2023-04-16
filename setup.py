from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='gptrim',
    version='0.1.0',
    description='A tool to trim the input of OpenAI GPT models.',
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
