from setuptools import setup, find_namespace_packages

setup(name='nnunet',
      packages=find_namespace_packages(include=["nnunet", "nnunet.*"]),
      version='1.7.0',
      description='nnU-Net. Framework for out-of-the box biomedical image segmentation.',
      url='https://github.com/MIC-DKFZ/nnUNet',
      author='Division of Medical Image Computing, German Cancer Research Center',
      author_email='f.isensee@dkfz-heidelberg.de',
      license='Apache License Version 2.0, January 2004',
      install_requires=[
            "torch>1.10.0",
            "tqdm",
            "scikit-image>=0.14",
            "scipy",
            "batchgenerators>=0.23",
            "numpy",
            "sklearn",
            "pandas",
            "requests",
            "nibabel", 
            "tifffile", 
            "matplotlib",
      ],
      entry_points={
          'console_scripts': [
              'nnUNet_train = nnunet.run.run_training:main',
              'nnUNet_train_DP = nnunet.run.run_training_DP:main',
              'nnUNet_train_DDP = nnunet.run.run_training_DDP:main',
          ],
      },
      keywords=['deep learning', 'image segmentation', 'medical image analysis',
                'medical image segmentation', 'nnU-Net', 'nnunet']
      )
