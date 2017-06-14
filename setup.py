from setuptools import setup

setup(name='combat',
        version='0.1',
        description='ComBat empirical Bayes correction of batch effects in expression data',
        url='https://github.com/dimenwarper/combat.py',
        packages=['combat'],
        install_requires=['numpy', 'scipy', 'matplotlib', 'pandas']
        )
