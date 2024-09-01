import unittest
from collections import defaultdict
from main import get_protocol_name

class TestFlowLogProcessor(unittest.TestCase):

    def setUp(self):
        # Set up any test-specific variables
        self.lookup_table = {
            ('25', 'tcp'): 'sv_P1',
            ('443', 'tcp'): 'sv_P2',
            ('23', 'tcp'): 'sv_P1',
            ('110', 'tcp'): 'email',
            ('993', 'tcp'): 'email',
            ('143', 'tcp'): 'email'
        }
        
        self.protocol_map = {
            '6': 'tcp',
            '17': 'udp',
            '1': 'icmp'
        }
        
        # Sample flow log entries as strings
        self.sample_logs = [
            "2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK",
            "2 123456789012 eni-9h8g7f6e 172.16.0.100 203.0.113.102 110 49156 6 12 9000 1620140761 1620140821 ACCEPT OK",
            "2 123456789012 eni-7i8j9k0l 172.16.0.101 192.0.2.203 993 49157 6 8 5000 1620140761 1620140821 ACCEPT OK"
        ]
        
    def test_get_protocol_name(self):
        # Test that protocol numbers are correctly converted to names
        self.assertEqual(get_protocol_name('6'), 'tcp')
        self.assertEqual(get_protocol_name('17'), 'udp')
        self.assertEqual(get_protocol_name('1'), 'icmp')
        self.assertEqual(get_protocol_name('999'), 'unknown')

    def test_tagging(self):
        tag_counts = defaultdict(int)
        port_protocol_counts = defaultdict(int)
        
        for line in self.sample_logs:
            fields = line.strip().split()
            dstport = fields[5]
            protocol_number = fields[7]
            protocol_name = get_protocol_name(protocol_number)
            
            tag = self.lookup_table.get((dstport, protocol_name), 'Untagged')
            tag_counts[tag] += 1
            port_protocol_counts[(dstport, protocol_name)] += 1

        # Test expected counts
        self.assertEqual(tag_counts['sv_P1'], 1)
        self.assertEqual(tag_counts['email'], 2)
        self.assertEqual(tag_counts['Untagged'], 0)
        
        self.assertEqual(port_protocol_counts[('25', 'tcp')], 1)
        self.assertEqual(port_protocol_counts[('110', 'tcp')], 1)
        self.assertEqual(port_protocol_counts[('993', 'tcp')], 1)

if __name__ == '__main__':
    unittest.main()
