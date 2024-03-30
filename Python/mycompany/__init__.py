# Package of Python:
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# in this section, mycompany package contains abc and xyz module, and __init__.py has to present to be recognized as a package.
# As long as mycompany is the unique one presented in the tree structure, you can call for abc module by mycompany.abc to avoid conflict with another module named abc from other packages.

# mycompany
#  ├─ web
#  │  ├─ __init__.py
#  │  ├─ utils.py
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py
#  └─ utils.py

# Likewise, should ww be called, the module is mycompany.web.www; while mycompany.utils and mycompany.web.utils are different