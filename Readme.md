Daily Playground
===

## Basically all code-related activities

### venv shouldn't be included in git
- Use following command to activate and use the virtual environment:
```
python -m venv venv
.\venv\scripts\activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r .\DeepLearning\requirements.txt
```
*Should windows returns '因为在此系统上禁止运行脚本' when it comes to venv, run 'set-executionpolicy remotesigned' in administrator-access powershell*