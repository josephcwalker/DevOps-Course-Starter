class ViewModel:
    def __init__(self, items):
        self._items = items
    
    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        return list(filter(lambda item: item.status == "Not Started", self.items))
    
    @property
    def in_progress_items(self):
        return list(filter(lambda item: item.status == "In Progress", self.items))
    
    @property
    def done_items(self):
        return list(filter(lambda item: item.status == "Done", self.items))
