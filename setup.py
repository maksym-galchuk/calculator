from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1.0",
    description="A simple calculator project for CI/CD lab",
    author="Student",
    author_email="student@example.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "flake8>=6.1.0",
        "black>=23.7.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)