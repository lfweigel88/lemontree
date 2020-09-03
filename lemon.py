#!/usr/bin/python3
import time
import json
from influxdb import InfluxDBClient
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)
client = InfluxDBClient('localhost')
client.switch_database('plants')


while True:
    # read moisture level through capacitive touch pad
    # read temperature from the temperature sensor
    #temp = ss.get_temp()
    avg = 0.0
    avg2 = 0.0
    i = 0
    while i < 12:
        touch = ss.moisture_read()
        touch = touch/1024 * 100
        temp = ss.get_temp()
        avg = touch + avg
        avg2 = temp + avg2
        i = i + 1
        print(str(i) + " : " + str(avg) + ", " + str(avg2))
        time.sleep(5)
    touch = avg/12
    temp = avg2/12
    print("moisture: " + str(touch))
    print("temperature: " + str(temp))
    json_body = [
      {
        "measurement": "lemon",
        "fields": {
              "moisture": touch,
              "temperature": temp
        }
      }
    ]
    client.write_points(json_body)
