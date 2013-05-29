'''
Example: python ./examples/create_bond.py

Creates bond interface.
'''
from pyroute2 import ipdb

ip = ipdb()

try:

    # The same scheme works for bridge interfaces too: you
    # can create a bridge interface and enslave some ports
    # to it just as below.

    with ip.create(kind='bond', ifname='bond,james') as i:
        # enslave two interfaces: tap0 and tap1
        i.add_port(ip.tap0.index)
        i.add_port(ip.tap1.index)
        # make an example more scary: add IPs to the bond,james
        i.add_ip('10.251.0.1', 24)
        i.add_ip('10.251.0.2', 24)

finally:
    ip.shutdown()
