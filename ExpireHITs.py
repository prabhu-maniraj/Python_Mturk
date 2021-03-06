from boto.mturk.connection import MTurkConnection
import xmltodict, json, pdb
 
ACCESS_ID ='your access id'
SECRET_KEY = 'your key'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
 
def get_all_reviewable_hits(mtc):
    page_size = 50
    hits = mtc.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/page_size
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn = pn + 1
        print "Request hits page %i" % pn
        temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
    return hits
 
mtc = MTurkConnection(aws_access_key_id='SSSSSSSSSSSSSSSSSSSSSS',
                      aws_secret_access_key='Vkkkkkkkkkkkkkkkkkkkkkkkkkkk',
                      host='mechanicalturk.sandbox.amazonaws.com')
 
 
hits = get_all_reviewable_hits(mtc)


#expire a HIT
for hit in hits:
    print (hit)
    mtc.disable_hit(hit, response_groups=None)
else:
    print ("Successfully Expired all the reviewable HITs")

