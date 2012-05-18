from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='psusymp.traversingplone',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['psusymp'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.routes',
          'collective.django',
          'psusymp.traversingdjango'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """
      )
