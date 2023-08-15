EP_PING = 'ping'
EP_INFO = 'info'
EP_LOGS_GET = 'logs_get'
EP_CONF_GET = 'conf_get'
EP_CONF_SET = 'conf_set'
EP_CRON_ENA = 'cron_ena'
EP_CRON_DIS = 'cron_dis'
EP_UPDATE_MAT = 'update_mat'
EP_UPDATE_DDH = 'update_ddh'
EP_UPDATE_DDT = 'update_ddt'
EP_UPDATE_LIU = 'update_liu'
EP_KILL_DDH = 'kill_ddh'
EP_KILL_API = 'kill_api'
EP_MAC_LOGGER_RESET = 'mac_logger_reset'


# PING probes a lot of IPs, timeout will expire, should be low
# rest return immediately upon response, they can be higher
d_ep = {
    EP_PING: .5,
    EP_INFO: 10,
    EP_LOGS_GET: 10,
    EP_CONF_GET: 5,
    EP_CONF_SET: 5,
    EP_CRON_ENA: 1,
    EP_CRON_DIS: 1,
    EP_UPDATE_MAT: 60,
    EP_UPDATE_DDH: 30,
    EP_UPDATE_DDT: 30,
    EP_UPDATE_LIU: 30,
    EP_KILL_DDH: 5,
    EP_KILL_API: 5,
}

LIST_CONF_FILES = {
    'settings/ddh.json',
    'settings/ctx.py',
    'run_dds.sh',
    'settings/_li_all_macs_to_sn.yml',
    '/etc/crontab'
}

