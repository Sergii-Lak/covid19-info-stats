from setuptools import setup

setup(
    name='covid19-info-stats',
    version='0.1.1',
    packages=['covid19-info-stats'],    
    url='https://github.com/Sergii-Lak/covid19-info-stats',
    package_dir={'': 'C/Users/bcollins/UHD_PY/uhd/host/build/python'}
    license='MIT',
    author='Sergii-Lak',
    install_requires=["pandas", "numpy"],
    author_email='serg1509@yandex.ru',
    description='Сovid19 statistics per countries and for the world'
)
