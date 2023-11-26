class Solution(object):
    def defangIPaddr(self, address):
        new_add = address.replace('.', '[.]')
        return new_add