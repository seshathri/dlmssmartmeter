from gurux_dlms import *

client = GXDLMSClient(True)

# // Count server address from serial number.
serverAddress = client.getServerAddress(Serial number)
# Count server address from logican and physical address.
serverAddress = client.getServerAddress2(logical Address, physical Address, Address size in bytes)

#pylint: disable=too-few-public-methods,broad-except
class myclient():
    @classmethod
    def main(cls, args):
        reply = GXReplyData()
        data = self.client.snrmRequest()
        if data:
            self.readDLMSPacket(data, reply)
            self.client.parseUAResponse(reply.data)
            size = self.client.limits.maxInfoTX + 40
            self.replyBuff = bytearray(size)
            reply.clear()
            self.readDataBlock(self.client.aarqRequest(), reply)
            self.client.parseAareResponse(reply.data)
            reply.clear()
        if self.client.authentication.value > Authentication.LOW.value:
        for it in self.client.getApplicationAssociationRequest():
            self.readDLMSPacket(it, reply)
            self.client.parseApplicationAssociationResponse(reply.data)

if __name__ == '__main__':
   
    myclient.main(sys.argv)
