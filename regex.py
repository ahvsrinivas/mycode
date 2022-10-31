#!/usr/bin/python3

import re
contact = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"

conobj= re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)
print(conobj.group())
