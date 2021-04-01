import tempfile
import os
import sentencepiece as spm


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
        with open(file_name,'rb') as f:
            return f.read()


    def deserialize(self,model_serialized):
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, 'wb') as tmp:
                tmp.write(model_serialized)
            self.load_model(path, add_suffix=False)
        finally:
            os.remove(path)

    def load_model(self,file_prefix):

        self.model = spm.SentencePieceProcessor()
        self.model.Load(file_prefix)
        self._model_serialized = self.serialize(file_prefix)


    def tokenize(self,line, insert_start=None, insert_end=None, sample=None,pre_tokenize = None):
        # if pre_tokenize:

        if not pre_tokenize:
            self.model.EncodeAsIds()




    @staticmethod
    def train_sp(**kwargs):


        # kwargs.update({'unk_piece': UNK_TOKEN, 'bos_piece': BOS_TOKEN,
        #                'eos_piece': EOS_TOKEN, 'pad_piece': PAD_TOKEN,
        #                'unk_id': UNK, 'bos_id': BOS,
        #                'eos_id': EOS, 'pad_id': PAD,
        #                'unk_surface': UNK_TOKEN,
        #                })

        for arg, val in kwargs.items():
            if isinstance(val, bool):
                kwargs[arg] = 'true' if val else 'false'

        config = ' '.join(['{}={}'.format(name, value)
                           for name, value in kwargs.items() if value is not None])
        spm.SentencePieceTrainer.Train(config)





