# Python Cline Rules Test Project

This is a Python-based test project to validate the agentic coding rules and templates functionality with Cline.

## Purpose

This project serves as a testing ground to ensure that:
- Cline rules are properly loaded and applied in Python projects
- Confidence assessment framework works correctly
- Development standards are followed for Python code
- Memory bank functionality operates as expected
- Repository analysis generates comprehensive documentation

## Project Structure

```
python-cline-test/
├── .clinerules/          # Cline rules directory
│   ├── agent-rules.xml   # Core agent behavior
│   ├── dev-standards.xml # Development standards
│   ├── analysis.xml      # Analysis framework
│   └── memory-bank.md    # Memory bank guidelines
├── src/                  # Source code
│   ├── __init__.py       # Package initialization
│   └── main.py           # Main module with sample functions
├── tests/                # Test files
│   ├── __init__.py       # Test package initialization
│   └── test_main.py      # Comprehensive unit tests
├── docs/                 # Documentation
├── pyproject.toml        # Python project configuration
└── README.md             # This file
```

## Features

### Source Code (`src/main.py`)
- **Type Hints**: Full type annotations for all functions
- **Error Handling**: Comprehensive input validation and error handling
- **Logging**: Proper logging configuration and usage
- **Documentation**: Detailed docstrings following Python conventions
- **Clean Code**: Follows PEP 8 and best practices

### Test Suite (`tests/test_main.py`)
- **Comprehensive Coverage**: Tests for all functions and edge cases
- **Proper Structure**: Organized test classes and descriptive test names
- **Mocking**: Uses unittest.mock for testing logging behavior
- **Error Testing**: Validates exception handling
- **Integration Tests**: Tests combining multiple functions

### Development Tools
- **pytest**: Modern testing framework with coverage reporting
- **black**: Code formatting
- **flake8**: Linting and style checking
- **mypy**: Static type checking
- **Coverage**: Test coverage reporting

## Setup and Installation

```bash
# Navigate to the project directory
cd python-cline-test

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests with coverage
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_main.py

# Run with coverage report
pytest --cov=src --cov-report=html
```

## Code Quality Tools

```bash
# Format code
black src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/

# Run all quality checks
black src/ tests/ && flake8 src/ tests/ && mypy src/ && pytest
```

## Testing Cline Rules

### Expected Behaviors

When Cline works with this project, it should:

1. **Load Rules**: Automatically read and apply rules from `.clinerules/`
2. **Confidence Assessment**: Use 0-10 scale before making changes
3. **Code Quality**: Generate clean, well-documented Python code
4. **Testing**: Create comprehensive unit tests with proper structure
5. **Error Handling**: Implement defensive programming practices
6. **Type Safety**: Use proper type hints and validation

### Test Commands for Cline

Try these commands to test Cline's behavior:

```
# Memory check
WE CAN DO IT

# Confidence assessment
I want to add a user authentication system. What's your confidence level?

# Code generation
Add a new function to calculate the average of a list of numbers with proper error handling and tests

# Repository analysis
Conduct a comprehensive analysis of this Python project using the repository analysis framework

# Memory bank creation
Create a memory bank for this project following the memory-bank.md guidelines
```

## Sample Functions

The project includes sample functions that demonstrate:

- **hello_world()**: Simple function with logging
- **calculate_sum()**: Function with input validation and error handling
- **get_user_info()**: Function returning structured data with validation

Each function includes:
- Type hints
- Comprehensive docstrings
- Input validation
- Error handling
- Logging
- Corresponding unit tests

## Development Standards Validation

This project validates that Cline follows:

- **PEP 8**: Python style guidelines
- **Type Safety**: Proper use of type hints
- **Error Handling**: Defensive programming practices
- **Testing**: Comprehensive test coverage
- **Documentation**: Clear docstrings and comments
- **Logging**: Appropriate logging levels and messages
- **Code Organization**: Proper module and package structure

## Next Steps

After validating the rules work correctly:

1. **Copy to Real Projects**: Use `.clinerules/` in your actual Python projects
2. **Customize Rules**: Adapt for your specific Python frameworks (Django, FastAPI, etc.)
3. **Team Adoption**: Share setup with your development team
4. **Continuous Improvement**: Update rules based on project learnings

---

This project demonstrates how Cline can be configured to follow enterprise-grade Python development practices through systematic rules and guidelines.
