import logging
# Configure logging
logging. basicConfig(
filename=®application.log, level=logging. DEBUG,
format="%(asctime)s - %(levelname)s - %(message)s"
# Start of program
logging. info(" Application started.")
def divide_numbers(a, b):
logging.debug(f'divide_numbers() called with a={a}, b={b}")
try:
logging.debug(" Attempting division.")
result = a / b
logging.info(f"Division successful: {a} / {b} = {result} ")
return result
except ZeroDivisionError:
logging.exception("Error: Division by zero.")
return None
except Exception as e:
logging.exception(f"Unexpected error: {e}")
return None

# Main program
logging. debug(" Entering main program.*)
try:
num1 = int(input(" Enter first number: "))
num2 = int(input(* Enter second number: "))
logging. info(f"User entered: {num1}, {num2})
result = divide_numbers(num1, num2)
if result is not None:
print("Result:", result)
logging.info("Result displayed successfully.")
else:
print("Operation could not be completed.")
logging. warning("No result was generated.*)
except ValueError:
print("Invalid input! Please enter numbers only.")
logging.exception("Invalid input received from user.")
except Exception as e:
print(" An unexpected error occurred.")
logging.exception(f"Unexpected application error: {e}")
logging. info(" Application ended.")
