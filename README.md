# Full Stack Developer Demo – Django + DRF + PostgreSQL (SQLite for demo)

This is a simple demo project built with **Django** and **Django REST Framework**.  
It demonstrates the key skills requested in the assignment:

- ✅ Basic CRUD APIs
- ✅ Integration with a third-party API
- ✅ Simple reporting / data visualization

## Features

1. **CRUD API for Items**
   - Endpoints: `/api/items/`
   - Supports `GET, POST, PUT, DELETE`

2. **Third-Party API Integration**
   - Endpoint: `/api/fetch-btc/`
   - Fetches real-time Bitcoin price (USD) from [CoinGecko API](https://www.coingecko.com/)

3. **Reporting & Visualization**
   - Endpoint: `/api/report/`
   - Displays a bar chart (Chart.js) of items created in the last 7 days.

4. **Welcome Page**
   - Root URL `/` shows a simple welcome page with links to all endpoints.

---

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (default)  
  *(Can be swapped to PostgreSQL/Supabase by updating `DATABASES` in `settings.py`)*
- **Visualization:** Chart.js (via template)
- **3rd-party API:** CoinGecko (Bitcoin price)


Server runs at: http://127.0.0.1:8000/



📌 Endpoints

Root Welcome: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

CRUD Items: http://127.0.0.1:8000/api/items/

Bitcoin Price: http://127.0.0.1:8000/api/fetch-btc/

Items Report: http://127.0.0.1:8000/api/report/
```bash
git clone https://github.com/your-username/django-demo-priyanka.git
cd django-demo-priyanka
