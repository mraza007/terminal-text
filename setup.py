from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
     name='terminal-text',    
     version='1.0',                         
     scripts=['termtext'],
     description='Its a simple commandline tool that allows you send text messages and mms to your phone using terminal',
     install_requires=[
        "twilio",
        "docopt",
        "pyOpenSSL"
    ],
    classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: MacOS :: Linux',
            'Programming Language :: Python',
    'Programming Language :: Python :: 3.6'],
    long_description=long_description,
    long_description_content_type='text/markdown'
 )
