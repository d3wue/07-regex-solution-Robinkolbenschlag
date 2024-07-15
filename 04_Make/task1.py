import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

regv4 = re.compile('^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$')
regv6 = re.compile('^([0-9a-f]{4}:){7}[0-9a-f]{4}$')


regv4Counter = 0
regv6Counter = 0
invalidCounter = 0

for ip in ipAddresses:
    m1 = regv4.match(ip)
    m2 = regv6.match(ip)
    if m1:
        print(m1.group(0))
        regv4Counter += 1
    elif m2:
        regv6Counter += 1
    else:
        invalidCounter += 1

print(f'Valid IPv4 addresses: {regv4Counter}')
print(f'Valid IPv6 addresses: {regv6Counter}')
print(f'Invalid IP addresses: {invalidCounter}')

