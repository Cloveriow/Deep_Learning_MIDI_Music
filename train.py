import numpy as np
from utils import csv2seq, CharRNN, train

from tqdm import tqdm
import os, plac


@plac.annotations(
    # Optional
    n_hidden=("隱藏單元數", "option", "nh", int),
    n_layers=("隱藏層數", "option", "nl", int),
    bs=("Batch size", "option", "bs", int),
    seq_len=("輸入序列的長度", "option", "sl", int),
    lr=("學習率", "option", "lr", float),
    d_out=("輟學率", "option", "do", float),
    save_every=("要保存的模型的步驟數", "option", "se", int),
    print_every=("打印訓練信息（loss等）的步數", "option", "pe", int),
    name=("模型的文件夾名稱。 如果找不到該文件夾，它將使用該名稱創建一個新文件夾", "option", "o", str),
    midi_source_folder=("數據的文件夾名稱 它必須具有 Midicsv 格式的 .csv 文件", "option", "i", str),
)
def main(n_hidden=128, n_layers=3, bs=64, seq_len=25, lr=0.001, d_out=0.001, save_every=20000, print_every=500,
         name='model', midi_source_folder = "dataset"):
#def main(n_hidden=64, n_layers=2, bs=128, seq_len=25, lr=0.001, d_out=0.2, save_every=20000, print_every=500,
#         name='model', midi_source_folder = "dataset"):
    # Initialize Folder
    if not os.path.exists(name):
        os.makedirs(name)

    # Initialize Data
    note = {}
    for fname in tqdm(os.listdir(midi_source_folder)):
        if fname not in [".DS_Store", '.ipynb_checkpoints']:
            note = csv2seq(midi_source_folder, fname, note)
    text = " ".join([track for music in note.values() for track in music.values()])

    chars = tuple(set(text))
    int2char = dict(enumerate(chars))
    char2int = {ch: ii for ii, ch in int2char.items()}
    encoded = np.array([char2int[ch] for ch in text])

    # Training
    net = CharRNN(chars, n_hidden, n_layers, drop_prob=d_out)
    print(net)
    train(net, encoded, name, batch_size=bs, seq_length=seq_len, lr=lr, print_every_n_step=print_every, save_every_n_step=save_every)


if __name__ == '__main__':
    plac.call(main)
