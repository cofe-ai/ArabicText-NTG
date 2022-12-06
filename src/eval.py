# -*- coding:UTF-8 -*-
import json
from rouge_score import rouge_scorer, scoring
import sacrebleu
import os
from arguments import get_args

class Dataset:
    def __init__(self, path, data_type="jsonl"):
        self.path = path
        self.data_type = data_type
        self.data = self.gather_data()

    @staticmethod
    def read_line(path):
        with open(path, "r", encoding="utf8") as fr:
            for line in fr:
                line = line.strip()
                if not line:
                    continue
                yield line
    
    def gather_data(self):
        data = dict()
        assert os.path.exists(self.path)
        for line in self.read_line(self.path):
            if self.data_type == "jsonl":
                data_i = json.loads(line)
                uuid = data_i.get("uuid")
                title = data_i.get("title")
                data[uuid] = title
            else:
                raise NotImplementedError
        return data

class TextGenerationEvaluator:
    def __init__(self, metrics: list):
        self.metrics = metrics

    def _evaluate_by_metric(self, metric_type, total_golds, total_preds):
        metric_dict = dict()
        if metric_type == "rouge":
            rouge_types = ["rouge1", "rouge2", "rougeL"]
            scorer = rouge_scorer.RougeScorer(rouge_types=rouge_types, use_stemmer=True)
            aggregator = scoring.BootstrapAggregator()
            for ref, pred in zip(total_golds, total_preds):
                score = scorer.score(ref, pred)
                aggregator.add_scores(score)
            result = aggregator.aggregate()
            metric_dict.update({key: value.mid.fmeasure * 100 for key, value in result.items()})
        
        elif metric_type == "bleu":
            bleu_results = sacrebleu.corpus_bleu(total_golds, [total_preds])
            bleu_score = bleu_results.score
            metric_dict.update({"bleu": bleu_score})
        else:
            raise NotImplementedError
        return metric_dict

    def eval(self, golds, preds):
        metrics = dict()
        for metric in self.metrics:
            result = self._evaluate_by_metric(metric, total_golds=golds, total_preds=preds)
            metrics.update(result)
        return metrics



def main():
    args = get_args()
    pred_path = args.pred
    gold_path = args.gold
    pred_data = Dataset(pred_path, data_type="jsonl")
    gold_data = Dataset(gold_path, data_type="jsonl")
    preds = []
    golds = []
    for uuid in gold_data.data.keys():
        preds.append(pred_data.data[uuid])
        golds.append(gold_data.data[uuid])
    evaluator = TextGenerationEvaluator(args.metrics)
    metrics = evaluator.eval(golds=golds, preds=preds)   
    for k, v in metrics.items():
        print(f"{k}: {v}") 

if __name__ == "__main__":
    main()