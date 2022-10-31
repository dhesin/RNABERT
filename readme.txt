rna_tokenizer.py: creates tokenizer .json file for pretraining or .csv file with labels for sequences for fine-tuning. Need to make changes in the code to switch between too. Need to be maintained well and/or modified to handle more data, e.g. secondary structure. Makeshift code to experiment with code.

bert-rna-model.json: Find an online example for Bert configuration and modified it. Reduced number of layers and vocabulary size. Added num_labels

bert-rna-tokenizer-1.json: Output of run_tokenizer.py.

RF00002.fa and RF03064.fa: Randomly downloaded sequences from 2 families. rna_tokenizer reads these files to create tokenizer and .json and .csv files

RF_2_family-finetune.fa.csv: Output of run_tokenizer.py for finetuning. It includes labels and text columns. Labels: Family Text: Sequence

run_mlm.py: masked language model pretraining. Modified to pretrain from scratch, read sequence data. Default values are updated for our purpose.

run_cls.py: This file is from Sequence Classification task example (run_glue.py)  at HF. Copied and modified for our purpose. It reads RF_2_family-finetune.fa.csv and trains with labels.



conda create -n CS230 python=3.10
pip install -r requirements.txt
python run_mlm.py --output_dir ./out_mlm
python run_cls.py --output_dir ./out_cls model_name_or_path ./out_mlm
