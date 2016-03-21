from keys import HEALTHFINDER_API_KEY
import urllib, urllib2
import json
from textstat.textstat import textstat
from textblob import TextBlob

def run_healthfinder_query(search_terms, read_min,
                                         read_max,
                                         pol_min,
                                         pol_max,
                                         sub_min,
                                         sub_max):
    root_url = 'http://healthfinder.gov/developer/'
    search_type = 'Search.json'
    
    query = urllib2.quote(search_terms)

    
    search_url = "{0}{1}?api_key={2}&keyword={3}".format(
        root_url,
        search_type,
        HEALTHFINDER_API_KEY,
        query
    )
    
    results = []
    
    try:
        response = urllib2.urlopen(search_url).read()

        json_response = json.loads(response)
        
        
        for result in json_response["Result"]["Topics"]:
            summary = result["Sections"][0]["Description"]
            blobSummary = TextBlob(summary)
            read = textstat.flesch_reading_ease(summary)
            pola = ("%.2f" % blobSummary.sentiment.polarity)
            subj = ("%.2f" % blobSummary.sentiment.subjectivity)
            if (read_min <= read <= read_max) and (pol_max - pol_min <= pola) and (sub_max - sub_min <= subj):
                results.append({
                    'title':result["Title"],
                    'url':result["AccessibleVersion"],
                    'summary':result["Sections"][0]["Description"],
                    'read':read,
                    'pola':pola,
                    'subj':subj,
                    'source':'HealthFinder'
                    })
    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e
     
    return results
  