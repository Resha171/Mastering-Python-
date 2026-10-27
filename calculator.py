#!/usr/bin/env python3
"""
Advanced Calculator Application
A feature-rich calculator supporting basic arithmetic, scientific functions,
memory operations, history tracking, and a user-friendly CLI interface.
"""

import math
import json
import os
from datetime import datetime
from typing import Optional, List, Dict


class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


class Calculator:
    """A comprehensive calculator with all standard calculator features."""

    # Memory register
    _memory: float = 0.0
    # Calculation history
    _history: List[Dict] = []
    # Last result
    _last_result: Optional[float] = None

    # ===== Basic Arithmetic Operations =====

    def add(self, a: float, b: float) -> float:
        """Addition: a + b"""
        result = a + b
        self._record_history('add', a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtraction: a - b"""
        result = a - b
        self._record_history('subtract', a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiplication: a * b"""
        result = a * b
        self._record_history('multiply', a, b, result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Division: a / b"""
        if b == 0:
            raise CalculatorError("Division by zero is not allowed")
        result = a / b
        self._record_history('divide', a, b, result)
        return result

    def floor_divide(self, a: float, b: float) -> float:
        """Floor division: a // b"""
        if b == 0:
            raise CalculatorError("Division by zero is not allowed")
        result = a // b
        self._record_history('floor_divide', a, b, result)
        return result

    def modulo(self, a: float, b: float) -> float:
        """Modulo/Remainder: a % b"""
        if b == 0:
            raise CalculatorError("Modulo by zero is not allowed")
        result = a % b
        self._record_history('modulo', a, b, result)
        return result

    def power(self, base: float, exponent: float) -> float:
        """Exponentiation: base ^ exponent"""
        try:
            result = math.pow(base, exponent)
            self._record_history('power', base, exponent, result)
            return result
        except (ValueError, OverflowError) as e:
            raise CalculatorError(f"Cannot compute {base}^{exponent}: {e}")

    def nth_root(self, a: float, n: float) -> float:
        """Nth root: a^(1/n)"""
        if n == 0:
            raise CalculatorError("Root degree cannot be zero")
        if a < 0 and n % 2 == 0:
            raise CalculatorError("Cannot take even root of negative number")
        result = math.pow(a, 1/n)
        self._record_history('nth_root', a, n, result)
        return result

    # ===== Scientific Functions =====

    def square(self, a: float) -> float:
        """Square: a^2"""
        result = a ** 2
        self._record_history('square', a, None, result)
        return result

    def cube(self, a: float) -> float:
        """Cube: a^3"""
        result = a ** 3
        self._record_history('cube', a, None, result)
        return result

    def square_root(self, a: float) -> float:
        """Square root: sqrt(a)"""
        if a < 0:
            raise CalculatorError("Cannot take square root of negative number")
        result = math.sqrt(a)
        self._record_history('square_root', a, None, result)
        return result

    def cube_root(self, a: float) -> float:
        """Cube root: cbrt(a)"""
        result = math.copysign(abs(a) ** (1/3), a)
        self._record_history('cube_root', a, None, result)
        return result

    def logarithm(self, a: float, base: float = 10) -> float:
        """Logarithm: log_base(a)"""
        if a <= 0:
            raise CalculatorError("Logarithm undefined for non-positive numbers")
        if base <= 0 or base == 1:
            raise CalculatorError("Invalid logarithm base")
        result = math.log(a, base)
        self._record_history('logarithm', a, base, result)
        return result

    def natural_log(self, a: float) -> float:
        """Natural logarithm: ln(a)"""
        if a <= 0:
            raise CalculatorError("Natural log undefined for non-positive numbers")
        result = math.log(a)
        self._record_history('natural_log', a, None, result)
        return result

    def exponential(self, a: float) -> float:
        """Exponential: e^a"""
        try:
            result = math.exp(a)
            self._record_history('exponential', a, None, result)
            return result
        except OverflowError:
            raise CalculatorError("Result too large")

    # ===== Trigonometric Functions =====

    def sin(self, a: float) -> float:
        """Sine (input in radians): sin(a)"""
        result = math.sin(a)
        self._record_history('sin', a, None, result)
        return result

    def cos(self, a: float) -> float:
        """Cosine (input in radians): cos(a)"""
        result = math.cos(a)
        self._record_history('cos', a, None, result)
        return result

    def tan(self, a: float) -> float:
        """Tangent (input in radians): tan(a)"""
        try:
            result = math.tan(a)
            self._record_history('tan', a, None, result)
            return result
        except Exception:
            raise CalculatorError("Tangent undefined at this angle")

    def asin(self, a: float) -> float:
        """Arcsine (output in radians): asin(a)"""
        if abs(a) > 1:
            raise CalculatorError("Arcsine input must be between -1 and 1")
        result = math.asin(a)
        self._record_history('asin', a, None, result)
        return result

    def acos(self, a: float) -> float:
        """Arccosine (output in radians): acos(a)"""
        if abs(a) > 1:
            raise CalculatorError("Arccosine input must be between -1 and 1")
        result = math.acos(a)
        self._record_history('acos', a, None, result)
        return result

    def atan(self, a: float) -> float:
        """Arctangent (output in radians): atan(a)"""
        result = math.atan(a)
        self._record_history('atan', a, None, result)
        return result

    def degrees_to_radians(self, deg: float) -> float:
        """Convert degrees to radians"""
        result = math.radians(deg)
        self._record_history('deg_to_rad', deg, None, result)
        return result

    def radians_to_degrees(self, rad: float) -> float:
        """Convert radians to degrees"""
        result = math.degrees(rad)
        self._record_history('rad_to_deg', rad, None, result)
        return result

    # ===== Hyperbolic Functions =====

    def sinh(self, a: float) -> float:
        """Hyperbolic sine: sinh(a)"""
        result = math.sinh(a)
        self._record_history('sinh', a, None, result)
        return result

    def cosh(self, a: float) -> float:
        """Hyperbolic cosine: cosh(a)"""
        result = math.cosh(a)
        self._record_history('cosh', a, None, result)
        return result

    def tanh(self, a: float) -> float:
        """Hyperbolic tangent: tanh(a)"""
        result = math.tanh(a)
        self._record_history('tanh', a, None, result)
        return result

    # ===== Factorial and Gamma =====

    def factorial(self, a: int) -> float:
        """Factorial: a!"""
        if a < 0 or a != int(a):
            raise CalculatorError("Factorial only defined for non-negative integers")
        result = math.factorial(int(a))
        self._record_history('factorial', a, None, result)
        return result

    def absolute(self, a: float) -> float:
        """Absolute value: |a|"""
        result = abs(a)
        self._record_history('absolute', a, None, result)
        return result

    def round_number(self, a: float, decimals: int = 0) -> float:
        """Round to specified decimal places"""
        result = round(a, decimals)
        self._record_history('round', a, decimals, result)
        return result

    # ===== Memory Functions =====

    def memory_clear(self) -> float:
        """Clear memory (MC)"""
        self._memory = 0.0
        return self._memory

    def memory_recall(self) -> float:
        """Recall memory (MR)"""
        return self._memory

    def memory_add(self, value: float) -> float:
        """Add to memory (M+)"""
        self._memory += value
        return self._memory

    def memory_subtract(self, value: float) -> float:
        """Subtract from memory (M-)"""
        self._memory -= value
        return self._memory

    def memory_set(self, value: float) -> float:
        """Set memory value"""
        self._memory = value
        return self._memory

    # ===== Utility Functions =====

    def _record_history(self, operation: str, a: float, b, result: float):
        """Record calculation in history"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'operand1': a,
            'operand2': b,
            'result': result
        }
        self._history.append(entry)
        self._last_result = result

    def get_history(self) -> List[Dict]:
        """Get calculation history"""
        return self._history.copy()

    def clear_history(self):
        """Clear calculation history"""
        self._history = []

    def get_last_result(self) -> Optional[float]:
        """Get the last calculated result"""
        return self._last_result

    @staticmethod
    def percent(a: float, b: float) -> float:
        """Calculate percentage: what percent is a of b"""
        if b == 0:
            raise CalculatorError("Cannot calculate percentage with zero base")
        result = (a / b) * 100
        return result

    @staticmethod
    def inverse(x: float) -> float:
        """Multiplicative inverse: 1/x"""
        if x == 0:
            raise CalculatorError("Cannot compute inverse of zero")
        return 1 / x

    @staticmethod
    def negate(x: float) -> float:
        """Negate a number: -x"""
        return -x

    @staticmethod
    def pi() -> float:
        """Return the value of pi"""
        return math.pi

    @staticmethod
    def e() -> float:
        """Return the value of e"""
        return math.e


class CalculatorCLI:
    """Command-line interface for the calculator."""

    def __init__(self):
        self.calc = Calculator()
        self.running = True

    def print_menu(self):
        """Print the main menu with available operations."""
        print("\n" + "=" * 60)
        print("        ADVANCED CALCULATOR")
        print("=" * 60)
        print("\n--- Basic Operations ---")
        print("  +   - Addition        |  -   - Subtraction")
        print("  *   - Multiplication  |  /   - Division")
        print("  //  - Floor Division  |  %   - Modulo")
        print("  ^   - Power           |  nrt - Nth Root")
        print("  x%%  - Percentage      |  inv - Inverse (1/x)")
        print("  neg - Negate")
        print("\n--- Scientific Functions ---")
        print("  sqrt - Square Root    |  cbrt - Cube Root")
        print("  sq   - Square         |  cb   - Cube")
        print("  log  - Log(base 10)   |  ln   - Natural Log")
        print("  exp  - e^x            |  fact - Factorial")
        print("  abs  - Absolute Value |  rnd  - Round")
        print("\n--- Trigonometry ---")
        print("  sin  cos  tan    - Basic Trig")
        print("  asin acos atan   - Inverse Trig")
        print("  sinh cosh tanh   - Hyperbolic")
        print("  deg  rad         - Angle Conversion")
        print("\n--- Constants ---")
        print("  pi  - Value of pi      |  e   - Value of e")
        print("\n--- Memory ---")
        print("  mc  - Memory Clear      |  mr  - Memory Recall")
        print("  m+  - Memory Add        |  m-  - Memory Subtract")
        print("\n--- Other ---")
        print("  hist  - Show History    |  clr  - Clear History")
        print("  ms   - Memory Status    |  last - Last Result")
        print("  help  - Show Menu       |  quit - Exit")
        print("\n--- Input Formats ---")
        print("  Binary:  0b1010 + 5")
        print("  Octal:   0o755 + 10")
        print("  Hex:     0xFF + 255")
        print("  Sci:     1.5e3 + 500")
        print("  Memory:  mr + 10  (uses memory value)")
        print("=" * 60)

    def parse_input(self, user_input: str):
        """
        Parse and evaluate a calculator expression.
        Supports binary (0b), octal (0o), hex (0x), scientific notation,
        and all calculator functions.
        """
        user_input = user_input.strip()

        if not user_input:
            return None

        # Handle angle mode display for trig functions
        parts = user_input.split()

        # Check for memory reference (mr)
        if 'mr' in user_input.lower():
            user_input = user_input.replace('mr', str(self.calc.memory_recall()))
            user_input = user_input.replace('MR', str(self.calc.memory_recall()))
            parts = user_input.split()

        # Replace functions with their values/operations
        replacements = {
            'pi': str(math.pi),
            'e': str(math.e),
        }

        for func, value in replacements.items():
            user_input = user_input.replace(func, value)

        return user_input

    def evaluate_expression(self, expression: str) -> Optional[float]:
        """
        Safely evaluate a mathematical expression.
        Supports basic operators, parentheses, and math functions.
        """
        try:
            # Validate expression - only allow safe characters
            import re
            # Remove whitespace
            expr = expression.strip()

            # Replace function names with math module equivalents
            func_map = {
                'sqrt': 'math.sqrt',
                'cbrt': 'math.cbrt',
                'log': 'math.log10',
                'ln': 'math.log',
                'exp': 'math.exp',
                'sin': 'math.sin',
                'cos': 'math.cos',
                'tan': 'math.tan',
                'asin': 'math.asin',
                'acos': 'math.acos',
                'atan': 'math.atan',
                'sinh': 'math.sinh',
                'cosh': 'math.cosh',
                'tanh': 'math.tanh',
                'abs': 'math.fabs',
                'fact': 'math.factorial',
                'deg': 'math.degrees',
                'rad': 'math.radians',
                'pi': str(math.pi),
                'e': str(math.e),
            }

            for func, replacement in func_map.items():
                # Use word boundaries to avoid partial matches
                expr = re.sub(r'\b' + func + r'\b', replacement, expr)

            # Validate that expression only contains safe characters
            allowed_pattern = r'^[\d\s\.\+\-\*\/\%\(\)\^eE]+$'
            if not re.match(allowed_pattern, expr):
                if not re.search(r'[a-zA-Z]', expr):
                    raise CalculatorError("Invalid expression format")

            # Replace ^ with ** for exponentiation
            expr = expr.replace('^', '**')

            # Create safe environment for eval
            safe_dict = {
                '__builtins__': {},
                'math': math,
                'abs': abs,
                'round': round,
            }

            result = eval(expr, safe_dict, {})

            if isinstance(result, float):
                if math.isnan(result):
                    raise CalculatorError("Result is not a number (NaN)")
                if math.isinf(result):
                    raise CalculatorError("Result is infinite")

            return float(result)

        except CalculatorError:
            raise
        except ZeroDivisionError:
            raise CalculatorError("Division by zero is not allowed")
        except ValueError as e:
            raise CalculatorError(f"Invalid value: {e}")
        except Exception as e:
            raise CalculatorError(f"Error evaluating expression: {e}")

    def handle_input(self, user_input: str):
        """Handle different types of user input."""
        user_input = user_input.strip()

        if not user_input:
            return

        # Handle special commands
        cmd = user_input.split()[0].lower() if user_input.split() else ''

        if cmd == 'quit' or cmd == 'exit' or cmd == 'q':
            print("Goodbye! Thanks for using Advanced Calculator.")
            self.running = False
            return

        elif cmd == 'help' or cmd == '?':
            self.print_menu()
            return

        elif cmd == 'hist' or cmd == 'history':
            self.show_history()
            return

        elif cmd == 'clr' or cmd == 'clear':
            self.calc.clear_history()
            print("History cleared.")
            return

        elif cmd == 'mc':
            mem = self.calc.memory_clear()
            print(f"Memory cleared. M = {mem}")
            return

        elif cmd == 'mr':
            mem = self.calc.memory_recall()
            print(f"Memory recall: {mem}")
            print(f"Last result available as 'last'")
            return

        elif cmd == 'ms':
            mem = self.calc.memory_recall()
            print(f"Memory status: M = {mem}")
            return

        elif cmd == 'm+':
            # Add last result to memory
            if self.calc.get_last_result() is not None:
                mem = self.calc.memory_add(self.calc.get_last_result())
                print(f"Added last result to memory. M = {mem}")
            else:
                print("No previous result to add to memory.")
            return

        elif cmd == 'm-':
            if self.calc.get_last_result() is not None:
                mem = self.calc.memory_subtract(self.calc.get_last_result())
                print(f"Subtracted last result from memory. M = {mem}")
            else:
                print("No previous result to subtract from memory.")
            return

        elif cmd == 'last':
            last = self.calc.get_last_result()
            if last is not None:
                print(f"Last result: {last}")
            else:
                print("No previous result.")
            return

        elif cmd == 'pi':
            print(f"pi = {math.pi}")
            return

        elif cmd == 'e':
            print(f"e = {math.e}")
            return

        # Handle single-argument functions
        single_arg_funcs = {
            'sqrt': self.calc.square_root,
            'cbrt': self.calc.cube_root,
            'sq': self.calc.square,
            'cb': self.calc.cube,
            'log': lambda x: self.calc.logarithm(x, 10),
            'ln': self.calc.natural_log,
            'exp': self.calc.exponential,
            'fact': self.calc.factorial,
            'abs': self.calc.absolute,
            'sin': self.calc.sin,
            'cos': self.calc.cos,
            'tan': self.calc.tan,
            'asin': self.calc.asin,
            'acos': self.calc.acos,
            'atan': self.calc.atan,
            'sinh': self.calc.sinh,
            'cosh': self.calc.cosh,
            'tanh': self.calc.tanh,
            'inv': Calculator.inverse,
            'neg': Calculator.negate,
            'deg': Calculator.radians_to_degrees,
            'rad': Calculator.degrees_to_radians,
            'rnd': self.calc.round_number,
        }

        if cmd in single_arg_funcs:
            try:
                if len(user_input.split()) < 2:
                    print(f"Usage: {cmd} <number>")
                    print(f"Example: {cmd} 5")
                    return
                arg = float(user_input.split()[1])
                result = single_arg_funcs[cmd](arg)
                self.display_result(result, user_input)
            except (ValueError, CalculatorError) as e:
                print(f"Error: {e}")
            return

        # Handle percentage
        if cmd == 'pct':
            try:
                parts = user_input.split()
                if len(parts) >= 3:
                    a = float(parts[1])
                    b = float(parts[2])
                    result = Calculator.percent(a, b)
                    self.display_result(result, f"{a}% of {b}")
                else:
                    print("Usage: pct <value> <base>")
            except ValueError:
                print("Error: Please enter valid numbers")
            return

        # Try to evaluate as expression
        try:
            # Handle memory reference in expressions
            expr = user_input
            if 'mr' in expr.lower() and 'mr' != cmd:
                expr = expr.replace('mr', str(self.calc.memory_recall()))
                expr = expr.replace('MR', str(self.calc.memory_recall()))

            result = self.evaluate_expression(expr)
            self.display_result(result, user_input)
        except CalculatorError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def display_result(self, result: float, expression: str):
        """Display the calculation result."""
        print(f"\n  Expression: {expression}")
        print(f"  Result: {self.format_number(result)}")

        # Show additional info for certain results
        if abs(result) > 0 and abs(result) < 1e-10:
            print(f"  Scientific: {result:.2e}")
        elif abs(result) > 1e15:
            print(f"  Scientific: {result:.6e}")

        # Store as last result
        if self.calc._last_result is None:
            self.calc._last_result = result
        else:
            # The operation's _record_history already sets it
            pass

    def format_number(self, num: float) -> str:
        """Format number for display."""
        if num == int(num) and abs(num) < 1e15:
            return str(int(num))
        return f"{num:.10g}"

    def show_history(self):
        """Display calculation history."""
        history = self.calc.get_history()
        if not history:
            print("No calculation history available.")
            return

        print("\n" + "-" * 50)
        print("CALCULATION HISTORY")
        print("-" * 50)
        for i, entry in enumerate(history[-20:], 1):  # Show last 20
            op = entry['operation']
            a = entry['operand1']
            b = entry['operand2']
            result = entry['result']
            ts = entry['timestamp']

            if b is not None:
                print(f"{i:3d}. {op}({a}, {b}) = {self.format_number(result)} [{ts}]")
            else:
                print(f"{i:3d}. {op}({a}) = {self.format_number(result)} [{ts}]")
        print("-" * 50)
        print(f"Total calculations: {len(history)}")

    def save_history(self, filename: str):
        """Save history to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.calc.get_history(), f, indent=2)
            print(f"History saved to {filename}")
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self, filename: str):
        """Load history from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.calc._history = data
            print(f"History loaded from {filename} ({len(data)} entries)")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading history: {e}")

    def run(self):
        """Main calculator loop."""
        print("\n" + "=" * 60)
        print("    WELCOME TO ADVANCED CALCULATOR")
        print("    Type 'help' for menu or 'quit' to exit")
        print("=" * 60)

        while self.running:
            try:
                user_input = input("\n>>> ").strip()
                if user_input:
                    self.handle_input(user_input)
            except KeyboardInterrupt:
                print("\n\nUse 'quit' to exit.")
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")

        # Save history on exit
        if self.calc.get_history():
            save_option = input("\nSave history before exiting? (y/n): ").strip().lower()
            if save_option == 'y':
                filename = input("Enter filename (or press Enter for default): ").strip()
                if not filename:
                    filename = f"calc_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                self.save_history(filename)


# ===== Batch Processing Functions =====

def process_from_file(filepath: str):
    """Process calculations from a file (one expression per line)."""
    calc = Calculator()
    results = []

    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                try:
                    result = eval(line, {'__builtins__': {}, 'math': math, 'abs': abs, 'round': round})
                    if '^' in line:
                        result = eval(line.replace('^', '**'), {'__builtins__': {}, 'math': math, 'abs': abs, 'round': round})
                    results.append({
                        'line': line_num,
                        'expression': line,
                        'result': result
                    })
                    print(f"Line {line_num}: {line} = {result}")
                except Exception as e:
                    print(f"Line {line_num}: Error - {e}")

    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

    return results


# ===== Main Entry Point =====

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Process file mode
        filename = sys.argv[1]
        print(f"Processing calculations from: {filename}")
        process_from_file(filename)
    else:
        # Interactive mode
        cli = CalculatorCLI()
        cli.run()
