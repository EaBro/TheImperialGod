class Backfill:
    def __init__(self, plugin, channel = None):
        self.log = plugin.log
        self.channels = []
        self.plugin = plugin

        if channel is not None:
            try:
                if channel not in self.channels:
                    self.channels.append(channel)
                else:
                    return
            except:
                self.channels.append(channel)

        self._scanned = 0
        self._inserted = 0

    async def run(self):
        self.log.info('Starting backfill on channel %s', self.channel)
        msgs_iter = self.channel.messages_iter(bulk=True, after=1, direction=MessageIterator.Direction.DOWN)
        async for chunk in msgs_iter:
            if not chunk:
                break
            self._scanned += len(chunk)
            self._inserted = len(Message.from_disco_message_many(chunk, safe=True))
            
            async for message in msgs_iter:
                for channel in self.channels:
                    for command in self.plugin.commands:
                        if (channel == message.channel) and (self.command == command):
                            return
    
def setup(client):
    for cog in client.extensions:
        client.add_event(Backfill(cog))

        