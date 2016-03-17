import urllib, urllib2
import xmltodict
import re
from textstat.textstat import textstat
from textblob import TextBlob

## pip install xmltodict

def run_medline_query(search_terms):
    root_url = 'https://wsearch.nlm.nih.gov/ws/query'
    source = 'healthTopics'
    
    query = urllib.quote(search_terms)
    query = query.replace('%2B','+')
    query = query.replace('%27','%22')
    
    search_url = "{0}?db={1}&term={2}&rettype=brief".format(
        root_url,
        source,
        query)
       
    results = []
       
    try:
        response = urllib2.urlopen(search_url).read()
        response = xmltodict.parse(response)
        
        for result in response['nlmSearchResult']['list']['document']:
            summary = re.sub('\<.*?>','', result['content'][-1]['#text'])
            blobSummary = TextBlob(summary)
            results.append({
                'title':re.sub('\<.*?\>','', result['content'][0]['#text']),
                'url':result['@url'],
                'summary':re.sub('\<.*?\>','', result['content'][-1]['#text']),
                'read':textstat.flesch_reading_ease(summary),
                'pola':("%.2f" % blobSummary.sentiment.polarity),
                'subj':("%.2f" % blobSummary.sentiment.subjectivity),
                'source':'MedLine'
                })
            

    except urllib2.URLError as e:
        print "Error when querying the MedLine API: ", e
        
    return results
    