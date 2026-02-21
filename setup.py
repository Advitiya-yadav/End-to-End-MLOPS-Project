from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []

    with open(file_path, "r") as f:
        for line in f:
            req = line.strip()

            if not req or req.startswith("#"):
                continue

            if req == "-e .":
                continue

            requirements.append(req)

    return requirements


setup(
    name="Network Security Project",
    version="0.0.1",
    author="Advitiya Yadav",
    author_email="advitiyayadav2105@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)