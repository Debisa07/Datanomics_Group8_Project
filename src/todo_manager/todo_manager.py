
def print_tasks(tasks):
	if not tasks:
		print("No tasks in the list.")
		return
	print("\nCurrent To-Do List:")
	for idx, task in enumerate(tasks, 1):
		status = "Done" if task['completed'] else "Pending"
		print(f"{idx}. {task['desc']} (Priority: {task['priority']}) - {status}")

def main():
	tasks = []
	completed_count = 0
	print("Welcome to the To-Do List Manager!")
	while True:
		print("\nChoose an action: add, view, delete, complete, exit")
		action = input("Action: ").strip().lower()
		if action == "add":
			desc = input("Enter task description: ").strip()
			priority = input("Enter priority (high/medium/low): ").strip().lower()
			tasks.append({"desc": desc, "priority": priority, "completed": False})
			print("Task added.")
		elif action == "view":
			print_tasks(tasks)
		elif action == "delete":
			print_tasks(tasks)
			if not tasks:
				continue
			num = input("Enter task number to delete: ").strip()
			if num.isdigit() and 1 <= int(num) <= len(tasks):
				removed = tasks.pop(int(num) - 1)
				print(f"Removed: {removed['desc']}")
			else:
				print("Invalid task number.")
		elif action == "complete":
			print_tasks(tasks)
			if not tasks:
				continue
			num = input("Enter task number to mark as complete: ").strip()
			if num.isdigit() and 1 <= int(num) <= len(tasks):
				idx = int(num) - 1
				if not tasks[idx]['completed']:
					tasks[idx]['completed'] = True
					print(f"Marked as complete: {tasks[idx]['desc']}")
				else:
					print("Task already completed.")
			else:
				print("Invalid task number.")
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
