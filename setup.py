from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pys3sync-sachin',
    version='0.1.3',
    author="Sachin Rajput",
    author_email="er.sachinrajput1991@gmail.com",
    description="Continuously Sync local files to/from S3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/srajput1991/s3sync",
    py_modules=['s3sync'],
    install_requires=[
        'click',
        'click_log',
        'watchdog',
        'pyyaml',
        'token-bucket',
        'pyformance'
    ],
    entry_points='''
        [console_scripts]
        s3sync=s3sync:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7'
)
