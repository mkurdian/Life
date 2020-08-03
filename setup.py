from setuptools import setup, find_packages

setup(
    name='life',
    version='0.0.1',
    python_requires='==3.7.7',
    extras_require=dict(tests=['pytest==6.0.1']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        'pygame==1.9.6',
    ],
)
