import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Turing College batch DS_01_2023 Carsten Hennig Sprint1 Python Mastery: Calculator',
    version='1.0.0',
    author='Carsten Hennig',
    author_email='carsten.hennig@gmail.com',
    description='A simple Python package with basic calculator functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CarstenHennig/python-calculator',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='',
    keywords='Python calculator package function class',
    python_requires='3.8'
)


