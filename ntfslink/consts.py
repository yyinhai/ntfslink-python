from ctypes64 import *
#define FILE_ATTRIBUTE_READONLY             0x00000001
#define FILE_ATTRIBUTE_HIDDEN               0x00000002
#define FILE_ATTRIBUTE_SYSTEM               0x00000004
#define FILE_ATTRIBUTE_DIRECTORY            0x00000010
#define FILE_ATTRIBUTE_ARCHIVE              0x00000020
#define FILE_ATTRIBUTE_DEVICE               0x00000040
#define FILE_ATTRIBUTE_NORMAL               0x00000080
#define FILE_ATTRIBUTE_TEMPORARY            0x00000100
#define FILE_ATTRIBUTE_SPARSE_FILE          0x00000200
#define FILE_ATTRIBUTE_REPARSE_POINT        0x00000400
#define FILE_ATTRIBUTE_COMPRESSED           0x00000800
#define FILE_ATTRIBUTE_OFFLINE              0x00001000
#define FILE_ATTRIBUTE_NOT_CONTENT_INDEXED  0x00002000
#define FILE_ATTRIBUTE_ENCRYPTED            0x00004000
#define FILE_ATTRIBUTE_VIRTUAL              0x00010000
#define FILE_NOTIFY_CHANGE_FILE_NAME    0x00000001
#define FILE_NOTIFY_CHANGE_DIR_NAME     0x00000002
#define FILE_NOTIFY_CHANGE_ATTRIBUTES   0x00000004
#define FILE_NOTIFY_CHANGE_SIZE         0x00000008
#define FILE_NOTIFY_CHANGE_LAST_WRITE   0x00000010
#define FILE_NOTIFY_CHANGE_LAST_ACCESS  0x00000020
#define FILE_NOTIFY_CHANGE_CREATION     0x00000040
#define FILE_NOTIFY_CHANGE_SECURITY     0x00000100
#define FILE_ACTION_ADDED                   0x00000001
#define FILE_ACTION_REMOVED                 0x00000002
#define FILE_ACTION_MODIFIED                0x00000003
#define FILE_ACTION_RENAMED_OLD_NAME        0x00000004
#define FILE_ACTION_RENAMED_NEW_NAME        0x00000005
#define MAILSLOT_NO_MESSAGE             ((DWORD)-1)
#define MAILSLOT_WAIT_FOREVER           ((DWORD)-1)
#define FILE_CASE_SENSITIVE_SEARCH          0x00000001
#define FILE_CASE_PRESERVED_NAMES           0x00000002
#define FILE_UNICODE_ON_DISK                0x00000004
#define FILE_PERSISTENT_ACLS                0x00000008
#define FILE_FILE_COMPRESSION               0x00000010
#define FILE_VOLUME_QUOTAS                  0x00000020
#define FILE_SUPPORTS_SPARSE_FILES          0x00000040
#define FILE_SUPPORTS_REPARSE_POINTS        0x00000080
#define FILE_SUPPORTS_REMOTE_STORAGE        0x00000100
#define FILE_VOLUME_IS_COMPRESSED           0x00008000
#define FILE_SUPPORTS_OBJECT_IDS            0x00010000
#define FILE_SUPPORTS_ENCRYPTION            0x00020000
#define FILE_NAMED_STREAMS                  0x00040000
#define FILE_READ_ONLY_VOLUME               0x00080000
#define FILE_SEQUENTIAL_WRITE_ONCE          0x00100000
#define FILE_SUPPORTS_TRANSACTIONS          0x00200000
#define FILE_SUPPORTS_HARD_LINKS            0x00400000
#define FILE_SUPPORTS_EXTENDED_ATTRIBUTES   0x00800000
#define FILE_SUPPORTS_OPEN_BY_FILE_ID       0x01000000
#define FILE_SUPPORTS_USN_JOURNAL           0x02000000

## Macros
def CTL_CODE(DeviceType, Function, Method, Access):
	""" #define CTL_CODE( DeviceType, Function, Method, Access ) (((DeviceType) << 16) | ((Access) << 14) | ((Function) << 2) | (Method)) """
	return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method

def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
	""" #define DEVICE_TYPE_FROM_CTL_CODE(ctrlCode) (((DWORD)(ctrlCode & 0xffff0000)) >> 16) """
	return (ctrlCode & 0xffff0000) >> 16

