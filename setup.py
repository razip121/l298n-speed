import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="l298n-speed",
    version="0.0.3",
    author="Pascal Watteel",
    author_email="pascal@watteel.com",
    description="A module to assist in controlling an L298N H-Bridge motor driver including speed control via pwm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piwi3910/l298n-speed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
