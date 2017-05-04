import setuptools

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='salesforce-tools',
    version='0.1.0',
    description='Tools for tinkering with Salesforce',
    long_description=readme,
    author='Luke Fritz',
    author_email='luke@lukeandkrista.com',
    url='https://github.com/ldfritz/salesforce-tools',
    license=license
)
