## Sample 实例

```shell
docker build -t jamtur01/nginx .
# nginx 作为启动命令 -v 挂卷
docker run -d -p 80 --name website -v $PWD/website:/var/www/html/website jamtur01/nginx nginx
```