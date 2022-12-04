from setuptools import setup, find_packages

setup(
    name="normutil",
    use_scm_version={"write_to": "src/normutil/_version.py"},
    setup_requires=["setuptools_scm"],
    description="Demo package for normconf talk on packaging",
    author="Tom Baldwin",
    author_email="baldwint@baldwint.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
