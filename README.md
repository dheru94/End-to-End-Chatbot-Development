# Food Corner - A Food Ordering Website with Chatbot Integration

## Overview
**Food Corner** is a vibrant and interactive food ordering website that provides users with a seamless experience to order their favorite dishes. The project integrates a chatbot powered by NLP technologies to assist users in placing orders, tracking their orders, and answering queries. The website is designed with a visually appealing UI and robust backend support.

## Features
- **Interactive Menu:** Displays a variety of food items like Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa.
- **Chatbot Integration:** A Dialogflow-powered chatbot embedded into the website to handle:
  - New order placements.
  - Order tracking.
- **Dynamic Backend:** Built with FastAPI to handle webhook requests and manage database operations efficiently.
- **Database Management:** Uses MySQL to store and track order details, including real-time status updates.
- **Responsive Design:** Fully responsive and visually optimized for an engaging user experience.

## Technologies Used
### Frontend:
- **HTML5 & CSS3**: For designing the website layout and styling.

### Backend:
- **FastAPI**: For handling webhook requests and API endpoints.
- **Dialogflow**: For chatbot integration and intent management.

### Database:
- **MySQL**: For storing and managing order data.

### Tools:
- **Ngrok**: For hosting the FastAPI server and enabling HTTPS access.

## Setup Instructions
### Prerequisites
- Python 3.8+
- MySQL
- Ngrok

### Steps
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd food_corner
   ```

2. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn mysql-connector-python
   ```

3. **Set Up the Database:**
   - Create a MySQL database named `pandeyji_eatery`.
   - Import the required schema:
     ```sql
     CREATE TABLE order_tracking (
         order_id INT PRIMARY KEY,
         status VARCHAR(255)
     );
     -- Add more schema as per the project requirements
     ```

4. **Run the FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Expose the Server Using Ngrok:**
   ```bash
   ngrok http 8000
   ```
   Copy the HTTPS URL provided by Ngrok and update it in your Dialogflow webhook settings.

6. **Launch the Website:**
   Open `index.html` in your browser or deploy it to a server.

## Chatbot Intents
### 1. **order.add**
- **Functionality:** Adds items to the user’s order.
- **Parameters:** `food-item`, `number`.

### 2. **order.remove**
- **Functionality:** Removes items from the user’s order.
- **Parameters:** `food-item`.

### 3. **track.order**
- **Functionality:** Tracks the status of an order.
- **Parameters:** `order_id`.

## File Structure
```plaintext
.
├── main.py                # FastAPI backend logic
├── db_helper.py           # Database interaction functions
├── generic_helper.py      # Helper functions for session management
├── index.html             # Frontend HTML file
├── styles.css             # Frontend CSS file
├── README.md              # Project documentation
```

## Screenshots
- **Banner Image:**
  ![Banner](path_to_banner_image)

- **Website Preview:**
  _Insert a screenshot of the website here_

## Future Enhancements
- Add a payment gateway integration.
- Implement user authentication for a personalized experience.
- Expand the menu with more options and categories.

## Learnings
- Gained hands-on experience with chatbot integration using Dialogflow.
- Improved understanding of FastAPI for building scalable backends.
- Learned how to design responsive and visually appealing websites.
- Strengthened knowledge of database management with MySQL.

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. Suggestions and feedback are always welcome!

## License
This project is licensed under the [MIT License](LICENSE).

---

**Happy Ordering! 🍕🥗**
