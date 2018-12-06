import ipcalc

class SubnetCalclator:

    subnet = ipcalc.Network('')

    def set_subnet(self,*args):
        
        self.subnet = ipcalc.Network(args)

    def get_subnet(self):

        return self.subnet

    def get_netmask(self):

        return str(self.subnet.netmask())

    def get_subnet_list(self):

        temp = []

        for x in self.subnet:
            temp.append(x)

        return x