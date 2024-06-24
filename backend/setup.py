from setuptools import setup, find_packages

setup(
    name='DepotSentry',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'Flask',
        'pytest',
        # other dependencies
    ],
    include_package_data=True,
    zip_safe=False,
)
