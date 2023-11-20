from setuptools import setup, find_packages

setup(
    name='cli-bip',
    version='0.1',
    description='CLI BATCH IMAGE PROCESSOR',
    url='https://github.com/P-MCC/cli-bip',
    author='P-MCC',
    author_email='',
    license='MIT',
    install_requires=['opencv-python, click'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['cli-bip=cli-bip.__main__:main']
    )
)