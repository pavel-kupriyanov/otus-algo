from .factor import FactorArray


class PriorityQueue:

    def __init__(self):
        self.priority_list: list[int] = []
        self.queues: list[FactorArray] = []

    def enqueue(self, priority: int, item):
        queue, insert_index = None, len(self.priority_list)
        for i, index_priority in enumerate(self.priority_list):
            if priority == index_priority:
                queue = self.queues[i]

            if priority > index_priority:
                insert_index = i
                break

        if not queue:
            queue = FactorArray()
            self.priority_list.insert(insert_index, priority)
            self.queues.insert(insert_index, queue)

        queue.append(item)

    def dequeue(self):
        queue = self.queues[0]
        item = queue.remove(0)

        if queue.size == 0:
            self.priority_list.pop(0)
            self.queues.pop(0)

        return item
