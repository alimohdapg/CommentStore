from queue import Queue
from .comment import Comment


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class CommentStore:
    comment_list = Queue()

    def insert_comment(self, name, visit_date, comment_str):
        cmt = Comment(name, visit_date, comment_str)
        self.comment_list.put(cmt)
