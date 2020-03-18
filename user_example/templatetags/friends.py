from django import template
from social_django.models import UserSocialAuth
import random
import requests

register = template.Library()


@register.inclusion_tag('user_example/social.html', takes_context=True)
def print_friends(context):
    user_id = context['user'].id
    user = UserSocialAuth.objects.filter(user_id=user_id).first()
    token = user.access_token
    print(token)
    r = requests.get('https://api.vk.com/method/friends.get',
                     params={'fields': 'first_name', 'access_token': token,
                             'offset': 0, 'v': 5.73})

    answer = r.json()
    amount_of_friends = answer['response']['count']
    all_friends = answer['response']['items']
    random_friends = random.sample(range(amount_of_friends), 5)
    friends = [all_friends[i] for i in random_friends]
    return {'token': token, 'friends': friends}
