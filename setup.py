import setuptools
import versioneer

version = versioneer.get_version()
cmdclass = versioneer.get_cmdclass()

with open("README.md", "r", encoding="utf-8") as infile:
    readme = infile.read()

packagedir = "src"

setuptools.setup(
    name="mash",
    version=version,
    cmdclass=cmdclass,
    author="Peter Kraus",
    author_email="peter@tondon.de",
    description="get guess structures of perovskites",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/PeterKraus/mash",
    project_urls={
        "Bug Tracker": "https://github.com/PeterKraus/mash/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": packagedir},
    packages=setuptools.find_packages(where=packagedir),
    python_requires=">=3.9",
    install_requires=[
        "mendeleev",
    ],
    extras_require={},
    entry_points={"console_scripts": ["mash=mash:main"]},
)
