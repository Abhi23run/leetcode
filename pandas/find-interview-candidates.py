data = [[190, 1, 5, 2], [191, 2, 3, 5], [192, 5, 2, 3], [193, 1, 3, 5], [194, 4, 5, 2], [195, 4, 2, 1], [196, 1, 5, 2]]
contests = pd.DataFrame(data, columns=['contest_id', 'gold_medal', 'silver_medal', 'bronze_medal']).astype({'contest_id':'Int64', 'gold_medal':'Int64', 'silver_medal':'Int64', 'bronze_medal':'Int64'})
data = [[1, 'sarah@leetcode.com', 'Sarah'], [2, 'bob@leetcode.com', 'Bob'], [3, 'alice@leetcode.com', 'Alice'], [4, 'hercy@leetcode.com', 'Hercy'], [5, 'quarz@leetcode.com', 'Quarz']]
users = pd.DataFrame(data, columns=['user_id', 'mail', 'name']).astype({'user_id':'Int64', 'mail':'object', 'name':'object'})

## Finding users with 3 or more gold medals
### Method 1 : Using value_conuts and map function to broadcast the results of an aggregation back to the original data, ensuring that the transformed data aligns correctly with the original data.
set(contests[contests['gold_medal'].map(contests['gold_medal'].value_counts()>=3)]['gold_medal'])

### Method 2 : Using groupBy object and Transform - The transform method in Pandas is used to perform group-wise transformations on a DataFrame or Series. When applied to a GroupBy object, it returns an object that is indexed the same way as the original DataFrame or Series, but with the values computed within each group. This is often used when you want to broadcast the results of an aggregation back to the original data, ensuring that the transformed data aligns correctly with the original data.
set(contests[contests.groupby('gold_medal')['gold_medal'].transform('count')>=3]['gold_medal'])

## Finding users with any medal in 3 or more consecutive contests
results = set()
subset_size=3

# Iterate through the DataFrame and process each subset
for i in range(0, len(contests)-3):
    subset = contests.iloc[i:i+subset_size,1:]
    iteration_set=(set([value for value in set(subset.dropna().values.flatten()) if subset.dropna().values.flatten().tolist().count(value)>=3]))
    results=results.union(iteration_set)   
# Print the results
results

## Final Solution - Method 1 

import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    set_consectuive_all_gold=set(contests[contests.groupby('gold_medal')['gold_medal'].transform('count')>=3]['gold_medal'])
    set_consectuive_any=set()
    subset_size=3

    # Iterate through the DataFrame and process each subset
    for i in range(0, len(contests)-2):
        subset = contests.iloc[i:i+subset_size,1:]
        iteration_set=(set([value for value in set(subset.dropna().values.flatten()) if subset.dropna().values.flatten().tolist().count(value)>=3]))
        set_consectuive_any=set_consectuive_any.union(iteration_set)   
    
    final_set=set_consectuive_all_gold.union(set_consectuive_any)

    return users[users['user_id'].isin(final_set)][['name','mail']]


