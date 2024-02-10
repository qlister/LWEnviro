# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = True

# enter a nickname for this board
nickname = "kitchen"

# network access details
wifi_ssid = "My Wi-Fi"
wifi_password = "sc00byd00"

# how often to wake up and take a reading (in minutes)
reading_frequency = 5

# how often to trigger a resync of the onboard RTC (in hours)
resync_frequency = 168

# where to upload to ("web_hook", "mqtt", "adafruitio")
destination = "mqtt"

# how often to upload data (number of cached readings)
upload_frequency = 1

# web hook settings
custom_http_url = None
custom_http_username = None
custom_http_password = None

# mqtt broker settings
mqtt_broker_address = "192.168.86.30"
mqtt_broker_username = "ha_mqtt"
mqtt_broker_password = "sc00byd00"

# adafruit ui settings
adafruit_io_username = None
adafruit_io_key = None

# influxdb settings
influxdb_org = None
influxdb_url = None
influxdb_token = None
influxdb_bucket = None

# grow specific settings
auto_water = False
moisture_target_1 = 50
moisture_target_2 = 50
moisture_target_3 = 50