from boto.mturk.connection import MTurkConnection,HIT
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import requests;


ACCESS_ID ='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
HOST = 'mechanicalturk.sandbox.amazonaws.com'
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)


 
title = 'Profile of record Athlete Information'
description = ('Provide Information about the Athlete')
keywords = 'website, rating, opinions'
 
height =[('4\'11','4\'11'),('5\'1','5\'1'),('5\'2','5\'2'),('5\'3','5\'3'),('5\'4','5\'4'),('5\'5','5\'5'),('5\'6','5\'6'),('5\'7','5\'7')]
 
#---------------  BUILD OVERVIEW -------------------
 
overview = Overview()
overview.append_field('Title', 'What is the Height if this Athlete?')
overview.append(FormattedContent('<a> target="_blank"'
                                 ' href="https://en.wikipedia.org/wiki/Brett_Favre"'
                                 ' Athlete Information URL</a>'))
# 
##---------------  BUILD QUESTION  -------------------
# 
qc = QuestionContent()
qc.append_field('Title','What is the Height of Brett Favre')
 
fta = SelectionAnswer(min=1, max=1,style='dropdown',
                      selections=height,
                      type='text',
                      other=False)
 
q = Question(identifier='design',
              content=qc,
              answer_spec=AnswerSpecification(fta),
              is_required=True)
 
question_form = QuestionForm()
question_form.append(overview)
question_form.append(q)
 
#--------------- CREATE THE HIT -------------------
 
HIT = mtc.create_hit(questions=question_form,
               max_assignments=1,
               title=title,
               description=description,
               keywords=keywords,
               duration = 60*5,
               reward=0.05)

for hit in HIT:
  print hit.HITId
  print(mtc.get_all_hits())
  print ("https://workersandbox.mturk.com/mturk/preview?groupId="+hit.HITTypeId);


