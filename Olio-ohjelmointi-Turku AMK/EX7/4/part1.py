class WorkItem:
    _id_counter = 1
    
    def __init__(self, description, assignee, hours_required):
        self._id = WorkItem._id_counter
        WorkItem._id_counter += 1
        self._description = description
        self._assignee = assignee
        self._hours_required = hours_required
        self._completed = False
    
    @property
    def id(self):
        return self._id
    
    @property
    def description(self):
        return self._description
    
    @property
    def assignee(self):
        return self._assignee
    
    @property
    def hours_required(self):
        return self._hours_required
    
    def is_completed(self):
        return self._completed
    
    def mark_completed(self):
        self._completed = True
    
    def __str__(self):
        status = "COMPLETED" if self._completed else "NOT COMPLETED"
        return f"{self._id}: {self._description} ({self._hours_required} hours), assigned to {self._assignee} {status}"

class WorkLog:
    def __init__(self):
        self._items = []
    
    def add_item(self, description, assignee, hours_required):
        item = WorkItem(description, assignee, hours_required)
        self._items.append(item)
    
    def all_items(self):
        return self._items
    
    def assignee_items(self, assignee):
        return [item for item in self._items if item.assignee == assignee]
    
    def mark_completed(self, item_id):
        for item in self._items:
            if item.id == item_id:
                item.mark_completed()
                return True
        return False
    
    def incomplete_items(self):
        return [item for item in self._items if not item.is_completed()]
    
    def completed_items(self):
        return [item for item in self._items if item.is_completed()]

# Example usage
work_log = WorkLog()
work_log.add_item("program hello world", "Eric", 3)
work_log.add_item("program webstore", "Adele", 10)
work_log.add_item("program mobile app for workload tracking", "Eric", 25)

for item in work_log.all_items():
    print(item)

work_log.mark_completed(1)
print("\nCompleted items:")
for item in work_log.completed_items():
    print(item)

print("\nIncomplete items:")
for item in work_log.incomplete_items():
    print(item)