def METHOD_FROM_CTL_CODE(ctrlCode):
	""" #define METHOD_FROM_CTL_CODE(ctrlCode) ((DWORD)(ctrlCode & 3)) """
	return ctrlCode & 3

# Windows definitions
ANYSIZE_ARRAY = 1
MAX_PATH = 260
INVALID_HANDLE_VALUE = -1
#NULL = 0
FALSE = 0
TRUE = 1

# Reparse Point buffer constants
REPARSE_MOUNTPOINT_HEADER_SIZE = sizeof(ULONG) + (2 * sizeof(USHORT))
MAX_NAME_LENGTH = 1024
MAX_REPARSE_BUFFER = 16 * MAX_NAME_LENGTH

# File command codes
FILE_READ_DATA = 0x0001
FILE_LIST_DIRECTORY = 0x0001
FILE_WRITE_DATA = 0x0002
FILE_ADD_FILE = 0x0002
FILE_APPEND_DATA = 0x0004
FILE_ADD_SUBDIRECTORY = 0x0004
FILE_CREATE_PIPE_INSTANCE = 0x0004
FILE_READ_EA = 0x0008
FILE_WRITE_EA = 0x0010
FILE_EXECUTE = 0x0020
FILE_TRAVERSE = 0x0020
FILE_DELETE_CHILD = 0x0040
FILE_READ_ATTRIBUTES = 0x0080
FILE_WRITE_ATTRIBUTES = 0x0100


# File attribute codes
FILE_ATTRIBUTE_READONLY = 0x00000001
FILE_ATTRIBUTE_HIDDEN = 0x00000002
FILE_ATTRIBUTE_SYSTEM = 0x00000004
FILE_ATTRIBUTE_DIRECTORY = 0x00000010
FILE_ATTRIBUTE_ARCHIVE = 0x00000020
FILE_ATTRIBUTE_DEVICE = 0x00000040
FILE_ATTRIBUTE_NORMAL = 0x00000080
FILE_ATTRIBUTE_TEMPORARY = 0x00000100
FILE_ATTRIBUTE_SPARSE_FILE = 0x00000200
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
FILE_ATTRIBUTE_COMPRESSED = 0x00000800
FILE_ATTRIBUTE_OFFLINE = 0x00001000
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 0x00002000
FILE_ATTRIBUTE_ENCRYPTED = 0x00004000
FILE_ATTRIBUTE_VIRTUAL = 0x00010000
FILE_ATTRIBUTE_REPARSE_DIRECTORY = (FILE_ATTRIBUTE_DIRECTORY | FILE_ATTRIBUTE_REPARSE_POINT)

# File open flags
FILE_FLAG_WRITE_THROUGH = 0x80000000
FILE_FLAG_OVERLAPPED = 0x40000000
FILE_FLAG_NO_BUFFERING = 0x20000000
FILE_FLAG_RANDOM_ACCESS = 0x10000000
FILE_FLAG_SEQUENTIAL_SCAN = 0x08000000
FILE_FLAG_DELETE_ON_CLOSE = 0x04000000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
FILE_FLAG_POSIX_SEMANTICS = 0x01000000
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_OPEN_NO_RECALL = 0x00100000
FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000
FILE_FLAG_REPARSE_BACKUP = FILE_FLAG_OPEN_REPARSE_POINT | FILE_FLAG_BACKUP_SEMANTICS

# Symbolic link flags
SYMLINK_FLAG_RELATIVE = 1
SYMLINK_FILE = 0x0
SYMLINK_DIR = 0x1

# The variables below deal with some of the more general stuff. (File
# IO, file access privileges, flags, basic typedefs, etc) There's a few
# flags dealing with reparse points that I left in this section for naming
# consistency.

# Generic access
GENERIC_READ = 0x80000000L
GENERIC_WRITE = 0x40000000L
GENERIC_EXECUTE = 0x20000000L
GENERIC_ALL = 0x10000000L

# File shared access
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004
FILE_SHARE_READ_WRITE = FILE_SHARE_READ | FILE_SHARE_WRITE
FILE_SHARE_ALL = FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE

# Creation flags
CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

