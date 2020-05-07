import randompy
import socket
import struct


def main():
    """
    Function get min subnet from generated ips array
    :return:
    """
    print(get_min_subnet(gen_addrs(100)))


def get_min_subnet(source_ips):
    """Return minimal ip address with subnet from ips array.

    >>> get_min_subnet(["37.97.186.66"])
    37.97.186.66/4

    """
    bits = 0
    result = 0
    for ip in source_ips:
        ip_int = ip2int(ip)
        for bits in range(0, 31):
            max_addr = 4294967295 >> bits
            if ip_int >= max_addr:
                result = ip_int
                break

    res_ip = int2ip(result)
    return f'{res_ip}/{bits + 1}'


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
