
def main():
	questions = [
		{"question": "What is the capital of France?", "answer": "paris"},
		{"question": "What is 5 + 7?", "answer": "12"},
		{"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
		{"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
		{"question": "What is the boiling point of water in Celsius?", "answer": "100"},
		{"question": "What is the chemical symbol for gold?", "answer": "au"},
		{"question": "What is the square root of 64?", "answer": "8"},
		{"question": "Who painted the Mona Lisa?", "answer": "da vinci"},
		{"question": "What is the fastest land animal?", "answer": "cheetah"},
		{"question": "What is the largest ocean on Earth?", "answer": "pacific"},
	]

	print("Welcome to the Quiz Game!")
	print("Answer the following questions:")

	score = 0
	user_answers = []

	for idx, q in enumerate(questions, 1):
		user_input = input(f"Q{idx}: {q['question']} ").strip().lower()
		user_answers.append(user_input)
		if user_input == q['answer']:
			score += 1

	print(f"\nYour score: {score}/{len(questions)}")

	# Show correct answers for wrong responses
	for idx, (q, user_input) in enumerate(zip(questions, user_answers), 1):
		if user_input != q['answer']:
			print(f"Q{idx}: {q['question']}")
			print(f"  Your answer: {user_input}")
			print(f"  Correct answer: {q['answer']}")

if __name__ == "__main__":
	main()
