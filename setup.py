from setuptools import setup, find_packages

        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'voice': ['PyNaCl==1.3.0'],
    'docs': [gdrfrrrrrr
        'sphinx==1.7.4',
        'sphinxcontrscord.py',
      author='Raands', 'discord.ext.tasks'],
      license='MIT',
      description='A python wrapper for the Discord API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
