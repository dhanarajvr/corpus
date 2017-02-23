import pandas
import json
import datetime
import unidecode
import pickle
import re
#from bson import json_util
__author__ = "dr"
__date__ = "08 December 2016"

#nha
def csv2json(input_file):
    out_dict = {'setup': []}
    df = pandas.read_excel(input_file)#,skip_footer=170158)
    qu=[]
    qu=df.question
    print qu
    #ans_cols = [x for x in df.columns if x.startswith('answer')]
    i=0ndex
    ans_cols=['answera','answerb','answerc','answerd','answere','answerf','answerg','answerh','answeri','answerj','answerk','answerl','answerm','answern','answero','answerp','answerq','answerr']
    
  
    for index, row in df.iterrows():
        	for ans_col in ans_cols:
            			if row[ans_col] == row[ans_col]:
					try:
						row['question']=str(row['question'])
						s=row['question'].split()
						if len(s)>4:
							row[ans_col]=str(row[ans_col])
							#row['question']=row['question'].append("\n")
							row[ans_col]=re.sub("\[first name\]",'(first name)',row[ans_col])
							row[ans_col]=re.sub("\(your country\)",'your country',row[ans_col])
							#x=row['question'].join("\n")
							#out_dict['setup'].append(x, row[ans_col])
							#if qu.count(row['question'])<2:
							#print "it is..", qu.count(row['question'])
                					out_dict['setup'].append([row['question'], row[ans_col]])
						
						
				
					except:
						pass
    return out_dict


#######################################################################################################################
if __name__ == '__main__':
    out_dict = csv2json('chatbot.xlsx')
    with open('output.json', 'w') as f:
        f.write(json.dumps(out_dict))
    
    print "Program ran successfully."
