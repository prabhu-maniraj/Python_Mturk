from boto.mturk.connection import MTurkConnection,HIT
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import requests;

resp = requests.get('https://mb7a42tvij.execute-api.us-east-1.amazonaws.com/prod/allprofiles?limit=100',headers={'x-api-key':'ihkjhjkh'})


print(resp.json())


#if (resp.status_code != 200):
#    # This means something went wrong.
#    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{}'.format(todo_item['id']))
#s=FileUploadURL(mtc);

