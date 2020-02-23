"""Setup."""

import setuptools

setuptools.setup(
    name="sb8200_exporter",
    version="0.0.1",
    author="Steven Brudenell",
    author_email="steven.brudenell@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.18.4",
        "beautifulsoup4>=4.6.0",
        "prometheus_client>=0.2.0",
        "html5lib>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "sb8200_exporter = sb8200_exporter:exporter_main",
        ],
    },
)
