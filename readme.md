# 这是一个为了便于部署 luoxu 而创建的工具包

## 编辑配置文件

### config.toml
配置 telegram 中各项

数据库默认不暴露,如果不想在多处修改数据库信息,保持现状即可.

web 配置需添加最终访问地址到 origins 

#### Telegram
```shell
python -m venv venv
source venv/bin/active
pip install -r requirements.txt
python auth.py
```

获取到了 luoxubot.session,

**这是telegram登录凭证,注意保护,不要分享此文件.**

### docker-compose.yml
如果上游接受了我的docker镜像,需要将各个服务的docker镜像组织部分修改.

修改web中的环境变量 VITE_LUOXU_URL 为 [真实访问地址]/luoxu

### caddy 访问密码
因为后端是由客户端直接链接,所以得加上密码防止未授权的链接.

Caddyfile中

用户名为 username

密码为 password

需要更改的话,查找caddy官方文档吧.