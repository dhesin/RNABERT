from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers import normalizers
from tokenizers.normalizers import Lowercase, NFD, StripAccents
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import WordLevelTrainer
from tokenizers.processors import TemplateProcessing

bert_tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))

#bert_tokenizer.normalizer = normalizers.Sequence([Lowercase()])
#bert_tokenizer.normalizer = normalizers.Sequence([NFD(), Lowercase(), StripAccents()])
bert_tokenizer.pre_tokenizer = Whitespace()
bert_tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    special_tokens=[("[CLS]", 1), ("[SEP]", 2)],
)
#trainer = WordLevelTrainer(
#    vocab_size=14, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]
#)
trainer = WordLevelTrainer(special_tokens=["[PAD]", "[CLS]", "[SEP]","[UNK]", "[MASK]"])



file_rna = open('RF00002.fa', 'r')
Lines = file_rna.readlines()
file_rna.close()

rna_seqs = []
for line in Lines:
    if line[0] != '>':
        #line = line[:-1]
        rna_str = '122.0,'
        for ch in line:
            if ch not in ['A', 'C', 'T', 'G', 'U', 'N', 'c', 'a', 'g', 't', 'u', 'n']:
                print(ch, "00002 NOT IN VOCAB:", line)
            rna_str = rna_str + ch.lower() + ' '
        #rna_str = rna_str[:-1]
        rna_seqs.append(rna_str)

file_rna = open('RF03064.fa', 'r')
Lines = file_rna.readlines()
file_rna.close()

for line in Lines:
    if line[0] != '>':
        #line = line[:-1]
        rna_str = '123.,'
        for ch in line:
            if ch not in ['A', 'C', 'T', 'G', 'U', 'N', 'c', 'a', 'g', 't', 'u', 'n']:
                print(ch, "03064 NOT IN VOCAB:", line)
            rna_str = rna_str + ch.lower() + ' '
        #rna_str = rna_str[:-1]
        rna_seqs.append(rna_str)

#print(rna_seqs)

file_rna = open('./RF_2_family-finetune.fa.csv', 'w')
file_rna.writelines(rna_seqs)
file_rna.close()

exit()
bert_tokenizer.train_from_iterator(rna_seqs, trainer=trainer)

#files = [f"data/wikitext-103-raw/wiki.{split}.raw" for split in ["test", "train", "valid"]]
#bert_tokenizer.train(files, trainer)
bert_tokenizer.save("./bert-rna-tokenizer-1.json")



