# 🧮 Streamlit Smart Calculator

A modern calculator web application built using **Python** and **Streamlit** with an interactive UI, structured calculation history, and expandable architecture for future enhancements.

---

# 🚀 Overview

This project started as a simple calculator and is progressively evolving into a feature-rich smart calculator application with:

- Interactive UI
- Multiple mathematical operations
- Persistent session history
- Tabular analytics-style history tracking
- Modular and scalable structure
- Future support for scientific and advanced features

The application is developed using:

- Python
- Streamlit
- Pandas
- GitHub Codespaces
- VS Code

---

# ✨ Current Features

## ✅ Core Calculator Features

- Addition
- Subtraction
- Multiplication
- Division
- Percentage Calculation
- Power Operation
- Modulus Operation
- Square Root Calculation

---

## ✅ Smart Input Handling

- Clean numeric inputs
- Removes unnecessary `.00` formatting
- Supports both integers and decimals dynamically

---

## ✅ Error Handling

- Division by zero protection
- Invalid square root protection
- Graceful error messaging

---

## ✅ Structured Calculation History

The app stores calculations in a professional tabular format including:

| Column | Description |
|---|---|
| Number 1 | First input value |
| Operation | Selected mathematical operation |
| Number 2 | Second input value |
| Result | Computed output |
| Timestamp | Time calculation was performed |

History is displayed using interactive Streamlit DataFrames.

---

## ✅ Interactive UI Elements

- Dropdown operation selector
- Action buttons
- Styled result display
- Interactive history table

---

## ✅ Session State Support

Uses Streamlit session state to preserve:

- Calculation history
- User interactions during app runtime

---

# 📂 Project Structure

```text
calculator-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
└── assets/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
```

---

## 2. Navigate Into Project

```bash
cd calculator-app
```

---

## 3. Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application will start locally at:

```text
http://localhost:8501
```

---

# 📦 Current Dependencies

- streamlit
- pandas

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| Pandas | Tabular data handling |
| GitHub Codespaces | Cloud development environment |
| VS Code | Development IDE |

---

# 📊 Application Architecture Direction

This project is intentionally designed to evolve progressively into a more advanced calculator and analytics-style application.

The architecture is being built incrementally to support future enhancements cleanly.

---

# 🔮 Planned Future Enhancements

The following features are planned for future versions:

## Scientific Features

- Trigonometric functions
- Logarithms
- Factorials
- Constants (π, e)
- Advanced equations

---

## UI Enhancements

- Dark/Light theme switcher
- Responsive layouts
- Improved styling
- Keyboard input support
- Better mobile experience

---

## History & Analytics

- Export history to CSV
- Search/filter history
- Sort calculations
- Usage statistics
- Charts and visualizations

---

## Productivity Features

- Memory storage
- Save favorite calculations
- Calculation replay
- Multi-tab calculator modes

---

## Advanced Features

- Unit converter
- Currency converter
- Graph plotting
- AI-assisted explanations
- Voice input support

---

## Backend & Data Features

- SQLite database integration
- User authentication
- Cloud persistence
- API integrations

---

# 📘 Learning Goals of This Project

This project is also being used as a practical learning platform for:

- Python development
- Streamlit framework
- Stateful web applications
- UI/UX concepts
- Data handling with pandas
- Git & GitHub workflows
- Cloud-based development
- Incremental software architecture

---

# 🤝 Contribution

This project is actively evolving.

Future improvements and refactoring are expected as new features are introduced.

---

# 📄 License

This project is currently open for personal learning and experimentation.

---

# 🚀 Future Vision

The long-term goal is to transform this application from a basic calculator into a:

- Smart productivity utility
- Scientific calculator
- Analytics-enabled calculator
- Interactive educational tool

while continuously improving software engineering practices during development.