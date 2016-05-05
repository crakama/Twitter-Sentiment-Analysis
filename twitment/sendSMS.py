# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# Specify your login credentials
class SMS(object):

    def send(self,num):
        def __init__(self):
            pass

        username = "CATHERINERAKAMA"
        apikey = "676dbd926bbb04fa69ce90ee81d3f5ffee2692aaf80eb5793bd70fe93e77dc2e"
        # Specify the numbers that you want to send to in a comma-separated list
        # Please ensure you include the country code (+254 for Kenya)
        to = num
        # And of course we want our recipients to know what we really do
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
        # Create a new instance of our awesome gateway class
        gateway = AfricasTalkingGateway(username, apikey)
        # Any gateway errors will be captured by our custom Exception class below,
        # so wrap the call in a try-catch block
        try:
            # Thats it, hit send and we'll take care of the rest.
            results = gateway.sendMessage(to, message)

            for recipient in results:
                # status is either "Success" or "error message"
                print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                    recipient[
                                                                        'status'],
                                                                    recipient[
                                                                        'messageId'],
                                                                    recipient['cost'])
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while sending: %s' % str(e)
