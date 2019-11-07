import numpy as np
import torch
from torch.utils.data import Dataset


class RandomDataset(Dataset):
    def __init__(self, size: int, target: int = 5):
        self.size = size
        self.target = target

        self.x = np.random.randn(self.size, 10)
        self.y = np.random.randint(0, self.target, self.size)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        return torch.FloatTensor(self.x[idx]), torch.LongTensor([self.y[idx]])
    
    def suffle(self):
        self.x = np.random.randn(self.size, 10)
        self.y = np.random.randint(0, self.target, self.size)

        print('[+] Shuffled!', flush=True)
