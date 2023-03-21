from twisted.internet import ssl

class ClientContextFactory(ssl.ClientContextFactory):
    def __init__(self, redis_config):
        self.redis_config = redis_config

    def getContext(self):
        ctx = ssl.ClientContextFactory.getContext(self)
        if (self.redis_config.redis_certificate):
            ctx.use_certificate_file(self.redis_config.redis_certificate))
        if (self.redis_config.private_key):
            ctx.use_privatekey_file(self.redis_config.private_key)
        if (self.redis_config.ca_file):
            ctx.load_verify_locations(cafile=self.redis_config.ca_file)
        elif (self.redis_config.ca_path):
            ctx.load_verify_locationa(capath=self.redis_config.ca_path)
        return ctx