import sys
import urllib3
import datetime

from pybotvac import (
    Account,
    Neato,
    OAuthSession,
    PasswordlessSession,
    PasswordSession,
    Vorwerk,
)

def log(level, msg):
  print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - ",level," - ", msg)

def info(msg):
  log("INFO", msg)

def warn(msg):
  log("WARN", msg)

def error(msg):
  log("ERROR", msg)



urllib3.disable_warnings()

# Set email address and client_id for vorwerk
email = "your.email@dress.com"
# do not change
client_id = "KY4YbVAvtgB7lp8vIbWQ7zLk3hssZlhR"

# Set your vendor
vendor = Vorwerk()

##########################
# Authenticate via One Time Password
##########################
session = PasswordlessSession(client_id=client_id, vendor=vendor)
session.send_email_otp(email)
code = input("Enter the code: ")
session.fetch_token_passwordless(email, code)

account = Account(session)
info("###########################################################")
info("Token : " + str(session._token))
info("###########################################################")
info("")


info("Robots:")
for robot in account.robots:
  info(robot)

  info("State:\n"+str(robot.state) )
  info("     isCharging  : " + str(robot.state["details"]["isCharging"]))
  info("     isDocked    : " + str(robot.state["details"]["isDocked"]))
  info("     charge      : " + str(robot.state["details"]["charge"]))
  info("Schedule enabled : " + str( robot.schedule_enabled) )
