import copy


# -----------------------------------
# these are SQS codes, not GUI codes
# -----------------------------------

OPCODE_SQS_DDH_BOOT = 'DDH_BOOT'
OPCODE_SQS_DDH_ERROR_BLE_HW = 'DDH_ERROR_BLE_HARDWARE'
OPCODE_SQS_DDH_ERROR_GPS_HW = 'DDH_ERROR_GPS_HARDWARE'
OPCODE_SQS_DDH_ALIVE = 'DDH_ALIVE'
OPCODE_SQS_LOGGER_DL_OK = 'LOGGER_DOWNLOAD'
OPCODE_SQS_LOGGER_ERROR_OXYGEN = 'LOGGER_ERROR_OXYGEN'
OPCODE_SQS_LOGGER_MAX_ERRORS = 'LOGGER_ERRORS_MAXED_RETRIES'
OPCODE_SQS_LOGGER_LOW_BATTERY = 'LOGGER_LOW_BATTERY'


ALL_OPCODE_SQS = [
    OPCODE_SQS_DDH_BOOT,
    OPCODE_SQS_DDH_ERROR_BLE_HW,
    OPCODE_SQS_DDH_ERROR_GPS_HW,
    OPCODE_SQS_DDH_ALIVE,
    OPCODE_SQS_LOGGER_DL_OK,
    OPCODE_SQS_LOGGER_ERROR_OXYGEN,
    OPCODE_SQS_LOGGER_MAX_ERRORS,
    OPCODE_SQS_LOGGER_LOW_BATTERY
]


def get_ddn_msg_list_of_opcodes():
    return ALL_OPCODE_SQS


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
        self.data = None

        # for testing
        # self.fake_field = None
        # del self.msg_ver

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
        self.data = d['data']

    def as_dict(self):
        return vars(self)

    def validate_ddn_msg_fields_names(self):
        # check myself as a message
        d = copy.deepcopy(self.as_dict())

        try:
            del d['reason']
            del d['logger_mac']
            del d['logger_sn']
            del d['project']
            del d['vessel']
            del d['ddh_commit']
            del d['utc_time']
            del d['local_time']
            del d['box_sn']
            del d['hw_uptime']
            del d['gps_position']
            del d['platform']
            del d['msg_ver']
            del d['data']
        except KeyError as e:
            print('error: DdnMsg object is missing key ->', e)
            return 1

        try:
            assert d == {}
        except AssertionError:
            print('error: DdnMsg object has extra unknown key ->', d)
            return 1
