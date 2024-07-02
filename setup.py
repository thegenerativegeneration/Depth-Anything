from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Load requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()
    requirements = [req.strip() for req in requirements]

setup(
    name="depth-anything",
    version="0.1.0",
    author="LiheYoung",
    author_email="author@example.com",  # Replace with actual author email
    description="Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thegenerativegeneration/Depth-Anything",  # Replace with actual URL
    packages=["depth_anything", "depth_anything.util"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    include_package_data=True,
)