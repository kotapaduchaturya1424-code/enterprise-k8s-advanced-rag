from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance
from datasets import Dataset

def run_evaluation():
    data = {
        'question': ['Why did my pod get OOMKilled?'],
        'contexts': [['Pod OOMKilled error occurs when container memory limit is exceeded.']],
        'answer': ['The pod was killed because it ran out of allocated memory limit.'],
    }
    dataset = Dataset.from_dict(data)
    results = evaluate(dataset, metrics=[faithfulness, answer_relevance])
    print("Ragas Evaluation Results:", results)

if __name__ == "__main__":
    run_evaluation()