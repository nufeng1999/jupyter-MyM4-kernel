#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyM4_kernel',
      vem4ion='0.0.1',
      description='Minimalistic M4 kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyM4-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyM4-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiem4=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyM4_kernel/install_MyM4_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'M4','m4','macro','processor'],
      include_package_data=True
      )
