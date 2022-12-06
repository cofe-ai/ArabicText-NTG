# ArabicText-NTG

## Introduction

In order to evaluate the generation ability of pretrained models, We published a large-scale, multi-topic Arabic news title generation dataset: **ArabicText-NTG**. It contains over 1M samples of Arabic news with their titles, which is the largest in the Arab world. The titles and contents have been strictly cleaned and manually filtered as insurance of high quality. Furthermore, we provide baseline results and evaluation scripts for a fair comparison. Feel free to download the dataset at [BAAIData](https://data.baai.ac.cn/details/ArabicText-NTG).

## Dataset Statistics

| Split     | # Docs  | Avg content len (token/char) | Avg title len (token/char) |
| --------- | ------- | ---------------------------- | -------------------------- |
| **TRAIN** | 836.3K  | 260.7/1314.0                 | 9.26/48.7                  |
| **VALID** | 104.5K  | 259.0/1306.1                 | 9.24/48.6                  |
| **TEST**  | 104.5K  | 258.2/1303.7                 | 9.28/48.8                  |
| **Total** | 1045.5K | 260.2/1312.2                 | 9.26/48.7                  |

## Getting Started

### Requirements

```bash
# to calculate the bleu score
pip install scarebleu
# to calculate rouge_score correctly, you need to install a patched version of rouge_score, which fix bugs in Arabic
pip install git+https://github.com/ARBML/rouge_score_ar
```

### Usage

run `scripts/eval.sh` to get evaluation results.

## Baselines

on the way...
