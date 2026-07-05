# 📚 Book Price Monitor & Analysis

## 📌 Project Overview

The **Book Price Monitor** project is a web scraping and data analysis application that collects book information from an online bookstore and transforms it into actionable business insights. The application extracts book details such as title, price, rating, and availability, stores the data in a CSV file, and provides analysis to support pricing and inventory decisions.

This project demonstrates skills in **Python, Web Scraping, Data Cleaning, Data Analysis, and Dashboard Development**.

---

# 🎯 Business Problem Statement

Online bookstores contain thousands of products whose prices, ratings, and stock availability change frequently. Manually tracking this information is time-consuming and inefficient.

The objective of this project is to automate the collection of book data and generate insights that help stakeholders:

- Monitor product prices
- Identify highly rated books
- Track stock availability
- Analyze pricing trends
- Support pricing and inventory decisions

---

# 📂 Dataset Information

The scraped dataset contains the following fields:

| Column | Description |
|---------|-------------|
| Book Name | Title of the book |
| Price | Selling price |
| Rating | Customer rating (One to Five) |
| Availability | Stock availability |

---

# 📊 Key Performance Indicators (KPIs)

- Total Books Scraped
- Average Book Price
- Highest Priced Book
- Lowest Priced Book
- Books Available in Stock
- Average Customer Rating

---

# 📈 Dashboard Features

- 📚 Total Books Overview
- 💰 Price Distribution
- ⭐ Rating Distribution
- 📦 Stock Availability Analysis
- 🔍 Search Books by Name
- 📊 Interactive Charts
- 📈 Summary Statistics

---

# 🔍 Business Questions Answered

- Which books have the highest prices?
- What is the average price of books?
- Which rating category contains the most books?
- How many books are currently in stock?
- What percentage of books have a rating of Four or Five?
- Which books provide the best value based on price and rating?

---

# 💡 Business Insights

- Identify premium-priced books.
- Discover the most highly rated books.
- Monitor inventory availability.
- Compare prices across multiple books.
- Analyze customer preferences through ratings.

---

# ✅ Recommendations

- Promote highly rated books to increase sales.
- Monitor expensive books for pricing optimization.
- Restock popular books that become unavailable.
- Offer discounts on low-rated or slow-moving books.
- Track pricing regularly to remain competitive.

---

# 🛠 Technologies Used

- Python
- Pandas
- BeautifulSoup
- Requests
- Streamlit
- Plotly
- VS Code
- CSV

---

# 📁 Project Structure

```
Book-Price-Monitor/
│
├── app.py
├── scraper.py
├── products.csv
├── requirements.txt
├── README.md
├── assets/
│   └── dashboard.png
└── screenshots/
```

---

# 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/AravindJ03042004/Competitor_Price_Monitor-
```

### 2. Navigate to the Project Folder

```bash
cd book-price-monitor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Scraper (Optional)

```bash
python scraper.py
```

### 5. Launch the Dashboard

```bash
streamlit run app.py
```

---

# 📷 Dashboard Preview

> Add screenshots of your Streamlit dashboard here.

```
screenshots/dashboard.png
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Web Scraping using BeautifulSoup
- Data Cleaning with Pandas
- Exploratory Data Analysis (EDA)
- Interactive Dashboard Development
- Business Insight Generation
- Data Visualization
- CSV Data Management

---

# 📈 Future Enhancements

- Multi-page web scraping
- Automatic scheduled scraping
- Historical price tracking
- Price change alerts
- Database integration (MySQL/PostgreSQL)
- Export reports in PDF and Excel
- Deploy dashboard to Streamlit Community Cloud

---

# 👨‍💻 Author

**Lucky Aravind**

Aspiring Data Analyst

### Skills
- Python
- SQL
- Excel
- Power BI
- Streamlit
- Web Scraping
- Data Visualization

**GitHub:**https://github.com/AravindJ03042004/Competitor_Price_Monitor-

**LinkedIn:**https://www.linkedin.com/in/aravind-j-3b3269281/