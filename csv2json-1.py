import pandas
import json
import datetime
import unidecode
import pickle
import re
#from bson import json_util
__author__ = "dr"
__date__ = "08 December 2016"

stop = [line.rstrip('\n') for line in open('stopwords.txt')]
from nltk.stem.porter import *
#oho
stemmer = PorterStemmer()

def csv2json(input_file):
    out_dict = {'setup': []}
    df = pandas.read_excel(input_file,skip_footer=170000)
    qu=[]
    #qu=df.question
    #print qu
    #ans_cols = [x for x in df.columns if x.startswith('answer')]
    i=0
    ans_cols=['Answer 1','Answer 2','Answer 3','Answer 4','Answer 5','Answer 6','Answer 7','Answer 8','Answer 9','Answer 10','Answer 11','Answer 12','Answer 13','Answer 14','Answer 15','Answer 16','Answer 17','Answer 18','Answer 19','Answer 20','Answer 21','Answer 22','Answer 23','Answer 24','Answer 25','Answer 26','Answer 27','Answer 28','Answer 29','Answer 30',]
#['answera','answerb','answerc','answerd','answere','answerf','answerg','answerh','answeri','answerj','answerk','answerl','answerm','answern','answero','answerp','answerq','answerr']
    
  
    for index, row in df.iterrows():
        	for ans_col in ans_cols:
            			if row[ans_col] == row[ans_col]:
					try:	
						row['question']=str(row['question'])
						if len(row['question'].split())>2:
							s1=row['question'].lower().split()
							s1 = [stemmer.stem(word) for word in s1 if word not in stop]
							s1=" ".join(s1)
							row['question']=s1

						 
						row[ans_col]=str(row[ans_col])
						#row['question']=row['question'].append("\n")
						row[ans_col]=re.sub("\[first name\]",'(first name)',row[ans_col])
						row[ans_col]=re.sub("\{first name\}",'(first name)',row[ans_col])
						row[ans_col]=re.sub("\(your country\)",'your country',row[ans_col])
                				out_dict['setup'].append([row['question'], row[ans_col]])
						'''
						else:
							row[ans_col]=str(row[ans_col])
							#row['question']=row['question'].append("\n")
							row[ans_col]=re.sub("\[first name\]",'(first name)',row[ans_col])
							row[ans_col]=re.sub("\{first name\}",'(first name)',row[ans_col])
							row[ans_col]=re.sub("\(your country\)",'your country',row[ans_col])
                					out_dict['setup'].append([row['question'], row[ans_col]])'''
					except:
						print "k"
						pass
						
						
				
					
    return out_dict


#######################################################################################################################
if __name__ == '__main__':
    out_dict = csv2json('Chatbot 2016 All - updated with prior answers - v7-31.1.17.xlsx')
    with open('outputmass.json', 'w') as f:
        f.write(json.dumps(out_dict))
    
    print "Program ran successfully."
