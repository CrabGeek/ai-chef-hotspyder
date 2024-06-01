from enum import Enum

class SpyderStatus(Enum):
    RUNNING = "RUNNING"
    STOP = "STOP"
    UNKNOWN = "UNKNOWN"
    INITIATED = "INITIATED"