class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address_components = address.split('.')
        defanged_address = "[.]".join(address_components)
        
        return defanged_address