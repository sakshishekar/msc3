class predictor:
    def __init__(self):
        self.minNo = 100
        self.maxYes = 0
        self.weight={}
    def train(self, temp, wear):
        if temp not in self.weight:
            self.weight[temp] =0
            
        if self.maxYes>temp and wear == false :
           self.maxYes=temp
           self.weight[temp]= self.weight[temp] -1
        if self.minNo<temp and wear == true :
           self.minNo=temp
           self.weight[temp]+=1
                   
    def test(self, temp):
        if temp <= self.maxYes:
            print("Recommended to wear warm clothes at {temp} degree.".format(temp=temp))
            return True
        elif temp >= self.minNo:
            print("Not Recommended to wear warm clothes at {temp} degrees.".format(temp=temp))
            return False
        else:
            print("cannot predict clothing for {temp} degrees.".format(temp=temp))
            return 0
                    
p=predictor()
p.train(24,False)
p.train(14,True)
p.train(19,True)
p.train(20,True)
p.train(25,False)
p.train(19,True)
p.train(20,True)
p.train(25,False)

p.test(24)
p.test(14)
p.test(19)
p.test(20)
p.test(25)
p.test(19)
p.test(20)
p.test(25)


