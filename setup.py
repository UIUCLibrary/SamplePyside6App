from setuptools import setup

setup(
    name='SamplePyside6App',
    version='0.1',
    packages=['hellopyside6'],
    url='',
    license='',
    author='hborcher',
    author_email='',
    description='Just a sample pyside6 app for testing',
    install_requires="pyside6",
    include_package_data=True,
    package_data={"hellopyside6": ['main.qml']}
)
