# Currently Inactive

**Command Prefix**
"-"

**Custom Help**
"-help"

# Commands:
**-b Command:**
Converts binary to text.
Automatically creates a Discord invite link with the converted text.
Handles binary codes with or without spaces between each binary digit.
Removes duplicate "https://discord.gg/" if accidentally included in the input.

**.b Command:**
Fixes backward text.
Removes whitespace.
Creates a Discord invite link with the fixed text.
Handles backward Discord invite codes.
Removes duplicate "https://discord.gg/" if accidentally included.

**-64 Command:**
Converts base64 to text.
Handles base64-encoded strings, removing unnecessary characters.
Sends the decoded text.

**-i Command:**
Removes whitespace and symbols from a Discord invite code.
Creates a Discord invite link with the cleaned code.

# Event Handling:
The bot has an on_message event handler that triggers when a message is received.
It checks for messages starting with "stop" to stop the bot.
It detects and processes messages starting with ".b", "-64", and "-help".


