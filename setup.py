from setuptools import setup

setup(name='unbabel-localize',
      version='0.20',
      description='Seamless Localization using the Unbabel API',
      author='Vasco Calais Pedro',
      author_email='vasco@unbabel.co',
      packages=[
          'unbabel-localize',
          ],
      package_dir={
        'unbabel': 'unbabel-localize/',
        },
      install_requires=[
        'unbabel-py',
          ],
      url = 'https://github.com/Unbabel/unbabel-localize',
      download_url = 'https://github.com/Unbabel/unbabel-localize/tarball/0.1',
      classifiers = ['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python ',
                     'Topic :: Text Processing'
                     ]
      )
