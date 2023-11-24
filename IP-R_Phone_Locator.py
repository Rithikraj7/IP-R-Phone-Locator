import os
import time
from termcolor import colored
from twilio.rest import Client
import scapy.all as scapy
import phonenumbers
from phonenumbers import geocoder, carrier
import asyncio
import uuid
from scapy.all import sniff, IP


class MassageCarrier:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send_massage(self, message):
        client = Client(" Twilio Account SID", "Twilio Auth Token")
        client.messages.create(
            to=self.phone_number,
            from_='Twilio phone number',
            body=message,
        )
        # Trace the network transmission of the message.
        scapy.sniff(prn=self.trace_network_transmission, count=10, timeout=1)

    def trace_network_transmission(self, packet):
        if packet.haslayer(scapy.IP):
            source_ip = packet[scapy.IP].src
            destination_ip = packet[scapy.IP].dst
            print(f"Packet from: {source_ip} to: {destination_ip}")


class SMSTool:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.carrier = MassageCarrier(phone_number)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show_logo():
        SMSTool.clear_screen()
        time.sleep(1)
        print(colored(
            """
            ██╗██████╗       ██████╗     ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗      ██████╗  ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
            ██║██╔══██╗      ██╔══██╗    ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
            ██║██████╔╝█████╗██████╔╝    ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
            ██║██╔═══╝ ╚════╝██╔══██╗    ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
            ██║██║           ██║  ██║    ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
            ╚═╝╚═╝           ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
            Author: Rithik R
            About : SMS IP Hacking 
            """, 'green'))

    def send_massage(self, message):
        self.carrier.send_massage(message)

    def trace_network_transmission(self):
        self.carrier.send_massage("Tracing network transmission...")
        # You can add the logic for network transmission tracing here.

    def get_ip_phoneinfo(self, number):
        pep = phonenumbers.parse(number, "en")

        # Get location information
        location = geocoder.description_for_number(pep, "en")

        # Get carrier information
        service_provider = carrier.name_for_number(pep, "en")

        # Get region information
        region = geocoder.region_code_for_number(pep)

        # Print all details
        print(f"Phone Number: {number}")
        print(f"Location: {location}")
        print(f"Service Provider: {service_provider}")
        print(f"Region Code: {region}")

    async def get_actual_ip_address(self, destination_ip):
        """Gets the actual IP address of the receiver's device.

        Args:
            destination_ip: The IP address of the receiver's device.

        Returns:
            The actual IP address of the receiver's device.
        """

        # Get the ARP response for the destination IP address.
        arp_response = await asyncio.get_event_loop().run_in_executor(None, arping, destination_ip)

        # Get the actual IP address of the receiver's device from the ARP response.
        actual_destination_ip = arp_response[0][1].psrc

        return actual_destination_ip

    def packet_callback(self, packet):
        """Callback function to process each captured packet.

        Args:
            packet: The captured packet.
        """
        print(packet.summary())

    async def send_massage_async(self, phone_number):
        unique_identifier = uuid.uuid4()
        message = f"Hello from your Python massage carrier! \n\nUnique identifier: {unique_identifier}"

        client = Client("AC60d3a3982129822c06753b25f80d8cd7", "24eee3e8f0c42892f7dd1b243fefd60d")
        client.messages.create(
            to=phone_number,
            from_='+12603442846',
            body=message,
        )

        await asyncio.sleep(5)  # Adjust the timeout as needed

        # Start sniffing with the callback function.
        packets = sniff(prn=self.packet_callback, store=True, timeout=10)
        print(packets)


    async def send_massage1(self,phone_number):
        unique_identifier = uuid.uuid4()
        message = f"Hello from your Python massage carrier! \n\nUnique identifier: {unique_identifier}"

        client = Client("AC60d3a3982129822c06753b25f80d8cd7", "24eee3e8f0c42892f7dd1b243fefd60d")
        client.messages.create(
            to=phone_number,
            from_='+12603442846',
            body=message,
        )

        await asyncio.sleep(5)  # Adjust the timeout as needed

        # Start sniffing with the callback function.
        packets = sniff(prn=lambda pkt: pkt.show(), store=True, timeout=10)
        print(packets)

    def main_menu(self):
        while True:
            self.show_logo()

            print('1: Send SMS')
            print('2: Get IP Addresses')
            print('3: Get info of phone number')
            print('4: packet tracking')
            print('5: packet sniffing')
            print('6: Exit')

            choice = input("\nPlease choose an option: ")

            if choice == "1":
                message = input("Please input the message: ")
                self.send_massage(message)
            elif choice == "2":
                self.trace_network_transmission()
            elif choice == "3":
                self.get_ip_phoneinfo(self.phone_number)
            elif choice == "4":
                asyncio.run(self.send_massage1(self.phone_number))
            elif choice == "5":
                asyncio.run(self.send_massage_async(self.phone_number))
            elif choice == "6":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print(colored('''
   __ __      __ __        _      __      __                        __          ____ ___        ___    ___   __                    __                   __            
  / // /___  / // /___    | | /| / /___  / /____ ___   __ _  ___   / /_ ___    /  _// _ \ ____ / _ \  / _ \ / /  ___   ___  ___   / /  ___  ____ ___ _ / /_ ___   ____
 / _  // -_)/ // // _ \   | |/ |/ // -_)/ // __// _ \ /  ' \/ -_) / __// _ \  _/ / / ___//___// , _/ / ___// _ \/ _ \ / _ \/ -_) / /__/ _ \/ __// _ `// __// _ \ / __/
/_//_/ \__//_//_/ \___/   |__/|__/ \__//_/ \__/ \___//_/_/_/\__/  \__/ \___/ /___//_/        /_/|_| /_/   /_//_/\___//_//_/\__/ /____/\___/\__/ \_,_/ \__/ \___//_/   
                                                                                                                                                                      
''', 'green'))
    phone_number = input("Hello Welcome! Enter the Number Which need to Exploited: ")  # "+918310180317"
    sms_tool = SMSTool(phone_number)
    sms_tool.main_menu()
