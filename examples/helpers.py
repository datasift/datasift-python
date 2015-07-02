from __future__ import print_function
import time
from datasift import Client
from datasift.helpers.recording import *

datasift = Client("<user_name>", "<api_key>")

rec = PylonRecording(datasift, "<recording_hash>")

rec.refresh()

print(rec.hash)

print("STATUS: "+rec.status)

rec.analysis.filter = 'fb.author.age exists'

rec.analysis.start = rec.start

rec.analysis.end = datetime.datetime.now()

print("Create a time series")

my_ts = rec.analysis.timeseries('month')

print("Redacted: "+str(my_ts.redacted))

print("Total interactions: "+str(my_ts.interactions))

print(my_ts.results)

print("Create a frequency distribution")

my_fd = rec.analysis.freqdist('fb.author.region')

print("Redacted: "+str(my_fd.redacted))

print("Total interactions: "+str(my_fd.interactions))

print(my_fd.results)