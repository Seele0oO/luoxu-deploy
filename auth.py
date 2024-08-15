import toml
from telethon.sync import TelegramClient
import socks

# 读取配置文件
config = toml.load('config/config.toml')

# 从配置文件中获取 Telegram 的配置
api_id = config['telegram']['api_id']
api_hash = config['telegram']['api_hash']
account = config['telegram']['account']
session_db = config['telegram']['session_db']

# 检查并读取代理配置
proxy = None
if 'proxy' in config['telegram']:
    proxy_host = config['telegram']['proxy'][0]
    proxy_port = int(config['telegram']['proxy'][1])
    proxy = (socks.SOCKS5, proxy_host, proxy_port)

# 使用或不使用代理配置初始化 TelegramClient
with TelegramClient(session_db, api_id, api_hash, proxy=proxy) as client:
    client.send_message('me', 'Hello, myself!')
    # client.run_until_disconnected()
    print("auth success")
