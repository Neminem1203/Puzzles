import socket
f = open("twitchcredentials.txt", "r") # put your username in the first line and oauth in the second line
HOST = "irc.twitch.tv"
PORT = 6667
NICK = f.readline().strip()
PASS = f.readline().strip()
# CHANNEL = NICK # can only read other channels
readbuffer = ""
MODT = False
s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))

def send_message(message):
    # data = bytes(":{0}!{0}@{0}.tmi.twitch.tv PRIVMSG #{1} :{2}\r\n".format(NICK, CHANNEL, message), "UTF-8")
    data = bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8")
    s.send(data)

while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

disconnect = False
antispam = 0
while not disconnect:
    for line in str(s.recv(1024)).split('\\r\\n'):
        print(line)
        parts = line.split(':')
        print(parts)
        if(line == "b''"): # not sure why but sometimes my terminal gets spammed
            antispam += 1
            if antispam > 10:
                disconnect = True
        if("PING" in parts[0]): # Response to Ping from Twitch
            print("Sending Pong Message")
            s.send(bytes("PONG :tmi.twitch.tv", "UTF-8"))
        if len(parts) < 3:
            continue
        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = ":".join(parts[2:])

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if(message.lower().find("enter:") != -1):
            send = message.lower().split("enter:")[1].strip()
            send_message(username+" has entered "+send)
