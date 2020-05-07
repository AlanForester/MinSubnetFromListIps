from unittest import TestCase

from main import int2ip, ip2int, gen_addrs, get_min_subnet


class TestMain(TestCase):
    def test_int2ip(self):
        self.assertEqual(int2ip(627161666), "37.97.186.66")

    def test_ip2int(self):
        self.assertEqual(ip2int("37.97.186.66"), 627161666)

    def test_gen_addrs(self):
        self.assertEqual(len(gen_addrs(5)), 5)
        addr = gen_addrs(1)[0]
        dots_pos = [pos for pos, char in enumerate(addr) if char == '.']
        self.assertEqual(len(dots_pos), 3)

    def test_get_min_subnet(self):
        addrs = gen_addrs(1)
        result = get_min_subnet(addrs)
        self.assertEqual(result.find(addrs[0]), 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
