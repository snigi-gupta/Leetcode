# https://leetcode.com/problems/defanging-an-ip-address/
address = "1.1.1.1"
address = address.replace(".", "[.]")
print(address)
address = "1.1.1.1"
print('[.]'.join(address.split('.')))