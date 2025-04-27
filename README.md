# 🍽️ ByteAndBite

**ByteAndBite** is a Python script that keeps you updated on the real-time delivery status of your favorite restaurants on the [Wolt](https://wolt.com/) platform.  
No more endless refreshing—get notified the moment your chosen venue opens for delivery!

---

## 🚀 Features

- **Real-Time Tracking:** Instantly know when a restaurant is open for delivery.
- **Automatic Polling:** Checks every 5 seconds—so you don't have to.
- **Simple to Use:** Just paste the Wolt restaurant URL and relax.
- **Terminal Notifications:** Get clear, timestamped updates right in your terminal.

---

## 🛠️ Installation

1. **Clone this repository** (or download `ByteAndBite.py`):

   ```bash
   git clone <your-repo-url>
   cd ByteAndBite
   ```

2. **Install dependencies:**

   ```bash
   pip install requests
   ```

---

## 💡 Usage

1. **Run the script:**

   ```bash
   python ByteAndBite.py
   ```

2. **When prompted, paste the Wolt restaurant URL:**

   ```
   Enter the Wolt web address of the restaurant's page:
   https://wolt.com/en/isr/tel-aviv/restaurant-name
   ```

3. **Watch the terminal for updates:**

   ```
   Polling https://consumer-api.wolt.com/order-xp/web/v1/venue/slug/restaurant-name/dynamic to check if restaurant-name is open
   Venue is closed. Retrying in 5 seconds... (12:34:56)
   Venue is open at: 12:35:01. Bon Appétit.
   Press ENTER to close ByteAndBite....
   ```

---

## 📦 How It Works

1. **URL Conversion:** Converts your Wolt restaurant URL into the correct API endpoint.
2. **Polling:** Repeatedly checks the restaurant's delivery status via the Wolt API.
3. **Notification:** Alerts you as soon as the venue is open for delivery.

---

## 📝 Notes

- Works only with valid Wolt restaurant URLs.
- If the API is unreachable, the script will retry every 5 seconds.
- No personal data is collected or stored.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR.

---

## 📄 License

MIT License

---

**Enjoy your meal, and happy ordering!** 🍔🍕🍣