# File Device codes
FILE_DEVICE_BEEP = 0x00000001
FILE_DEVICE_CD_ROM = 0x00000002
FILE_DEVICE_CD_ROM_FILE_SYSTEM = 0x00000003
FILE_DEVICE_CONTROLLER = 0x00000004
FILE_DEVICE_DATALINK = 0x00000005
FILE_DEVICE_DFS = 0x00000006
FILE_DEVICE_DISK = 0x00000007
FILE_DEVICE_DISK_FILE_SYSTEM = 0x00000008
FILE_DEVICE_FILE_SYSTEM = 0x00000009
FILE_DEVICE_INPORT_PORT = 0x0000000a
FILE_DEVICE_KEYBOARD = 0x0000000b
FILE_DEVICE_MAILSLOT = 0x0000000c
FILE_DEVICE_MIDI_IN = 0x0000000d
FILE_DEVICE_MIDI_OUT = 0x0000000e
FILE_DEVICE_MOUSE = 0x0000000f
FILE_DEVICE_MULTI_UNC_PROVIDER = 0x00000010
FILE_DEVICE_NAMED_PIPE = 0x00000011
FILE_DEVICE_NETWORK = 0x00000012
FILE_DEVICE_NETWORK_BROWSER = 0x00000013
FILE_DEVICE_NETWORK_FILE_SYSTEM = 0x00000014
FILE_DEVICE_NULL = 0x00000015
FILE_DEVICE_PARALLEL_PORT = 0x00000016
FILE_DEVICE_PHYSICAL_NETCARD = 0x00000017
FILE_DEVICE_PRINTER = 0x00000018
FILE_DEVICE_SCANNER = 0x00000019
FILE_DEVICE_SERIAL_MOUSE_PORT = 0x0000001a
FILE_DEVICE_SERIAL_PORT = 0x0000001b
FILE_DEVICE_SCREEN = 0x0000001c
FILE_DEVICE_SOUND = 0x0000001d
FILE_DEVICE_STREAMS = 0x0000001e
FILE_DEVICE_TAPE = 0x0000001f
FILE_DEVICE_TAPE_FILE_SYSTEM = 0x00000020
FILE_DEVICE_TRANSPORT = 0x00000021
FILE_DEVICE_UNKNOWN = 0x00000022
FILE_DEVICE_VIDEO = 0x00000023
FILE_DEVICE_VIRTUAL_DISK = 0x00000024
FILE_DEVICE_WAVE_IN = 0x00000025
FILE_DEVICE_WAVE_OUT = 0x00000026
FILE_DEVICE_8042_PORT = 0x00000027
FILE_DEVICE_NETWORK_REDIRECTOR = 0x00000028
FILE_DEVICE_BATTERY = 0x00000029
FILE_DEVICE_BUS_EXTENDER = 0x0000002a
FILE_DEVICE_MODEM = 0x0000002b
FILE_DEVICE_VDM = 0x0000002c
FILE_DEVICE_MASS_STORAGE = 0x0000002d
FILE_DEVICE_SMB = 0x0000002e
FILE_DEVICE_KS = 0x0000002f
FILE_DEVICE_CHANGER = 0x00000030
FILE_DEVICE_SMARTCARD = 0x00000031
FILE_DEVICE_ACPI = 0x00000032
FILE_DEVICE_DVD = 0x00000033
FILE_DEVICE_FULLSCREEN_VIDEO = 0x00000034
FILE_DEVICE_DFS_FILE_SYSTEM = 0x00000035
FILE_DEVICE_DFS_VOLUME = 0x00000036
FILE_DEVICE_SERENUM = 0x00000037
FILE_DEVICE_TERMSRV = 0x00000038
FILE_DEVICE_KSEC = 0x00000039
FILE_DEVICE_FIPS = 0x0000003A
FILE_DEVICE_INFINIBAND = 0x0000003B
FILE_DEVICE_VMBUS = 0x0000003E
FILE_DEVICE_CRYPT_PROVIDER = 0x0000003F
FILE_DEVICE_WPD = 0x00000040
FILE_DEVICE_BLUETOOTH = 0x00000041
FILE_DEVICE_MT_COMPOSITE = 0x00000042
FILE_DEVICE_MT_TRANSPORT = 0x00000043
FILE_DEVICE_BIOMETRIC = 0x00000044
FILE_DEVICE_PMI = 0x00000045

# Methods
METHOD_BUFFERED = 0
METHOD_IN_DIRECT = 1
METHOD_OUT_DIRECT = 2
METHOD_NEITHER = 3
METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT

