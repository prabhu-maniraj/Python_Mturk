from boto.mturk.connection import MTurkConnection,HIT
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import requests;


ACCESS_ID ='AKIAI5H7LRLSIPSC244A'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)


 
title = 'Give your opinion about a website (sqor)'
description = ('Visit a website and give us your opinion about'
               ' the design and also some personal comments')
keywords = 'website, rating, opinions'
 
#ratings =[('Very Bad','-2'),
#         ('Bad','-1'),
#         ('Not bad','0'),
#         ('Good','1'),
#         ('Very Good','1')]
# 
#---------------  BUILD OVERVIEW -------------------
 
overview = Overview()
overview.append_field('Title', 'Give your opinion on this website')
overview.append(FormattedContent('<a target="_blank"'
                                 ' href="https://shop.sqor.com/">'
                                 ' Sqor Sports Shop</a>'))
# 
##---------------  BUILD QUESTION 1 -------------------
# 
#qc1 = QuestionContent()
#qc1.append_field('Title','How looks the design ?')
# 
#fta1 = SelectionAnswer(min=1, max=1,style='dropdown',
#                      selections=ratings,
#                      type='text',
#                      other=False)
# 
#q1 = Question(identifier='design',
#              content=qc1,
#              answer_spec=AnswerSpecification(fta1),
#              is_required=True)
# 
#---------------  BUILD QUESTION 2 -------------------
 
qc2 = QuestionContent()
qc2.append_field('Title','Your personal comments')
 
fta2 = FreeTextAnswer()
 
q2 = Question(identifier="comments",
              content=qc2,
              answer_spec=AnswerSpecification(fta2))
 
#--------------- BUILD THE QUESTION FORM -------------------
 
question_form = QuestionForm()
question_form.append(overview)
#question_form.append(q1)
question_form.append(q2)
 
#--------------- CREATE THE HIT -------------------
 
HIT = mtc.create_hit(questions=question_form,
               max_assignments=1,
               title=title,
               description=description,
               keywords=keywords,
               duration = 60*5,
               reward=0.05)dvz

for hit in HIT:
  print hit.HITId
  print(mtc.get_all_hits())
  print ("https://workersandbox.mturk.com/mturk/preview?groupId="+hit.HITTypeId);



#resp = requests.get('https://rest-stage.sqor.com/feeds/aggregate/sqor?limit=1000&offset=0',verify=False)
#print (resp.text)
#if resp.status_code != 200:
#    # This means something went wrong.
#    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{}'.format(todo_item['id']))
#s=FileUploadURL(mtc);
#print(s);
