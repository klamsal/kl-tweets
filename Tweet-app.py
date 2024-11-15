import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tweets = pd.read_csv('Tweets.csv')

# Streamlit app layout and title
st.title('Twitter Sentiment Analysis Dashboard')

# Display a brief description
st.markdown("""
This dashboard displays insights from a dataset of tweets regarding airlines. 
It includes visualizations of tweet sentiment and tweet counts by airline.
""")

# --- Sentiment Pie Chart ---
st.header('Sentiment Distribution of Tweets')

# Calculate value counts and reset index to create a 'count' column
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']  # Rename columns for clarity

# Create a pie chart using Plotly
fig_sentiment = px.pie(sentiment_counts,
                       values='count',  # Use the 'count' column for values
                       names='sentiment',  # Use the 'sentiment' column for names
                       title='Count of Tweets by Sentiment')

# Display the pie chart
st.plotly_chart(fig_sentiment)

# --- Airline Tweet Counts Bar Chart ---
st.header('Tweet Counts by Airline')

# Calculate tweet counts by airline
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['Airline', 'Tweet Count']

# Create the bar plot using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airline', y='Tweet Count', hue='Airline', data=airline_counts, palette='pastel', legend=False)

# Add titles and labels
plt.title('Tweet Counts by Airline')
plt.xlabel('Airline')
plt.ylabel('Tweet Count')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
st.pyplot(plt)

# You can also add more interactivity or options as needed
