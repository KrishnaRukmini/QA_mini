import re
import spacy
spacy.load('en_core_web_sm')
from spacy.lang.en import English

def create_clean_df(dataframe):
  count = 0

  for article_txt in dataframe.text:
    print(count)
    if not article_txt == None :
      article_txt = re.sub(r"&nbsp","",article_txt)
      article_txt = re.sub(r"http\S+","",article_txt)   
      article_txt = re.sub(r"Category:.*","",article_txt)
      article_txt = re.sub(r"References*","",article_txt)
      article_txt = re.sub(r"Extrenal Link*","",article_txt)
      article_txt = re.sub(r"See also*","",article_txt)
      article_txt = re.sub(r"\n"," ",article_txt)  
      article_txt = re.sub(r"\!|\#|\$|\%|\&|\(|\)|\*|\+|\-|\/|\:|\;|\<|\=|\>|\@|\[|\\|\]|\^|\_|\`|\{|\||\}|\~"," ",article_txt)
      article_txt = re.sub(r" +"," ",article_txt)
      article_txt = article_txt.replace(u'\xa0', u' ')
      if len(article_txt) > 0:
        convert_non_unicode = [convert_non_ascii(article_txt)] # converting non-unicode characters to their unicode equivalent
        article_txt = ' '.join(convert_non_unicode)
    dataframe['text'][count] = article_txt
    count += 1
  return dataframe
