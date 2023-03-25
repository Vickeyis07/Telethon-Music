import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6181590493:AAGJfymNNLs3haPSWYFOWAev4nyNZr69CKA")
    STRING_SESSION = os.environ.get("STRING_SESSION", " 1BVtsOKEBu4t809bUb7Me8dPS9FkCHfaQCm4vLl9gAd5FD3kjteL4vXnEFlemkXn_iufFtXuNjRKLUT5qfqyglNTznmYwXOHAmvtzGD2izZJiQdqFonGBx-d-XTl2BKC5dImuXTfZQTZM2LqYIwtWmd_JWneq2CiCIr-rxIhjfCwXzYqNkME7NAA2ofm1uj0MUe1RqQ0ygvejLk0MJUeoN7cVaACsxSQFG8p5dPXiUpuuWK0UtG_4P3vti45pVwlod_GYy3LxhU6YR1wbyAXWbuSIXCUugydgf4VJ9T-uEv8RZh6kvxhk9gWp7R_WvnUVd2FfsD8MphQPwQfcNmusFzIa5Hr9jAo=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
