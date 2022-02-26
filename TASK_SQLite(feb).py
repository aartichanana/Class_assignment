#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import sqlite3, csv, logging module files
import sqlite3,csv
import logging as lg
lg.basicConfig(filename = "C:\\Users\MR\\PYTHON\\iNeuronLive\\log_files\\Task_sql.log", level = lg.INFO, format = '%(asctime)s %(levelname)s %(message)s')


#connecting SQLite3 with pyhton
con = sqlite3.connect("sq1.db")
c = con.cursor()
lg.info("Successfully Connected to SQLite3")
    

    
#Inserting data of file vocab.enron.txt
def insert_data(filename):
    '''Inserting data of file vocab.enron.txt'''
    try:
        lg.info("creating first table")
        c.execute("Create table if not exists sq_table1(col1 text)")
        with open(filename,'r',encoding ='utf-8') as f:
            data = csv.reader(f)
            sq_table1 = (f"insert into sq_table1 values(?)")
            c.executemany(sq_table1, data)
        con.commit()
        lg.info("Record inserted successfully into sq_table1")
        
    
    except Exception as e:
        print(e)

    finally:
        con.close()
        lg.info("Connection closed")


#calling insert_data function to insert data for particular file
insert_data('vocab.nips.txt')


#vocab.enron.txt
#vocab.kos.txt
#vocab.nips.txt
#vocab.nytimes.txt
#vocab.pubmed.txt


# In[2]:


#Importing squmod module contaning function which applied on insert above data
import squmod

#It print same words with their total count
squmod.word_count()


# In[3]:


import squmod


#It print same starting word with their total count
squmod.seq_word_count()


# In[4]:


import squmod

#It remove all the punction marks and print the words without punctuation marks
squmod.remove_punc()


# In[5]:


import squmod

#it zipped all the five files into single one
squmod.zip_allfiles()


# In[ ]:





# In[ ]:




