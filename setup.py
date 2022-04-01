from setuptools import find_packages, setup

setup(
    name='housepricesadv',
    packages=find_packages(where="housepricesadv"),
    package_dir={"": "housepricesadv"},  # Optional
    version='0.1.0',
    description='kaggle competition adv house prices modeling',
    author='christian ritter',
    license='MIT',
)
