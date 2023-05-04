import sys
import logging

import smpplib.gsm
import smpplib.client
import smpplib.consts

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(filename)s:%(lineno)d %(message)s"
)


class SMPPService:
    client = None

    def __init__(self):
        self.client = smpplib.client.Client('127.0.0.1', 2775)
        self.client.set_message_sent_handler(
            lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
        self.client.set_message_received_handler(
            lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

        self.client.connect()
        self.client.bind_transceiver(system_id='osmocom', password='osmocom1')

    def send_normal(self, string='', dest='2222', source='6666'):
        parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(string)
        # part = b"".join(parts)
        try:
            string.encode("ascii")
            coding = encoding_flag
        except:
            coding = smpplib.consts.SMPP_ENCODING_ISO10646
        logging.info('Sending SMS "%s" to %s' % (string, dest))
        for part in parts:
            pdu = self.client.send_message(
                msg_type=smpplib.consts.SMPP_MSGTYPE_USERACK,
                source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
                source_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
                source_addr=source,
                dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
                destination_addr=dest,
                short_message=part,
                data_coding=coding,
                esm_class=msg_type_flag,
                # esm_class=smpplib.consts.SMPP_MSGMODE_FORWARD,
                registered_delivery=True,
            )
            logging.debug(pdu.sequence)

s = SMPPService()
s.send_normal('test', '2222')

