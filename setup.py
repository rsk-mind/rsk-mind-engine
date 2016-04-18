setup(name='fraud_backend',
      version='0.1',
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
      zip_safe=False)
