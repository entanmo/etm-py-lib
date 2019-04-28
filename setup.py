from setuptools import setup, find_packages

setup(
    name='etm-py-lib',
    version='1.0.0',
    keywords=('entanmo', 'python'),
    description='En-Tan-Mo Python Library',
    license='MIT License',

    url='https://github.com/entanmo/etm-py-lib.git',
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    platforms='any',
)
