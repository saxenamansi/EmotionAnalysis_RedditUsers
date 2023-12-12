# EmotionAnalysis_RedditUsers

In today's digital age, online communities like Reddit play a significant role in providing emotional support and a sense of belonging to individuals. Users often express their feelings, emotions, and experiences on different subreddits. Harnessing the valuable data generated within these communities is crucial in creating more effective mental health (or general) support systems. Such systems can provide users with empathetic responses and resources tailored to their emotional needs, ultimately contributing to a more empathetic and supportive online environment.

This (ongoing) project centrally focuses on exploring the relationship between an individual's emotional state and their writing style on a conversational platform like Reddit. It aims to discover whether emotional shifts manifest as discernible changes in the style, such as tone, usage of vocabulary, content, or patterns of their online posts, under the assumption that emotional fluctuations and writing style changes have a connection in online communication. 

This project consists of these steps:

1.  Scraping a pilot dataset from Reddit from random list of users. (5k Reddit posts)
2.  Classifying these posts using Roberta-base model and DistilBERT model trained on GoEmotions dataset.
3.  Performing Topic Modelling Analysis for the posts from each year to analyse the general trends.
4.  Obtaining Word Attribution Results for the Classification Model. (This defines our writing style)
5.  Visualising the Word Attribution Results to understand the connection (via writing style) between different emotions.
6.  Combining the Topic Modeling code with Classification model and Word Attributions to obtain more event-driven fluctuation in emotions, such as during Covid-19, and so on.
7.  Build a User Emotional LifeCycle Markov Model by obtaining probabiliites based on number of occurences of a transition from Emotion A to Emotion B. 
8.  Scrape a larger Reddit Dataset and apply all these techniques to it, to confirm and get better results. (65k Reddit posts)

These are the files in this project:

1. Classifying these posts from the pilot dataset using the Roberta-base model trained on GoEmotions dataset, which has 28 emotions. [Classification Code](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/1_PredictingEmotion.ipynb)
2. Analysing the code using Topic Modelling and Obtaining Word Attributions for the Classification Model [Analysis Code](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/2_UserRedditAnalysis.ipynb) [Topic modeling using POS tagging](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/6_TopicModeling.ipynb)
3. Analysing the Word Attribution results. [Analysis of Word Attributions](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/3_WordAttrs_analysis.ipynb)
3a. Visualising the connection between emotions using Word Attributions. [Emotion Visualisation](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/3a_visualise_emotions.py)
4. Obtaining transitional probabilities by averaging the occurences of a certain transition by the total number of transitions. [Emotional Transition Probabities](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/4_EmotionalProbabilities.ipynb)
4a. Visualising the Emotional Transition Probabilities obtained as a graph (only those above 0.05) [Emotional LifeCycle](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/4a_EmotionLifecycle.py)
5. Scraping the larger 65k posts dataset. [Reddit Scraping](https://github.com/saxenamansi/EmotionAnalysis_RedditUsers/blob/main/5_RedditScraping.ipynb)
6. 
