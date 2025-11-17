# 3110PythonNumericalLiteralChecker
# 🧮 Finite State Machine Number Validator

A Python implementation of **Finite State Machines (FSMs)** that validate **oct integers**, **hex integers**, **decimal integers** and **floating-point numbers** *without using* built-in parsing functions like `int()`, `float()`, `str.isdigit()`, or regular expressions.

---

## 👥 Group Members

| Full Name | GitHub Username | Tasks Completed | Extra Credit |
|------------|-----------------|-----------------|---------------|
|**Yong Thu La Wong**| @yxngles13 | Constructed all the NFAs and implemented main() function | Worked on all extra credit portion|
| **Josephine Villar** || Implemented hexinteger, decinteger, and octinteger functions | Reviewed all the NFAs and double checked them |


---

### 🔢 1. Decimal Integer (`is_decint`)
**Base:** 10  
**Description:** Standard non-negative integers without leading zeros (except `0` itself).  

---

### 🧮 2. Octal Integer (`is_octint`)
**Base:** 8  
**Description:** Integer literals starting with a `0o` or `0O` prefix followed by digits `0–7`.  

---

### 🧠 3. Hexadecimal Integer (`is_hexint`)
**Base:** 16  
**Description:** Integer literals starting with `0x` or `0X`, followed by digits `0–9` or letters `a–f` / `A–F`.  

---

### 🌊 4. Floating Point (`is_floatingpoint`)
**Base:** 10 (with optional scientific notation)  
**Description:** Floating-point numbers with optional sign, decimal point, and exponent (`e` / `E`).  

---

### 📊 Summary

| Literal Type | Prefix | Example | Base | Function |
|---------------|---------|----------|------|-----------|
| Decimal | none | `123`, `0` | 10 | `is_decint()` |
| Octal | `0o` or `0O` | `0o755` | 8 | `is_octint()` |
| Hexadecimal | `0x` or `0X` | `0xFF` | 16 | `is_hexint()` |
| Floating-point | optional sign, `.`, `e` | `-3.14e2` | 10 | `isfloatingpoint()` |

---

