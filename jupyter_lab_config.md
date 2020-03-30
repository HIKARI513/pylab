## 环境配置

先看这篇文章[JupyterLab：程序员的笔记本神器](JupyterLab：程序员的笔记本神器)，本篇主要是针对`Jupyter Lab`插件的一些配置。

首先开启插件安装`Tab`，点击`Settings->Advanced Settings Editor`，将`false`改成`true`:

```json
{
    "enabled": false
}
```

此时可通过GUI界面进行插件安装：

- jupyterlab-drawio
- jupyterlab_code_formatter

关于的安装配置，需要进入项目特定环境：

```shell
jupyter labextension install @ryantam626/jupyterlab_code_formatter
pipenv install jupyterlab_code_formatter
pipenv install black
jupyter serverextension enable --py jupyterlab_code_formatter
```

