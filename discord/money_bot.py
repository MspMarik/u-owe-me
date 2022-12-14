import discord
import responses
import yaml


info = 'INFO_YAML_PATH'

with open(info) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


# Send messages
async def send_message(user, message, user_message, is_private):
    user_message = user_message.lower()
    try:
        response = responses.handle_response(user_message, user)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    token = data["accounts"]["accountant"]["discord"]
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if (message.author == client.user) or (str(message.author) == "Filament Bot#4129"):
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        if channel == "settlements":

            # If the user message contains a '?' in front of the text, it becomes a private message
            if user_message[0] == '?':
                user_message = user_message[1:]  # [1:] Removes the '?'
                await send_message(username, message, user_message, is_private=True)
            else:
                await send_message(username, message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(token)

