import matplotlib.pyplot as plt
from wordcloud import WordCloud

# WordCloud for Story
story_text = ' '.join(word.lower() for word in df['Story'].dropna())
wordcloud = WordCloud(width=2000, height=800, background_color='white', max_words=320).generate(story_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud for Story')
plt.show()
