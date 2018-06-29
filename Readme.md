# Saleae Continuous Capture

This little script is handy for taking extended captures that span across hours, not just minutes.

First make sure you have `python3` and the Saleae package installed via `pip3`:

    pip3 install saleae

To use you can run the script once to get the sample rates provided by the print statement on line 26.

Lines 16-19 should be configured to your liking. (The duration and the sample rate.)

The Saleae Logic app also needs a slight tweak before this works:

1. Open Saleae Logic
1. Click on *Options* (top right corner) and go to *Preferences*
1. Nagivate to *Developer*
1. Enable the socket server using the default port.

Once configured you can simply run:

    python3 continuous_capture.py

That command should start a capture and continue as long as you set it for.

More information at [Circuit Dojo](https://www.circuitdojo.org/fundamentals/#current-measurements-over-time).

More information on the Saleae python plug-in [here](https://pypi.org/project/saleae/).
