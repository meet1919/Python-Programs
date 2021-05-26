posts = [
    {
        'author': 'OG',
        'title': 'search Post 1',
        'content': 'First post content',
        'date_posted': 'May 15, 2021'
    },
    {
        'author': 'Elon Musk',
        'title': 'search Post 2',
        'content': 'Second post content',
        'date_posted': 'May 16, 2021'
    }
]

dict = {'posts': posts}

for post in dict['posts']:
    print(post['title'])