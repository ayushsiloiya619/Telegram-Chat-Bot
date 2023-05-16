<!DOCTYPE html>
<html>
<head>
  
</head>
<body>
  <h1>Telegram Chatbot</h1>
  
  <p>This repository contains code for a Telegram chatbot implemented in Python. The chatbot is designed to respond to user messages with predefined responses. It utilizes the Telegram Bot API and the <code>python-telegram-bot</code> library for interaction with the Telegram platform.</p>
  
  <h2>Getting Started</h2>
  
  <h3>Dependencies</h3>
  
  <ul>
    <li><code>python-telegram-bot</code> library: Install using <code>pip install python-telegram-bot</code></li>
    <li><code>responses</code> module: You can implement this module to define your own responses based on user messages</li>
  </ul>
  
  <h3>Setting Up the Bot</h3>
  
  <ol>
    <li>Create a new bot on Telegram by following the <a href="https://core.telegram.org/bots#botfather">BotFather</a> instructions. Obtain the API key for your bot.</li>
    <li>Replace <code>keys.API_KEY</code> in the code with your bot's API key.</li>
  </ol>
  
  <h2>Usage</h2>
  
  <p>The chatbot provides the following commands:</p>
  
  <ul>
    <li><code>/start</code>: Starts the chatbot and displays a welcome message.</li>
    <li><code>/help</code>: Displays a help message with instructions.</li>
    <li><code>/contact</code>: Provides contact information for the bot's developer.</li>
  </ul>
  
  <p>The chatbot also responds to any text message sent by the user with predefined responses defined in the <code>responses</code> module.</p>
  
  <h2>Code Overview</h2>
  
  <p>The Python code in this repository consists of the following components:</p>
  
  <ul>
    <li><code>constants.py</code>: Contains the API key and any other constants required for the chatbot.</li>
    <li><code>responses.py</code>: Defines the responses for the chatbot based on user messages.</li>
    <li><code>main.py</code>: The main script that initializes the chatbot, sets up command and message handlers, and starts the bot.</li>
  </ul>
  
  <h3>Command Handlers</h3>
  
  <ul>
    <li><code>/start</code>: The <code>start_command</code> function handles the <code>/start</code> command and displays a welcome message.</li>
    <li><code>/help</code>: The <code>help_command</code> function handles the <code>/help</code> command and displays a help message.</li>
    <li><code>/contact</code>: The <code>contact_command</code> function handles the <code>/contact</code> command and provides contact information for the bot's developer.</li>
  </ul>
  
  <h3>Message Handler</h3>
  
  <p>The <code>handle_message</code> function is responsible for processing text messages sent by the user. It converts the message to lowercase, determines an appropriate response based on the <code>responses</code> module, and sends the response back to the user.</p>
    <h2>Contributing</h2>
  <p>If you wish to contribute to this project, you can:</p>
  <ul>
    <li>Fork the repository.</li>
    <li>Make your desired changes and improvements.</li>
    <li>Submit a pull request with a detailed explanation of the changes you made.</li>
  </ul>
  <p>We welcome and appreciate your contributions!</p>
  <h2>Contact</h2>
  <p>If you have any questions or suggestions regarding the chatbot or this repository, please feel free to contact <a href="mailto:ayushsiloiya@gmail.com">Ayush Siloiya</a>.</p>
</body>
</html>
