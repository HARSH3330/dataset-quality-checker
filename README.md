# Dataset Quality Checker 🚦

A simple and user-friendly system to validate vendor-uploaded datasets (CSV/Excel) and provide a quality status report using a traffic light indicator: **Green, Yellow, or Red**.

## 🧠 Purpose

This system is designed to help companies quickly assess the quality of data received from vendors. It evaluates files based on various quality metrics and provides a plain English explanation that even non-technical users (vendors) can understand.

## ✅ Features

- ✅ Supports **CSV** and **Excel** file uploads
- ✅ Validates datasets based on:
  - Missing values
  - Duplicate rows
  - Invalid data types
  - Empty columns
  - Custom business logic (optional)
- ✅ Returns a quality status:
  - 🟢 **Green** – Good quality
  - 🟡 **Yellow** – Acceptable, needs minor fixes
  - 🔴 **Red** – Poor quality, needs attention
- ✅ Vendor-friendly plain English feedback
- ✅ Easily extensible for other data formats and business rules

## 🛠️ Tech Stack

- Python
- Pandas
- Streamlit (for UI) *(optional if you're adding it later)*
- Custom scoring logic

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/dataset-quality-checker.git
cd dataset-quality-checker
