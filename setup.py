__version__ = "0.1.0"

setup(
        name='fraud_backend',
        version=__version__,
        description='The back-end logic of the  fraud detection platform'
        url='git@bitbucket.org:rasarmy/fraud-backend.git'
        author='RSK Project',
        author_email='',
        license='MIT',
        packages=['fraud_backend'],
        # dependent packages
        install_requires=[
            'numpy',
            'scipy'
            ],
        extras_require = {
            'docs': ['sphinx']
            },
        zip_safe=False)
