# Shopper-Spectrum-Ecommerce-Analytics
Customer Segmentation and Product Recommendation System using RFM Analysis, KMeans Clustering, and Collaborative Filtering with Streamlit Deployment.

## 📌 Project Overview
The global e-commerce industry generates massive volumes of transactional data daily. Extracting actionable insights from this data is crucial for improving customer experience, optimizing marketing strategies, and driving business growth.

**Shopper Spectrum** is an end-to-end data analytics and machine learning project that focuses on:
- Segmenting customers based on purchasing behavior using **RFM analysis and clustering**
- Recommending similar products using **item-based collaborative filtering**
- Providing real-time predictions through an interactive **Streamlit web application**

---

## 🎯 Business Objectives
- Identify high-value, regular, occasional, and at-risk customers
- Enable targeted marketing and retention strategies
- Provide personalized product recommendations
- Improve cross-selling and inventory planning decisions

---

## 🧠 Problem Type
- **Unsupervised Machine Learning** – Customer Segmentation
- **Recommendation System** – Collaborative Filtering

---

## 📊 Dataset Description
The dataset consists of transactional records from an online retail business.

| Column Name | Description |
|------------|------------|
| InvoiceNo | Unique transaction number |
| StockCode | Unique product code |
| Description | Product name |
| Quantity | Number of items purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Customer’s country |

---

## 🔧 Project Workflow

### 1️⃣ Data Cleaning & Preprocessing
- Removed records with missing `CustomerID`
- Excluded cancelled invoices
- Filtered invalid quantities and prices
- Created a new feature: `TotalAmount = Quantity × UnitPrice`

---

### 2️⃣ Exploratory Data Analysis (EDA)
- Transaction volume by country
- Top-selling products
- Monthly sales trends
- Distribution of monetary values
- RFM metric distributions

EDA provided insights into customer behavior patterns and sales trends.

---

### 3️⃣ RFM Analysis
Customer behavior was quantified using:
- **Recency**: Days since last purchase
- **Frequency**: Number of transactions
- **Monetary**: Total spend by customer

RFM values were standardized to prepare for clustering.

---

### 4️⃣ Customer Segmentation (KMeans Clustering)
- Optimal number of clusters determined using:
  - Elbow Method
  - Silhouette Score
- Customers segmented into:
  - **High-Value**
  - **Regular**
  - **Occasional**
  - **At-Risk**

Each cluster was interpreted using average RFM values to derive business meaning.

---

### 5️⃣ Product Recommendation System
- Implemented **Item-Based Collaborative Filtering**
- Created a customer–product interaction matrix
- Computed **cosine similarity** between products
- Recommended top 5 similar products based on purchase history

---

### 6️⃣ Streamlit Web Application
The application provides two interactive modules:

#### 🎯 Product Recommendation
- User inputs a product name
- System returns 5 similar products in real time

#### 👥 Customer Segmentation
- User inputs Recency, Frequency, and Monetary values
- System predicts the customer segment instantly

---

## 🛠 Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Cosine Similarity
- KMeans Clustering
- Streamlit
- Google Colab

---

## 📦 Project Deliverables
- 📓 Jupyter Notebook with:
  - Cleaned data
  - EDA visualizations
  - RFM analysis
  - Clustering evaluation
  - Recommendation system
- 📊 Streamlit Web Application
- 📁 Saved ML models for real-time prediction

---

## 🚀 How to Run the Streamlit App
```bash
pip install streamlit
streamlit run app.py


