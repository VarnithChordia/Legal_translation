import abc

class EncodeDecoder:
    @abc.abstractmethod
    def forward(self, batch):
        raise NotImplementedError("abstract method forward must be implemented")

    @abc.abstractmethod
    def score(self,batch):
        raise NotImplementedError("abstract method score must be implemented")


    @abc.abstractmethod
    def create(self, *args, **kwargs):
        raise NotImplementedError("abstract method create must be implemented")



    def get_n_trainable_params(self):
        pp = 0
        for p in list(self.parameters()):
            if p.requires_grad:
                num = 1
                for s in list(p.size()):
                    num = num * s
                pp += num
        return pp

