import datetime

from django.shortcuts import render
from django.db import models
from .models import Post


posts = [
    {
        'author': 'BenjiM',
        'title': 'Advances of Explainable AI',
        'content': 'Artificial intelligence (AI) can be defined as the science of creating machines (or programs) '
                   'that perform many tasks that would usually require human intelligence. The term covers a wide '
                   'span of different applications, from simple image analysis programs to sophisticated '
                   'cybersecurity programs. AI typically perceives data sets and ‘learns’ certain patterns and '
                   'trends, and then acts in accordance with its existing rule set and what it has learnt. '
                   'Explainable AI is, as defined by IBM, a collection of ‘processes and methods that allows human '
                   'users to comprehend and trust the results and output created’. It is, in effect, artificial '
                   'intelligence that’s results can be understood and confirmed by humans. Explainable AIs goal is '
                   '‘adding transparency to ML (machine learning) models’ by providing comprehensive information '
                   'detailing how the program reached the decision it did. This allows humans to clearly view and '
                   'dissect the decisions that the program made, and consequently why it reached its decision. ',
        'date_posted':  datetime.datetime(2022, 6, 10, 7, 0)
    },
    {
        'author': 'WillS',
        'title': 'The Importance of Punctuality',
        'content': 'Punctuality is incredibly important. As a university student I often find it hard to make it to '
                   'all my lectures on time. Here are 5 steps to help you be punctual: 1 - Set alarms, 2 - Wake up '
                   'early, 3 - Go to bed early, 4 - Eat three meals a day, 5 - Catch up on missed lectures.',
        'date_posted':  datetime.datetime(2022, 6, 9, 13, 30)
    }

]


def home(request):
    context = {
        #  'posts': Post.objects.all()
        # Would usually be 'Post.objects.all()' but I wanted to include the hardcoded blogs
        'posts': list(Post.objects.all()) + posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
