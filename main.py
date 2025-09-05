def add_numbers(num1, num2):
	# TODO: 足し算を実装
	return None

def multiply_numbers(num1, num2):
	# TODO: 掛け算を実装
	return None

def subtract_numbers(num1, num2):
	# TODO: 引き算を実装
	return None

def divide_numbers(num1, num2):
	# TODO: 割り算を実装
	if num2 == 0:
		raise ZeroDivisionError("0で割ることはできません。")
	return None

def check_choice(choice):
	if choice not in ['1', '2', '3', '4']:
		raise ValueError("無効な選択です。1から4の数字を選んでください。")

def calcuate(choice, num1, num2):
	if choice == '1':
		result = add_numbers(num1, num2)
		print(f"{num1} + {num2} = {result}")
	elif choice == '2':
		result = multiply_numbers(num1, num2)
		print(f"{num1} * {num2} = {result}")
	elif choice == '3':
		result = subtract_numbers(num1, num2)
		print(f"{num1} - {num2} = {result}")
	elif choice == '4':
		result = divide_numbers(num1, num2)
		print(f"{num1} / {num2} = {result}")

def main():
	print("二つの数の計算ができます！")
	print("1. 足し算")
	print("2. 掛け算")
	print("3. 引き算")
	print("4. 割り算")
	try:
		choice = input("選択してください (1/2/3/4): ")
		check_choice(choice)
		num1 = float(input("最初の数字を入力してください: "))
		num2 = float(input("次の数字を入力してください: "))
		calcuate(choice, num1, num2)
	except ValueError as e:
		print(f"エラー: {type(e).__name__}\nエラーメッセージ: {e}")
	except ZeroDivisionError as e:
		print(f"エラー: {type(e).__name__}\nエラーメッセージ: {e}")

if __name__ == "__main__":
	main()
	