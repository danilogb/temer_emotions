import json
import pandas as pd

with open('data.json', 'r') as f:
    data = json.load(f)

results = data['processingResult']

results = eval(results)

emotions = []

for i in range(len(results['fragments'])):
    try:
        for j in range(len(results['fragments'][i]['events'])):
            try:
                if results['fragments'][i]['events'][j][0]['scores'] is not None:
                    emotions.append(results['fragments'][i]['events'][j][0]['scores'])
                else:
                    continue
            except:
                continue
    except:
        continue


categories = emotions[0].keys()
categories.remove('neutral')

master_dict = {}
# initialize the arrays first
for key in emotions[0]:
    master_dict[key] = [d[key] for d in emotions]

# Exports dictionary to .csv file to be used in R
df = pd.DataFrame.from_dict(master_dict, orient='columns')
pd.DataFrame.to_csv(df, path_or_buf='temer_emotions.csv', index=False)

# Plots a bar chart with the averages of each category
exclude = ['neutral']
ax = df.ix[:, df.columns.difference(exclude)].mean().plot(kind='bar', title='Average emotions', x='Emotion', y='Intensity')
ax.set_xlabel("Emotion")
ax.set_ylabel("Intensity")
