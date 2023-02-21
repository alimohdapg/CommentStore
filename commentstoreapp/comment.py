class Comment:
    name = ''
    visit_date = ''
    comment_str = ''

    def __init__(self, name, visit_date, comment_str):
        self.name = name
        self.visit_date = visit_date
        self.comment_str = comment_str

    def __str__(self):
        details = ''
        details += f'Name        : {self.name}\n'
        details += f'VisitDate   : {self.visit_date}\n'
        details += f'Comment     : {self.comment_str}\n'
        return details

    
