from setuptools import setup

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
