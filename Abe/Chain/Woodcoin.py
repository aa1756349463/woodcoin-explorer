from .Sha256Chain import Sha256Chain

class Woodcoin(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Woodcoin'
        chain.code3 = 'LOG'
        chain.address_version = '\x49'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xfb\xc0\xb8\xdb'
        Sha256Chain.__init__(chain, **kwargs)
