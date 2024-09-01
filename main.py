import csv
from collections import defaultdict

# Loading lookup table into a dictionary
lookup_table = {}
with open('lookup_table.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    for row in reader:
        dstport, protocol, tag = row[0], row[1].lower(), row[2]
        lookup_table[(dstport, protocol)] = tag

# Function to convert protocol number to name
def get_protocol_name(proto_number):
    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp',
        # We can add more mappings here if needed
    }
    return protocol_map.get(proto_number, 'unknown')

# Processing flow logs
tag_counts = defaultdict(int)
port_protocol_counts = defaultdict(int)

with open('input.txt', mode='r') as infile:
    # next(infile)  # Skip header line
    # Skip this logic assuming that input file does not have header included
    for line in infile:
        fields = line.strip().split()

        dstport = fields[5]
        protocol_number = fields[7]
        protocol_name = get_protocol_name(protocol_number)

        tag = lookup_table.get((dstport, protocol_name), 'Untagged')
        tag_counts[tag] += 1

        port_protocol_counts[(dstport, protocol_name)] += 1

# Write tag counts to output file
with open('tag_counts.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Tag', 'Count'])
    for tag, count in tag_counts.items():
        writer.writerow([tag, count])

# Write port/protocol counts to output file
with open('port_protocol_counts.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Port', 'Protocol', 'Count'])
    for (dstport, protocol), count in port_protocol_counts.items():
        writer.writerow([dstport, protocol, count])