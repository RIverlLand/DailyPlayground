# Explain video from ThreeBlueOneBrown, how words gets turned into tensor
# Based on gensim package
# Similar to NLP video saw on Bilibili
# Run venv before using script, refer to Readme for more

import gensim.downloader
model = gensim.downloader.load('glove-wiki-gigaword-50') # Needs to connect to google I guess
print(model["tower"])
