from setuptools import setup, find_packages

setup(
    name="net_monitor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'net-monitor=net_monitor.main:main',
        ],
    },
    author="P R",
    author_email="privacy@example.com",
    description="A package to monitor network connections and check for malicious IPs.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pen370/net_monitor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None :: None",
        "Operating System :: Linux based",
    ],
    python_requires='>=3.6',
)
