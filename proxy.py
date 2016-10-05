from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP
from secrets import Proxy_Secrets

p_secrets = Proxy_Secrets()

Connection.set_proxy_info(
    '10.1.1.18',
    80,
    proxy_type=PROXY_TYPE_HTTP,
    proxy_user=p_secrets.user_name,
    proxy_pass=p_secrets.password,
)