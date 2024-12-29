# Fruit Management App

A web application with React frontend and Python backend.

## Project Structure

```
.
├── backend/              # Python FastAPI backend 
│   ├── main.py          # Main application entry
│   └── requirements.txt  # Python dependencies
└── frontend/            # React + Vite frontend
    ├── src/            # Source code
    ├── public/         # Static assets
    └── index.html      # Entry HTML file
```


## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 
- npm/yarn

### Backend Setup

1. Create and activate virtual environment:
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
cd backend
pip install -r requirements.txt

3. Run the backend server:
uvicorn main:app --reload


### Frontend Setup

1. Install dependencies:
cd frontend
npm install
npm install axios

2. Start development server:
npm run dev


### Development
- Frontend runs on: http://localhost:5173
- Backend API runs on: http://localhost:8000


## Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add some amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request