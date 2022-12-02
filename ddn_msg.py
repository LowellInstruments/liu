SQS_DDH_BOOT = 'DDH_BOOT'
SQS_DDH_ERROR_BLE_HW = 'DDH_ERROR_BLE_HARDWARE'
SQS_LOGGER_DL_OK = 'LOGGER_DOWNLOAD'
SQS_LOGGER_ERROR_OXYGEN = 'LOGGER_ERROR_OXYGEN'
SQS_LOGGER_MAX_ERRORS = 'LOGGER_ERRORS_MAXED_RETRIES'


class DdnMsg:
    def __init__(self,
                 msg_ver=1):
        self.reason = None
        self.logger_mac = None
        self.logger_sn = None
        self.project = None
        self.vessel = None
        self.ddh_commit = None
        self.utc_time = None
        self.local_time: None
        self.box_sn: None
        self.hw_uptime = None
        self.gps_position = None
        self.platform = None
        self.msg_ver = msg_ver

    def as_dict(self):
        return vars(self)


if __name__ == '__main__':
    m = DdnMsg()
    m.check_none()
    print(m.as_dict())
