import hashlib
from datetime import datetime , date

#Block Class
class Block():
    def __init__(self , data , previous_hash = ""):
        #private
        self.__data = data # 3 elemanlı liste olmalıdır [1,2,3]
        self.__timestamp = datetime.now() #zaman adımını gösterir
        self.__previous_hash = previous_hash #önceki hash elemanı
        self.__hash = self.createHash() #bloğun hash değeri
        
    #properties
    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data  = data
        
    def getTimestamp(self):
        return self.__timestamp
    
    def getPreviousHash(self):
        return self.__previous_hash
    def setPreviousHash(self , _hash):
        self.__previous_hash = _hash
    
    def getHash(self):
        return self.__hash
    def setHash(self , _hash):
        self.__hash = _hash
    
    #methods
    def __convertData(self):
        data = ""
        for i in range(0,len(self.__data)):
            data += str(self.__data[i])
        return data
        
    def createHash(self):
        hashMethod = hashlib.sha256()
        data = self.__convertData()
        hashMethod.update((data + self.__timestamp.isoformat() + self.__previous_hash).encode("utf-8"))
        return hashMethod.hexdigest()
    
    
    
#BlockChain Class
class BlockChain():
    def __init__(self):
        #public
        self.chain = [self.__genesisBlock()]
    
    def __genesisBlock(self):
        return Block([],"0"*50)
    
    def lastChain(self):
        return self.chain[-1]
    
    def addBlock(self , newBlock):
        newBlock.setPreviousHash(self.lastChain().getHash())
        newBlock.setHash(newBlock.createHash())
        self.chain.append(newBlock)
        
    def validation(self):
        for i in range(1 , len(self.chain)):
            block = self.chain[i]
            previousBlock = self.chain[i - 1]
            
            if block.getHash() != block.createHash():
                return False
            elif block.getPreviousHash() != previousBlock.getHash():
                return False
            
        return True
    
    def showTheChain(self):
        chain = []
        for i in range(0,len(self.chain)):
            _block = {
                    "id":i,
                    "data":self.chain[i].getData(),
                    "timeStamp":self.chain[i].getTimestamp(),
                    "hash":self.chain[i].getHash(),
                    "previousHash":self.chain[i].getPreviousHash()
                    }
            chain.append(_block)
        blockChain = {}
        blockChain["blockChain"] = chain
        return blockChain
    
    
#örnek
MCoin = BlockChain()
MCoin.addBlock(Block([1,2,300]))
MCoin.addBlock(Block([2,3,500]))
MCoin.addBlock(Block([3,4,600]))
print(MCoin.validation())   
chainInfo = MCoin.showTheChain()
for i in range(0,len(chainInfo["blockChain"])):
    for j in chainInfo["blockChain"][i].keys():
        print(j , ":" ,chainInfo["blockChain"][i][j])
    print("-"*50)

MCoin.chain[2].setData([1,2,100])
print(MCoin.validation())

        