# Import Statements
import sys
import shutil
import subprocess
import platform
import ollama

# Constants
Initial_Generator = "llama3.2"
Code_Checker = "phi4"

# Utility Functions
def remove_text_between_backticks(input_string):
    """Removes text between backticks."""
    first_backtick_pos = input_string.find("```")
    second_backtick_pos = input_string.find("```", first_backtick_pos + 3)
    if first_backtick_pos != -1 and second_backtick_pos != -1:
        return input_string[first_backtick_pos + 9 : second_backtick_pos]
    return input_string

def install_ollama():
    """Checks if Ollama is installed, otherwise asks user to install."""
    if shutil.which("ollama"):
        return True
    os_type = platform.system()
    print(f"Please install Ollama manually for {os_type}.")
    return False

# Ollama Interaction Functions
def ask_ollama(pseudo_code: str) -> str:
    """Asks Ollama to convert pseudocode to Python."""
    prompt = (
        "You are a strict code converter that translates pseudocode into Python code. "
        "Your output must preserve all indentation and spacing exactly as in the input. "
        "Do NOT provide explanations or ask questions. "
        "ONLY return the converted Python code with exact formatting in plain text. "
        "If the input is empty, return a single newline character."
        "\nHere is the block of pseudocode to convert:\n" + pseudo_code
    )
    try:
        response = ollama.chat(
            model=Initial_Generator,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error occurred: {e}"

def check_for_errors(python_code: str) -> str:
    """Asks Ollama to check Python code for errors."""
    prompt = (
        "You are a strict code checker. "
        "Analyze the given Python code for syntax errors, logical mistakes, missing functionality, or formatting issues. "
        "YOU ARE WRITING OVER THE GIVEN FILE please insert corrections where needed, if none are needed return the original program."
        "If there is any missing functionality please implement it. "
        "Do NOT provide explanations or ask questions. "
        "RESPOND IN PLAIN TEXT WITHOUT ANY FORMATTING. "
        "\nHere is the Python code to check:\n" + python_code
    )
    print("Now performing code check... this may take a while.")
    try:
        response = ollama.chat(
            model=Code_Checker,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error occurred: {e}"

# File Handling Functions
def read_file(filename: str) -> str:
    """Reads the content of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def write_output(output_path: str, text: str) -> None:
    """Writes the output to a file."""
    with open(output_path, "w") as f:
        f.write(text)

# Main Execution
def main():
    """Main function that orchestrates the process."""
    if not install_ollama():
        sys.exit(1)
    
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_filename> <output_filename>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    # Process pseudocode to Python code
    pseudo_code = read_file(input_filename)
    python_code = ask_ollama(pseudo_code)
    write_output(output_filename, python_code)
    
    print("Conversion complete. Output saved to", output_filename)
    
    # Check for errors and apply corrections
    error_check_result = check_for_errors(python_code)
    print("\nError Check Result:\n", error_check_result)
    
    final = remove_text_between_backticks(error_check_result)
    write_output(output_filename, final)

# Entry Point
if __name__ == "__main__":
    main()
