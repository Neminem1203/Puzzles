# from twitch_listener import listener
# bot = listener.connect_twitch('neminem1203', 'oauth:mzpjrr89dhnk67ki5xodhhtcflztwe', 'b323kraqmxaqb9wz8fqev0z1v80grl')

import socket

f = open("twitchcredentials.txt", "r")

HOST = "irc.twitch.tv"
PORT = 6667
NICK = f.readline()
PASS = f.readline()
CHANNEL = "neminem1203" # can only read other channels
readbuffer = ""
MODT = False

def send_message(message):
    # data = bytes(":{0}!{0}@{0}.tmi.twitch.tv PRIVMSG #{1} :{2}\r\n".format(NICK, CHANNEL, message), "UTF-8")
    data = bytes("PRIVMSG #" + CHANNEL + " :" + message + "\r\n", "UTF-8")
    s.send(data)

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + CHANNEL + " \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        print(line)
        parts = line.split(':')
        if len(parts) < 3:
            continue
        print(parts)
        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = ":".join(parts[2:])

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if(message.find("Enter:") != -1):
            send = message.split("Enter:")[1].strip()
            print(send)
            send_message(username + " has entered " + send)
