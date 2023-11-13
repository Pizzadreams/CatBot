# CatBot

## A Discord bot that generates cat images

### To achieve this goal:

* Find a Cat Image API: Look for a Cat Image API that provides random cat images. There are several APIs available, such as thecatapi.com or random.cat, which allows me to fetch random cat images programmatically.

* Set up a Backend Server: Create a backend server using Python. This server will act as a bridge between the Discord bot and the Cat Image API.

* Integrate the Cat Image API: Write the necessary code in the backend server to fetch random cat images from the chosen Cat Image API. Make HTTP requests to the API's endpoints and retrieving the image URLs.

* Create a Discord Bot: Set up a Discord bot by creating an application on the Discord Developer Portal. Obtain the bot token, which will be used to authenticate the bot with Discord's API. 

* Add the Bot to Discord Server: Invite the Discord bot to server by generating an invite link from the Developer Portal. Steps for adding the Bot to the Discord Server:
  1. In the Developer Portal, go to the "OAuth2" section.
  2. Under the "Scopes" section, select the "bot" checkbox.
  3. Scroll down to the "Bot Permissions" section and select the necessary permissions your bot requires (e.g., Read Messages, Send Messages, etc.).
  4. Copy the generated OAuth2 URL and open it in a new browser tab.
  5. Select your Discord server from the dropdown and click "Authorize" to add the bot to your server.<p></p>
* Link the Bot to the Backend: Write code in backend server to handle Discord bot commands. Use a Discord library like discord.js (for Node.js) or discord.py (for Python) to interact with the Discord API. Create a command that triggers the generation and sending of a random cat image.

* Deploy the Backend: Deploy backend server to a hosting platform or a server that is publicly accessible. Allow Discord to communicate with server and retrieve random cat images.

* Test and Use the Bot: Test the Discord bot in server by triggering the command of your choice to generate a random cat image. 