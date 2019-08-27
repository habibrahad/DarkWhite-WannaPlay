import os.path
import subprocess

try:
  VERSION = '3.0.0'
except Exception:
  VERSION = '3'

AUDIO_CACHE_PATH = os.path.join(os.getcwd(), 'audio_cache')
DISCORD_MSG_CHAR_LIMIT = 2000
