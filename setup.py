from setuptools import setup

classifiers=['Development Status :: 4 - Beta',
             'Environment :: X11 Applications :: GTK',
             'Intended Audience :: End Users/Desktop',
             'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
             'Operating System :: POSIX',
             'Programming Language :: Python',
             'Topic :: Desktop Environment :: Window Managers :: Applets']

setup(name='caps-lock',
      version='1.0',
      description='Keyboard Status Applet',
      author='Leandro Cerencio',
      author_email='cerencio@yahoo.com.br',
      url='https://www.github.com/lemoce/caps-lock',
      packages=['caps_lock'],
      package_dir={'caps_lock':'src/caps_lock'},
      package_data={'caps_lock':['data/*.svg']},
      entry_points={'console_scripts': ['keystatusapplet=caps_lock.module:main']})
