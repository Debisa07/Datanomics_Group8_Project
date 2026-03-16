
def print_tasks(tasks):
	if not tasks:
		print("No tasks in the list.")
		return
	print("\nCurrent To-Do List:")
	for idx, task in enumerate(tasks, 1):
		status = "Done" if task['completed'] else "Pending"
		print(f"{idx}. {task['desc']} (Priority: {task['priority']}) - {status}")

def add_task(tasks, desc, priority):
	tasks.append({"desc": desc, "priority": priority, "completed": False})
	return tasks

def delete_task(tasks, num):
	if num.isdigit() and 1 <= int(num) <= len(tasks):
		return tasks.pop(int(num) - 1)
	return None

def complete_task(tasks, num):
	if num.isdigit() and 1 <= int(num) <= len(tasks):
		idx = int(num) - 1
		if not tasks[idx]['completed']:
			tasks[idx]['completed'] = True
			return True
	return False
def main():
	tasks = []
	print("Welcome to the To-Do List Manager!")
	while True:
		print("\nChoose an action: add, view, delete, complete, exit")
		action = input("Action: ").strip().lower()
		if action == "add":
			desc = input("Enter task description: ").strip()
			priority = input("Enter priority (high/medium/low): ").strip().lower()
			add_task(tasks, desc, priority)
			print("Task added.")
		elif action == "view":
			print_tasks(tasks)
		elif action == "delete":
			print_tasks(tasks)
			if not tasks:
				continue
			num = input("Enter task number to delete: ").strip()
			removed = delete_task(tasks, num)
			if removed:
				print(f"Removed: {removed['desc']}")
			else:
				print("Invalid task number.")
		elif action == "complete":
			print_tasks(tasks)
			if not tasks:
				continue
			num = input("Enter task number to mark as complete: ").strip()
			if complete_task(tasks, num):
				print(f"Marked as complete: {tasks[int(num)-1]['desc']}")
			else:
				print("Invalid task number or already completed.")
		elif action == "exit":
			break
		else:
			print("Unknown action. Please try again.")

	completed = sum(1 for t in tasks if t['completed'])
	pending = len(tasks) - completed
	print(f"\nSummary: Completed tasks: {completed}, Pending tasks: {pending}")
	print("Goodbye!")

if __name__ == "__main__":
	main()
