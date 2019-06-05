## Docker

### 基础命令汇总

- docker info: 该命令会返回所有容器和镜像
- docker run: 创建容器
    - docker run -i -t ubuntu /bin/bash
- docker ps: 正在运行的容器
- docker start: 启动一个容器
- docker attach: 重新附到某个容器的会话上
- docker logs: 输出对应容器的输出 --tail
- docker top: 查看容器内的进程
- docker stats: 查看一个或多个容器的统计信息
- docker exec: 在容器内启动进程
- docker stop: 关闭容器
- docker inspect: 获得更多的容器信息
- docker rm: 删除容器
- docker images: 列出镜像
- docker pull: 拉取镜像
- docker search: 查找镜像
- docker rmi: 删除镜像
- docker network: 创建一个桥接网络

### 关于Dockerfile

- CMD: 指定一个容器启动时要运行的命令
- ENTRYPOINT: 不会被docker run覆盖
- WORKDIR: 指定工作目录，CMD等执行命令在此目录下面执行
- ENV: 设置环境变量
- USER: 指定镜像以什么样的用户去执行
- VOLUME: 用来向基于镜像创建的容器添加卷
- ADD: 将环境下的文件和目录复制到镜像中
- COPY: 复制本地文件或目录
- LABEL: 为镜像添加元数据
- STOPSIGNAL: 设置停止容器时发送什么系统调用信号给容器
- ARG: 在docker build命令运行时传递给镜像构建时的镜像
- ONBUILD: 为镜像添加触发器

### 关于Docker Compose

