import httpx
import os
import googletrans as gt
import pandas as pd
import progressbar 
import wordcloud as wc
from matplotlib import pyplot as plt



def translateAndCopyTweets():
    
    # Get the list of tweets's users
    list_files = os.listdir("./pickle/tweets/")

    # Set timeout to translate 
    timeout = httpx.Timeout(5) # 5 seconds timeout

    # Get the translator object
    translator = gt.Translator(timeout=timeout)

    for i in len(list_files):

        # Get i file which contains the tweets
        objs = pd.read_pickle('./pickle/tweets/' + list_files[i])

        # Create the progress bar
        bar = progressbar.ProgressBar(maxval=len(objs), \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

        # Start the bar
        bar.start()
        
        j = 0

        # Open the file where will put in the translated tweet
        f = open("tweets_translated.txt", "a")

        for obj in objs:
            old_text = str(obj['full_text'])
            # Google translate bores points without spaces ---> referr "https://github.com/ssut/py-googletrans/issues/267"
            text = old_text.replace('.', '. ')

            try:
                translated = translator.translate(text)
            except Exception:
                continue
            
            f.write(translated.text)
            bar.update(j+1)
            j = j + 1

        bar.finish()
    
    f.close()


def showWordCloud():


    f = open("tweets_translated.txt", "r")
    text = f.read()

    # Create and generate a word cloud image:
    wordcloud = wc.WordCloud().generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()












            
