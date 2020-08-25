from setuptools import setup

setup(
    name="docker-mirror",
    version="0.0.1",
    url="https://github.com/bamboovir/docker-mirror",
    author="Huiming Sun",
    author_email="bamboo1886@gmail.com",
    maintainer="Huiming Sun",
    maintainer_email="bamboo1886@gmail.com",
    long_description="",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["."],
    include_package_data=True,
    python_requires=">=3.7,",
    install_requires=["requests==2.22.0", "fire==0.3.1"],
    extras_require={"dev": ["black",]},
    entry_points={"console_scripts": ["docker-mirror = mirror.mirror:main"]},
)
