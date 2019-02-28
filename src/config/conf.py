import pickle
global config
import os

curr_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_path, 'channel_list.txt')
channel_list = open(file_path, "rb")

config = {

    # details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'srk3141', # your twitch username
    'oauth_password': 'oauth:stohe9j4evimw08quy46nm5htphllu',  # get this from http://twitchapps.com/tmi/

    # channel to join
    'channels': pickle.load(channel_list),

         # if set to true will display any data received
    'debug': False,

    # maximum amount of bytes to receive from socket - 1024-4096 recommended
    'socket_buffer_size': 4096,

    # kafka config - for multiple kafka hosts use comma separated values
    'kafka_brokers': ['localhost:9092'],
    # kafka topic
    'kafka_topic': 'twitch-parsed-message'
}
