from setuptools import setup, find_packages

execfile('csv2html/__init__.py')

setup(
    name='csv2html',
    version=__version__,
    description='A flexible utility to convert CSV files into HTML tables.',
    url='http://github.com/newhotter/csv2html',
    author='Danyil Bohdan',
    author_email='danyil.bohdan@gmail.com',
    license='BSD',
    packages=find_packages(),
    data_files=[('', ['LICENSE', 'README.md'])],
    zip_safe=False,
    install_requires=[
            'argparse',
            'html',
        ],
    entry_points={
        'console_scripts': [
            'csv2html = csv2html.csv2html:main',
        ],
    }
)
