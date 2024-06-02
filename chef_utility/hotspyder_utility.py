from concurrent.futures import ThreadPoolExecutor
from chef_utility import settings as utility_settings

THREAD_POOL = ThreadPoolExecutor(
    max_workers=utility_settings.THREAD_POOL_SIZE,
    thread_name_prefix=utility_settings.THREAD_NAME_PREFIX,
)


MQ_CHANNEL_CONSUMMING_POOL = ThreadPoolExecutor(
    max_workers=utility_settings.THREAD_POOL_SIZE,
    thread_name_prefix=utility_settings.THREAD_NAME_PREFIX,
)