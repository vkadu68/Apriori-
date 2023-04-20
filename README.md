# Apriori Algorithm for Frequent Itemset Mining

This is an implementation of the Apriori algorithm in Python. The algorithm is used for frequent itemset mining and association rule learning in data mining and machine learning.

## Installation

To use this implementation of the Apriori algorithm, you'll need to install Python.

## Usage

To use the Apriori algorithm, simply import the `apriori` module and call the `apriori()` function with the following parameters:

```
apriori(data, min_support=0.5, max_itemset_size=None)
```

Where `data` is a list of transactions, `min_support` is the minimum support threshold (default: 0.5), and `max_itemset_size` is the maximum size of itemsets to consider (default: None).

The `apriori()` function returns a list of frequent itemsets and their corresponding support values.

For example:

```python
from apriori import apriori

data = [['item1', 'item2', 'item3'], ['item1', 'item3'], ['item2', 'item3', 'item4']]

min_support = 0.5
max_itemset_size = None

result = apriori(data, min_support, max_itemset_size)

print(result)
```

This will run the Apriori algorithm on the `data` list with a minimum support of 0.5 and output the results to the console.

## Algorithm

The Apriori algorithm works by iteratively scanning the dataset to identify frequent itemsets, and using these itemsets to generate larger itemsets. Specifically, the algorithm uses a threshold called the minimum support to determine which itemsets are frequent. The minimum support is a user-defined parameter that specifies the minimum frequency threshold for an itemset to be considered frequent.

The algorithm consists of the following steps:

1. Generate a list of candidate 1-itemsets.
2. Scan the dataset to count the support of each candidate 1-itemset.
3. Discard infrequent 1-itemsets.
4. Generate a list of candidate 2-itemsets by joining frequent 1-itemsets.
5. Scan the dataset to count the support of each candidate 2-itemset.
6. Discard infrequent 2-itemsets.
7. Repeat steps 4-6 to generate candidate itemsets of increasing size until no more frequent itemsets can be found.

The Apriori algorithm is computationally expensive for large datasets, as it requires multiple passes through the data and generates a large number of candidate itemsets. However, it is still widely used in practice and has been extended and optimized in various ways over the years.

## Thresholds

The Apriori algorithm uses two thresholds to determine which itemsets are frequent: the minimum support and the maximum itemset size.

The minimum support is a user-defined parameter that specifies the minimum frequency threshold for an itemset to be considered frequent. The higher the minimum support, the more restrictive the algorithm is in identifying frequent itemsets.

The maximum itemset size is also a user-defined parameter that limits the size of itemsets to consider. This is useful for reducing the number of candidate itemsets generated by the algorithm and improving performance.

## License

This implementation of the Apriori algorithm is released under the MIT License.
