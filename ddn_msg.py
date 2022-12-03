OPCODE_SQS_DDH_BOOT = 'DDH_BOOT'
OPCODE_SQS_DDH_ERROR_BLE_HW = 'DDH_ERROR_BLE_HARDWARE'
OPCODE_SQS_LOGGER_DL_OK = 'LOGGER_DOWNLOAD'
OPCODE_SQS_LOGGER_ERROR_OXYGEN = 'LOGGER_ERROR_OXYGEN'
OPCODE_SQS_LOGGER_MAX_ERRORS = 'LOGGER_ERRORS_MAXED_RETRIES'


def get_db_list_of_opcodes():
    return [
        OPCODE_SQS_DDH_BOOT,
        OPCODE_SQS_DDH_ERROR_BLE_HW,
        OPCODE_SQS_LOGGER_DL_OK,
        OPCODE_SQS_LOGGER_ERROR_OXYGEN,
        OPCODE_SQS_LOGGER_MAX_ERRORS
    ]


class DdnMsg:
    def __init__(self, msg_ver=1):
        self.reason = None
        self.logger_mac = None
        self.logger_sn = None
        self.project = None
        self.vessel = None
        self.ddh_commit = None
        self.utc_time = None
        self.local_time = None
        self.box_sn = None
        self.hw_uptime = None
        self.gps_position = None
        self.platform = None
        self.msg_ver = msg_ver

    def cp_from_dict(self, d: dict):
        self.reason = d['reason']
        self.logger_mac = d['logger_mac']
        self.logger_sn = d['logger_sn']
        self.project = d['project']
        self.vessel = d['vessel']
        self.ddh_commit = d['ddh_commit']
        self.utc_time = d['utc_time']
        self.local_time = d['local_time']
        self.box_sn = d['box_sn']
        self.hw_uptime = d['hw_uptime']
        self.gps_position = d['gps_position']
        self.platform = d['platform']
        self.msg_ver = d['msg_ver']

    def as_dict(self):
        return vars(self)


if __name__ == '__main__':
    m = DdnMsg()
    print(m.as_dict())
