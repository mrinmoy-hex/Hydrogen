from src.interpreter import run

def main():
    while True:
        try:
            text = input("BASIC ~> ")
            if text.lower() in ['exit', 'quit']:
                print("Exiting the interpreter.")
                break
            
            result, error = run(text)
            if error:
                print(error.__str__())
            else:
                print(result)  # Print the tokens or evaluation result
            
        except Exception as e:
            """Error with the input stream"""
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
