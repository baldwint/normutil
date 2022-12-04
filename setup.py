from setuptools import setup, find_packages

setup(
    name="normutil",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Demo package for normconf talk on packaging",
    author="Tom Baldwin",
    author_email="baldwint@baldwint.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