# Access
FILE_ANY_ACCESS = 0
FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
FILE_READ_ACCESS = 0x0001
FILE_WRITE_ACCESS = 0x0002

# Reparse Tags
IO_REPARSE_TAG_RESERVED_ZERO = 0x00000000
IO_REPARSE_TAG_SYMBOLIC_LINK = IO_REPARSE_TAG_RESERVED_ZERO
IO_REPARSE_TAG_MOUNT_POINT = 0xA0000003L
IO_REPARSE_TAG_HSM = 0xC0000004L
IO_REPARSE_TAG_SIS = 0x80000007L

#define FSCTL_SET_REPARSE_POINT CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 41, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_REPARSE_POINT = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 41, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)

#define FSCTL_GET_REPARSE_POINT CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 42, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_GET_REPARSE_POINT = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 42, METHOD_BUFFERED, FILE_ANY_ACCESS)

#define FSCTL_DELETE_REPARSE_POINT CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 43, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_DELETE_REPARSE_POINT = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 43, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)

## Access Types
# The following are masks for the predefined standard access types
DELETE = 0x00010000L
READ_CONTROL = 0x00020000L
WRITE_DAC = 0x00040000L
WRITE_OWNER = 0x00080000L
SYNCHRONIZE = 0x00100000L

STANDARD_RIGHTS_REQUIRED = 0x000F0000L
STANDARD_RIGHTS_READ = READ_CONTROL
STANDARD_RIGHTS_WRITE = READ_CONTROL
STANDARD_RIGHTS_EXECUTE = READ_CONTROL

STANDARD_RIGHTS_ALL = 0x001F0000L

SPECIFIC_RIGHTS_ALL = 0x0000FFFFL

# AccessSystemAcl access type
ACCESS_SYSTEM_SECURITY = 0x01000000L

# MaximumAllowed access type
MAXIMUM_ALLOWED = 0x02000000L

# Security Tokens
TOKEN_ASSIGN_PRIMARY = 0x0001
TOKEN_DUPLICATE = 0x0002
TOKEN_IMPERSONATE = 0x0004
TOKEN_QUERY = 0x0008
TOKEN_QUERY_SOURCE = 0x0010
TOKEN_ADJUST_PRIVILEGES = 0x0020
TOKEN_ADJUST_GROUPS = 0x0040
TOKEN_ADJUST_DEFAULT = 0x0080
TOKEN_ADJUST_SESSIONID = 0x0100

TOKEN_ALL_ACCESS_P = STANDARD_RIGHTS_REQUIRED | TOKEN_ASSIGN_PRIMARY | TOKEN_DUPLICATE | TOKEN_IMPERSONATE | TOKEN_QUERY | TOKEN_QUERY_SOURCE | TOKEN_ADJUST_PRIVILEGES | TOKEN_ADJUST_GROUPS | TOKEN_ADJUST_DEFAULT
TOKEN_ALL_ACCESS = TOKEN_ALL_ACCESS_P | TOKEN_ADJUST_SESSIONID

# SE Privileges
SE_PRIVILEGE_ENABLED_BY_DEFAULT = 0x00000001L
SE_PRIVILEGE_ENABLED = 0x00000002L
SE_PRIVILEGE_REMOVED = 0X00000004L
SE_PRIVILEGE_USED_FOR_ACCESS = 0x80000000L

SE_PRIVILEGE_VALID_ATTRIBUTES = SE_PRIVILEGE_ENABLED_BY_DEFAULT | SE_PRIVILEGE_ENABLED | SE_PRIVILEGE_REMOVED | SE_PRIVILEGE_USED_FOR_ACCESS

# Privilege Set Control flags
PRIVILEGE_SET_ALL_NECESSARY = 1

# Privilege names.
SE_RESTORE_NAME = 'SeRestorePrivilege'
SE_BACKUP_NAME = 'SeBackupPrivilege'
SE_CREATE_SYMBOLIC_LINK_NAME = 'SeCreateSymbolicLinkPrivilege'
SE_MANAGE_VOLUME_NAME = 'SeManageVolumePrivilege'
SE_LOAD_DRIVER_NAME = 'SeLoadDriverPrivilege'
SE_UNSOLICITED_INPUT_NAME = 'SeUnsolicitedInputPrivilege'