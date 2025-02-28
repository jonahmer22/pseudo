# Pseudo
Pseudo - A Coding Language (eventually)

Pseudo is a tool designed to convert pseudocode into Python code seamlessly. It leverages the power of Ollama, a language model API, to ensure accurate and efficient conversion while maintaining the original formatting and structure of the pseudocode locally. Additionally, Pseudo includes a built-in code checker to identify and fix syntax errors, logical mistakes, and missing functionality in the generated Python code.

## Features
- **Pseudocode to Python Conversion**: Translates pseudocode into Python code while preserving indentation and spacing.
- **Code Error Checking**: Analyzes the generated Python code for syntax errors, logical mistakes, and missing functionality.
- **Automated Corrections**: Automatically fixes errors and implements missing functionality in the generated code.
- **Cross-Platform Compatibility**: Works on multiple operating systems (Windows, macOS, Linux) with Ollama installed.

## Installation
1. **Install Ollama**: Ensure Ollama is installed on your system. If not, follow the instructions for your operating system:
   - [Windows](https://ollama.com/download)
   - [macOS](https://ollama.com/download)
   - [Linux](https://ollama.com/download)

2. **Install Default Models**
    ```bash
    ollama pull llama3.2
    ollama pull phi4
    ```
    Default models can be changed by modifying the `Initial_Generator` and `Code_Checker` variables.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/jonahmer22/pseudo.git
   cd pseudo
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use Pseudo, run the script with an input file containing pseudocode and specify the output file for the generated Python code.

```bash
python3 interpreter.py <input_filename> <output_filename>
```

### Example

Create a file named `example_in.ps` with the following pseudocode:

Example code 
(please note that it is best practice to include labels, but code will still be generated without them; a slightly more complex version of which is [here](example_code.ps)):
```
BEGIN
    PRINT "Hello, World!"
END
```
or
```
say hello world!
```

Run the script:

```bash
python3 interpreter.py example_in.ps example_out.py
```

The generated Python code will be saved in `example_out.py`:

```python
print("Hello, World!")
```

The script will also check the generated code for errors and apply corrections if necessary.

## Code Checker

The built-in code checker ensures the generated Python code is free of errors and implements any missing functionality. It uses Ollama to analyze and correct the code, providing a robust and reliable output.

## Contributing

Contributions are welcome! If you'd like to contribute to Pseudo, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the GPL 3.0 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Ollama**: For providing the language model used in pseudocode conversion and code checking.
- **Python Community**: For their continuous support and contributions to the Python ecosystem.

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/jonahmer22/pseudo/issues).

Happy coding with Pseudo! 🚀