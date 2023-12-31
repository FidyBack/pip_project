from setuptools import setup

setup(
    name='dev_aberto_abel',
    version='0.1',
    author="abel",
    packages=['dev_aberto'],
    python_requires='>=3.6',
    platforms=['Linux', 'Windows'],
    install_requires=['requests>=2.20.0', 'babel>=2.6.0'],
    scripts=['scripts/hello.py'],
    )
