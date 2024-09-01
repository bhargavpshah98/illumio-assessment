# illumio-assessment

## Problem Statement
Write a program that can parse a file containing flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a csv file, and it has 3 columns, dstport, protocol, and tag. The dstport and protocol combination decide what tag can be applied.   

## Solution

### File Structure
- **input.txt** is the simple text file that contains sample log data.
- **lookup_table.csv** is a given sample file that contains dstport, protocol, and tag.
- **main.py** is the file that contains logic to produce the output files of tag_counts.csv and port_protocol_counts.csv
- **tag_counts.csv** is the **output** file containing the number of counts per tag, and if the tag is not found then it returns untagged.
- **port_protocol_counts.csv** is the **output** file that measures the count of combination from port and protocols from the log data.

### Logic and Assumptions
The logic that is used in developing the code is as follows:
- tags are produced based on the combination of dstport and protocol, which are saved in map data structure as:
    **lookup_table[(dstport, protocol)] = tag**
- **get_protocol_name** function is used for mapping the protocol number with its corresponding protocol name, which is required in the port_protocol_counts.csv file
- **defaultdict** is used for counting the tags and port_protocol to its corresponding values and it also makes the code efficient.
- we are now parsing the log file which is input.txt (could be any other name as well) using read mode. 
  I have made the following **assumptions** of the data as per the AWS reference for flow logs and the sample input data given:
    1. 6th column in input log data is dstport
    2. 8th column in input log data is protocol number
  Once, we have received the above values, it is mapped with the protocol name and lookup table, and the count for the required output starts from here.
- tag counts are written in the tag_counts.csv file using Python's write function.
- port, protocol, and its counts are written in port_protocol_counts.csv file using the inbuilt file write function.

### Steps to reproduce and run the code
- I have not included the output files in this repository so that you can easily reproduce and run the code on your machine.
- Steps to follow are:
  - Clone the repository
  - go to the folder where you have cloned this repository and run:
    **python3 main.py**
  - This would produce 2 output files "tag_counts.csv" and "port_protocol_counts.csv"

### Although I have not included the output files in the repository, these are the screenshots of it
![Alt text](https://github.com/user-attachments/assets/e454ad61-d67e-4b99-8224-66208cb743c5)
![Alt text](https://github.com/user-attachments/assets/cfd44f9b-398f-40f4-8527-3c3dc4be2c4e)

I hope everything is clear. Please don't hesitate to reach out or ask any questions.
