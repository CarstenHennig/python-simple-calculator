from itertools import islice
from pubsub import *
from pprint import pprint
from typing import NamedTuple, DefaultDict, Optional, List
from collections import namedtuple, deque, defaultdict
import time

User = str
Post = NamedTuple('Post', [('timestamp', float), ('user', str), ('text', str)])
posts = deque()  # type: Deque[Post]                # Posts from newest to oldest
user_posts = defaultdict(deque)  # type: DefaultDict[str, deque]     # create deque
following = defaultdict(set)  # type: Dict[User, Set[User]]
followers = defaultdict(set)  # type: Dict[User, Set[User]]


def post_message(user: str, text: str, timestamp: float = None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    following[user].add(followed_user)
    followers[followed_user].add(user)


def post_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(islice(user_posts[user], limit))


post_message('guido', 'i love #python type hinting')
post_message('davin', 'blablabla')
post_message('davin', 'blablablabla blubb')
post_message('davin', 'blablabla bla bla')
post_message('raymondh', 'bbla bla bla')

follow('davin', 'raymondh')
follow('davin', 'guido')

if __name__ == '__main__':
    pprint(posts)
    pprint(user_posts['raymondh'])
    pprint(following)
    pprint(followers)
    pprint(post_by_user('davin', limit=5))
pprint(len(user_posts['raymondh']))
