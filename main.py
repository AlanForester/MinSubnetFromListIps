import ipaddress
import pprint

import netaddr
import randompy
import socket
import struct


def main():
    """
    Function get min subnet from generated ips array
    :return:
    """
    print("Result: ", get_min_subnet(gen_addrs(2)))


def get_min_subnet(source_ips):
    """Return minimal ip address with subnet from ips array.

    >>> get_min_subnet(["156.92.87.158","209.190.202.178"])
    128.0.0.0/1

    """
    min_addr = 4294967296
    max_addr = 0
    for ip in source_ips:
        print(ip)
        ip_int = ip2int(ip)
        if min_addr > ip_int:
            min_addr = ip_int
        if max_addr < ip_int:
            max_addr = ip_int

    result = 'Error'
    for bit in reversed([i for i in range(0, 33)]):
        subnet = f'{int2ip(max_addr)}/{bit}'
        n = netaddr.IPNetwork(subnet)
        if netaddr.IPAddress(int2ip(min_addr)) in netaddr.IPNetwork(n.cidr):
            result = n.cidr
            break

    return str(result)


def gen_addrs(count):
    """Return the list of ip addresses.

    >>> gen_addrs(1)
    ["37.97.186.66"]

    """
    return [randompy.ipv4address() for _ in range(0, count)]


def ip2int(addr):
    """Return int by ip.

    >>> ip2int("37.97.186.66")
    627161666

    """
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    """Return ip by int.

    >>> ip2int(627161666)
    "37.97.186.66"

    """
    return socket.inet_ntoa(struct.pack("!I", addr))


if __name__ == "__main__":
    main()
