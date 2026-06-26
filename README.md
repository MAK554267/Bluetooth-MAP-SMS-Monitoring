# Bluetooth MAP-Based SMS Monitoring and OTP Authentication Security Analysis

> A Wireless & Mobile Security project demonstrating Bluetooth Message Access Profile (MAP), SMS event monitoring, and OTP authentication simulation in a controlled laboratory environment.

---

# Overview

This project was developed as part of the **Wireless and Mobile Security** course at the **University of Wah**.

The objective is to demonstrate how Bluetooth Message Access Profile (MAP) works and analyze its relationship with SMS-based One-Time Password (OTP) authentication.

The project consists of two environments:

* **Windows** – Hosts the authentication portal.
* **Kali Linux** – Monitors Bluetooth MAP events and displays them on a Flask dashboard.

---

# Technologies Used

### Operating Systems

* Windows 10 / Windows 11
* Kali Linux

### Programming Languages

* Python
* HTML
* CSS
* JavaScript

### Frameworks

* Flask
* Bootstrap 5

### Authentication

* Firebase Authentication (Testing Mode)

### Wireless Technologies

* Bluetooth Classic
* Bluetooth Message Access Profile (MAP)

### Tools

* VirtualBox
* VS Code
* Git
* GitHub
* mapAccountHijack

---

# Hardware Requirements

* Android Smartphone
* Bluetooth USB Adapter (Bluetooth 4.0+ Recommended)
* Laptop/Desktop
* Internet Connection

---

# Software Requirements

## Windows

* Google Chrome
* Visual Studio Code (Optional)

## Kali Linux

Install required packages:

```bash
sudo apt update

sudo apt install bluetooth

sudo apt install bluez

sudo apt install bluez-tools

sudo apt install libbluetooth-dev

sudo apt install build-essential

sudo apt install python3

sudo apt install python3-pip

sudo apt install python3-venv
```

---


# Running the Project

## Step 1 – Clone This Repository

```bash
git clone https://github.com/MAK554267/Bluetooth-MAP-SMS-Monitoring.git

cd Bluetooth-MAP-SMS-Monitoring
```

---

## Step 2 – Clone mapAccountHijack (Kali Linux)

```bash
git clone https://github.com/sgxgsx/mapAccountHijack.git

cd mapAccountHijack
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install required packages:

```bash
pip install aiohttp pyobex requests
```

---

## Step 3 – Configure Firebase Authentication (Windows)

The authentication portal uses **Firebase Phone Authentication**.

Before running the login portal:

1. Create a Firebase project.
2. Enable **Phone Authentication**.
3. Copy your Firebase configuration.
4. Open the login HTML file.
5. Locate the following section:

```javascript
const firebaseConfig = {
    apiKey: "...",
    authDomain: "...",
    projectId: "...",
    storageBucket: "...",
    messagingSenderId: "...",
    appId: "..."
};
```

6. Replace the placeholder values with **your own Firebase project configuration**.

> **Note:** Never commit your production Firebase credentials or sensitive configuration to a public repository. Use a separate testing project or environment variables where appropriate.

---

## Step 4 – Run Login Portal (Windows)

Open

```
index.html
```

using:

* Google Chrome

or

* VS Code Live Server

---

## Step 5 – Configure Bluetooth (Kali Linux)

Restart Bluetooth:

```bash
sudo systemctl restart bluetooth
```

Verify adapter:

```bash
hciconfig
```

---

## Step 6 – Pair Android Device

```bash
bluetoothctl
```

Commands:

```text
power on

agent on

default-agent

scan on

pair <PHONE_MAC>

trust <PHONE_MAC>

connect <PHONE_MAC>
```

---

## Step 7 – Verify MAP Service

```bash
sdptool browse <PHONE_MAC>
```

---

## Step 8 – Start Flask Dashboard

Navigate to the Dashboard folder.

Run:

```bash
python3 server.py
```

Open:

```
http://127.0.0.1:8080
```

---

## Step 9 – Start Bluetooth Monitoring

Navigate to mapAccountHijack.

Run:

```bash
python3 mapAccountHijack.py \
--address <PHONE_MAC> \
--dest-dir ./out \
--backend http://127.0.0.1:8080/
```

---

## Step 10 – Demonstration

1. Open the Login Portal on Windows.
2. Request OTP.
3. Generate SMS activity on the Android phone.
4. Bluetooth MAP forwards message events.
5. Kali Linux receives monitoring events.
6. Flask Dashboard displays the events in real time.

---

# Problems Encountered

* Bluetooth adapter not detected in VirtualBox.
* Smartphone pairing issues.
* Python dependency conflicts.
* Bluetooth service configuration errors.
* Dashboard communication issues.
* Firebase testing limitations.

Each issue was resolved through proper configuration, dependency installation, and Bluetooth service setup.

---

# Security Analysis

This project demonstrates:

* Bluetooth Message Access Profile (MAP)
* Bluetooth trust relationships
* SMS event monitoring
* Mobile authentication security
* Wireless communication security
* Authentication workflow analysis

---

# Future Improvements

* Support Bluetooth Low Energy (BLE)
* Dashboard analytics
* Multi-device monitoring
* Enhanced visualization
* Authenticator App integration

---

# Disclaimer

This project is intended **only for educational and cybersecurity research purposes**.

All demonstrations were performed in a controlled laboratory environment using devices owned or authorized by the project team.

Do not use this project to access or monitor devices without authorization.

---

# Authors

* Hassan Iftikhar
* Muhammad Azfar Waqas
* Albash Ahmed

Department of Computer Science

University of Wah

Course: Wireless and Mobile Security
