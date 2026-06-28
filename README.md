# Inventory Management REST API

A RESTful API built with Flask, SQLAlchemy, and MySQL for managing product inventory. This project supports CRUD operations and provides real-time inventory summary analytics. Deployed on Railway.

## Features

- Add new products
- View all products
- Update product details
- Delete products
- Get inventory summary
- Cloud deployment with Railway
- MySQL database integration

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- Railway
- Thunder Client

## API Endpoints

### Get all products
GET /products

Response:
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "quantity": 5,
    "price": 50000
  }
]
```

### Add a product
POST /products

Request Body:
```json
{
  "name": "Laptop",
  "quantity": 5,
  "price": 50000
}
```

Response:
```json
{
  "message": "Product added successfully!"
}
```

### Update product
PUT /products/<id>

Request Body:
```json
{
  "name": "Laptop",
  "quantity": 10,
  "price": 55000
}
```

### Delete product
DELETE /products/<id>

Response:
```json
{
  "message": "Product deleted successfully!"
}
```

### Inventory summary
GET /products/summary

Response:
```json
{
  "total_inventory_value": 250000,
  "total_products": 1,
  "total_quantity": 5
}
```

## Live Demo

Base URL:
https://web-production-26a59.up.railway.app

## Installation

Clone repository:

```bash
git clone https://github.com/RRC2002/inventory-management-api.git
cd inventory-management-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python app.py
```

## Deployment

Deployed on Railway with MySQL database integration.

## Author

Rajashree Roy Choudhury
