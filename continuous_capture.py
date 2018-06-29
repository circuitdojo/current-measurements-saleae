#!/usr/bin/env python3

# One common issue is that Saleae records traces into memory, which means that
# it can't handle very long captures. This example shows how to use scripting to
# do long recordings over time. There will be brief gaps every time Saleae saves
# the old recording and starts a new one.

# Modified by Jared Wolff @ Circuit Dojo jared@circuitdojo.org

import os
import time

import saleae

folder = time.strftime('%Y-%m-%d-%H%M%S')

# Variables to tweak
samples_per_sec = 100
samples_per_capture = 60*60*24 # 60 seconds * 60 minutes * 24 hours
number_of_captures = 1
sample_rate_selected = 8
# End variables

os.mkdir(folder)

s = saleae.Saleae()

print( "Sample rates:\n" + ''.join( str(v)+"\n" for v in s.get_all_sample_rates()) )
print( "Default: " + str(s.get_all_sample_rates()[sample_rate_selected]))

s.set_active_channels([],[0])
s.set_num_samples(samples_per_sec * samples_per_capture)
s.set_sample_rate(s.get_all_sample_rates()[sample_rate_selected])

for i in range(0,number_of_captures):
	path = os.path.abspath(os.path.join(folder, str(i)))
	s.capture_to_file(path)
