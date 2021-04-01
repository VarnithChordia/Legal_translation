class SentencePiece(object):

    def __init__(self,
                 model_type ='unigram',
                 num_symbols=10000,
                 split_by_white_space=False,
                 character_coverage=1.0,
                 file_name=None):
        self.num_symbols = num_symbols
        self.split_by_white_space = split_by_white_space
        self.character_coverage = character_coverage
        self.model_type = model_type


    def serialize(self,file_name):
        with open(file_name,'rb')