from elasticsearch import Elasticsearch
from getvisibletext import GetVisibleText

es = Elasticsearch([{'host':'localhost','port':9200}])
es.ping()

print("es.ping() : " + str(es.ping()))

url1 = "https://en.wikipedia.org/wiki/Information_retrieval"
text1 = {"url":url1,"visibletext":GetVisibleText(url1)}
url2 = "https://en.wikipedia.org/wiki/Big_data"
text2 = {"url":url2,"visibletext":GetVisibleText(url2)}
url3 = "https://en.wikipedia.org/wiki/Big_Ben"
text3 = {"url":url3,"visibletext":GetVisibleText(url3)}

res = es.index(index='project_ir',doc_type='html',id=1,body=text1)
res = es.index(index='project_ir',doc_type='html',id=2,body=text2)
res = es.index(index='project_ir',doc_type='html',id=3,body=text3)


res = es.get(index='project_ir',doc_type='html',id=1)

print("es.get(..) = " + str(res))

res = es.search(index='project_ir',body={
	'query':{
		'match':{
			"visibletext":"Big Data" 
			}
		}
	}
	)

print("es.search(..match..) = " + str(res))

res = es.search(index='project_ir',body={
	'query':{
		'match_phrase':{
			"visibletext":"Big Data" 
			}
		}
	}
	)


print("es.search(..match phrase..) = " + str(res))

