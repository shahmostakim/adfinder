import nltk 

try:
    nltk.download('stopwords')
    nltk.download('punkt') 
    print('============ nltk libraries downloaded successfully! =============')
except: 
    print('Problem occured. Stopwords and punkt download was unsuccessful')