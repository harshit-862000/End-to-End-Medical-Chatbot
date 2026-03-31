from pathlib import Path

from setuptools import find_packages, setup


def read_requirements() -> list[str]:
    requirements_path = Path(__file__).with_name("requirements.txt")
    requirements = []

    for line in requirements_path.read_text().splitlines():
        requirement = line.strip()

        if not requirement or requirement.startswith("#") or requirement == "-e .":
            continue

        requirements.append(requirement)

    return requirements


setup(
    name="Generative AI Project",
    version="0.0.0",
    author="harshit",
    author_email="harshituohyd@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements(),
)
    
