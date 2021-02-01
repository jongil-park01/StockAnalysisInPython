from slacker import Slacker

slack = Slacker('xoxb-1719146385936-1710633395777-eX8VvNaI5jEq0mvBnALwUf85')

# Send a message to #stocktrading channel
slack.chat.post_message('#stocktrading', 'Hello Unicorn!')