# 🧠 Week 4 Assignment: AI in Software Engineering  
### Theme: *Building Intelligent Software Solutions*

This project demonstrates practical applications of Artificial Intelligence in software engineering through code automation, testing, and predictive analytics.  
It combines **AI-driven code completion**, **automated testing with Selenium**, and **predictive modeling for resource allocation** using machine learning.

---

## 📘 Part 1: Theoretical Analysis
**Topics Covered**
- **AI-driven code generation:** Tools like GitHub Copilot accelerate development by auto-suggesting code snippets, reducing syntax errors, and saving time. However, they may produce non-optimized or insecure code if used without review.  
- **Bug detection:** Supervised models use labeled data to learn from past bug reports, while unsupervised models cluster anomalies to find new, unseen patterns.  
- **Bias mitigation:** Critical in user personalization systems to ensure fairness and inclusivity across diverse user groups.

---

## ⚙️ Part 2: Practical Implementation

### 🧩 Task 1 – AI-Powered Code Completion
Implemented two Python functions for sorting a list of dictionaries by key: one AI-suggested and one manually written.  
**Analysis:** The AI-generated version was more concise and efficient, showcasing the speed and readability advantages of AI coding tools.

### 🤖 Task 2 – Automated Testing with AI (Flask + Selenium)
Developed a simple **Flask login app** and automated its testing using **Selenium**.  
The AI-assisted test covered both valid and invalid credentials, achieving improved coverage and speed compared to manual testing.

**Login Credentials**
- **Username:** `admin`  
- **Password:** `1234`

### 📊 Task 3 – Predictive Analytics for Resource Allocation
Trained a **Random Forest** model on the Kaggle Breast Cancer dataset (repurposed for issue priority classification).  

**Results**
- **Accuracy:** 97.4%  
- **F1 (macro):** 0.97  
- Model correctly identified almost all priorities, with minimal confusion between medium and high categories.

**Interpretation:**  
The model performs reliably for predictive analytics, helping teams allocate resources efficiently and prioritize high-impact issues.

---

## 🧭 Part 3: Ethical Reflection
Bias can occur if certain issue types or team data are underrepresented.  
Using tools like **IBM AI Fairness 360**, such biases can be detected and mitigated through fairness metrics (e.g., disparate impact) and preprocessing techniques that rebalance the dataset, ensuring fairer model predictions.

---

## 💡 Bonus: Innovation Proposal
**AI Documentation Assistant** – An AI tool that automatically generates software documentation from code comments and commit messages, reducing developer workload and improving maintainability.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KIRUMAH-sam/wk-4_automation.git
cd wk-4_automation


