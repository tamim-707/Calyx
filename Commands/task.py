from Memory.storage import Memory


class TaskManager:
    def __init__(self, memory):
        self.memory = memory
#adding task           
    def add_task(self, task_text):
        if not task_text.strip():
            return "Please write a task"

        data = self.memory.load()

        task = {
            "task": task_text,
            "done": False
        }

        data["tasks"].append(task)
        self.memory.save(data)

        return f"Task added: {task_text}"
#Showing tasks
    def show_tasks(self):
        data = self.memory.load()
        tasks = data["tasks"]

        if not tasks:
            return "No tasks found."

        result = "Tasks:\n"

        for i, task in enumerate(tasks, start=1):
            status = "[DONE]" if task["done"] else "[TODO]"
            result += f"{i}. {task['task']} {status}\n"

        return result
#Mark symbol    
    def mark_done(self, task_number):
        data = self.memory.load()
        tasks = data["tasks"]

        task_number -= 1

        if task_number < 0 or task_number >= len(tasks):
            return "Task not found."

        tasks[task_number]["done"] = True
        self.memory.save(data)

        return "Task marked as done."
 #deleteing task   
    def delete_task(self, task_number):
        data = self.memory.load()
        tasks = data["tasks"]

        task_number -= 1

        if task_number < 0 or task_number >= len(tasks):
            return "Task not found."

        deleted = tasks.pop(task_number)
        self.memory.save(data)

        return f"Deleted task: {deleted['task']}"