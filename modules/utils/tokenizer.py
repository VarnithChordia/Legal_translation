import tempfile
import os
import sentencepiece as spm
import torch



class BPETokenizer:
    def __init__(self,file_prefix,
                 additional_tokens,
                 num_symbols,
                 total_symbols,
                 min_frequency,
                 separator,
                 **kwargs):
        super(BPETokenizer, self).__init__(file_prefix=file_prefix,
                                           additional_tokens=additional_tokens,
                                           **kwargs)
        self.num_symbols = num_symbols
        self.min_frequency = min_frequency
        self.total_symbols = total_symbols
        self.separator = separator
        self.file_prefix = '/data/vchordia/LegalData/wmt16_de_en/train.tok.clean.moses_pretok.bpe.32000.shared-de_en.codes'
        self.vocab_file = self._vocab_filename(self.file_prefix)
        # self.codes_file = '{}.codes'.format(self.file_prefix)
        # if os.path.isfile(self.codes_file):
        #     self.set_bpe(self.codes_file)


    def

class SentencePiece(object):

    def __init__(self,
                 file_prefix,
                 model_type ='unigram',
                 num_symbols=10000,
                 split_by_white_space=False,
                 character_coverage=1.0,
                 file_name=None):
        self.file_prefix = os.path.abspath(file_prefix)
        self.num_symbols = num_symbols
        self.split_by_white_space = split_by_white_space
        self.character_coverage = character_coverage
        self.model_type = model_type


    def serialize(self,file_prefix):
        with open(file_prefix,'rb') as f:
            return f.read()


    def deserialize(self,model_serialized):
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, 'wb') as tmp:
                tmp.write(model_serialized)
            self.load_model(path, add_suffix=False)
        finally:
            os.remove(path)

    def load_model(self, file_prefix):

        self.model = spm.SentencePieceProcessor()
        self.model.Load(file_prefix)
        self._model_serialized = self.serialize(file_prefix)


    def tokenize(self,line, insert_start=None, insert_end=None, sample=None,pre_tokenize = None):

        targets = self.model.EncodeAsIds(line)
        return torch.tensor(targets, dtype=torch.long)

    def idx2word(self, idx):
        return self.model.IdToPiece(idx)

    def word2idx(self, word):
        return self.model.PieceToId(word)

    @property
    def vocab_size(self):
        return len(self.model)


    def __getstate__(self):
        state = self.__dict__.copy()
        del state['model']
        return state

    def __setstate__(self, newstate):
        self.deserialize(newstate['_model_serialized'])


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


class CharTokenizer:

    def segment(self, line):
        line = self.pre_tokenize(line)
        return list(line.strip())

    def detokenize(self, inputs, delimiter=u''):
        return super(CharTokenizer, self).detokenize(inputs, delimiter)



