
packages:
    pkg.installed:
        - names:
            - build-essential
            - git
            - python
            - python-dev
            - python-pip
            - python-virtualenv


virtualenvwrapper:
    pip.installed:
        - require:
            - pkg: packages