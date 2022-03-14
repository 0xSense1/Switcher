import telnetlib
import time

print("\n")
print("""\
   _____         _ _       _
  / ____|       (_) |     | |
 | (_____      ___| |_ ___| |__   ___ _ __
  \___ \ \ /\ / / | __/ __| '_ \ / _ \ '__|
  ____) \ V  V /| | || (__| | | |  __/ |
 |_____/ \_/\_/ |_|\__\___|_| |_|\___|_|


""")
print("\n")
print("This is Python Script which is written by Akbar a.k.a  Decryptor.© 2013.All rights reserved. ")
print("\n")
print("Please Select Which Operation you want to do.")
print("\n")

print("𝟏.Switch port")
print("𝟐.Log File")
print("𝟑.Switch Up-Time")
print("𝟒.Mac-Addresses")
print("𝟓.Vlan Configuration")
print("𝟔.Refresh Port")
print("𝟕.Write Vlan")
print("\n")

user_input = int(input("Enter Only Number 1-7:   "))
print("\n")
if user_input == 1:
    def check_port():
        switch = input("Enter Switch IP Here:  ")
        port = int(input("Specify Port Number:  "))
        print("\n")
        password = 'example'
        username = 'example'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username: ")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully connected to %s" % switch)
        tn.write(b"terminal length 0\n")
        time.sleep(1)
        tn.write(b"sh int fa 0/%d\n" % port)
        time.sleep(1)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Done")

    check_port()

elif user_input == 2:
    def check_log():
        switch = input("Enter switch IP here:  ")
        print("\n")
        password = 'j0hn256w00'
        username = 'gus'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully Connected to %s" % switch)
        tn.write(b"terminal length 0\n")
        tn.write(b"show logging\n")
        time.sleep(1)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Done")


    check_log()


elif user_input == 3:
    def check_version():
        switch = input("Enter switch IP here:  ")
        print("\n")
        password = 'j0hn256w00'
        username = 'gus'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully connected to %s" % switch)
        tn.write(b"show version\n")
        time.sleep(2)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Done")


    check_version()

elif user_input == 4:
    def check_mac():
        switch = input("Enter switch IP here:  ")
        vlan = int(input("Specify Vlan Number:  "))
        print("\n")
        password = 'j0hn256w00'
        username = 'gus'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully connected to %s" % switch)
        tn.write(b"show mac address-table dynamic vlan %d\n" % vlan)
        time.sleep(2)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Done")


    check_mac()

elif user_input == 5:
    def check_vlan_conf():
        switch = input("Enter switch IP here:  ")
        print("\n")
        password = 'j0hn256w00'
        username = 'gus'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully connected to %s" % switch)
        tn.write(b"show run\n")
        time.sleep(2)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Done")


    check_vlan_conf()

elif user_input == 6:
    def refresh_port():
        switch = input("Enter switch IP here:  ")
        ref_port = int(input("Specify Port Number:  "))
        print("\n")
        password = 'j0hn256w00'
        username = 'gus'

        tn = telnetlib.Telnet(switch)
        tn.read_until(b"Username")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password")
        tn.write(password.encode("ascii") + b"\n")
        print("Successfully connected to %s" % switch)
        tn.write(b"conf t\n")
        time.sleep(2)
        tn.write(b"int fa 0/%d\n" % ref_port)
        time.sleep(2)
        tn.write(b"shutdown\n")
        time.sleep(2)
        tn.write(b"no shutdown\n")
        time.sleep(2)
        tn.write(b"exit\n")
        time.sleep(2)
        tn.write(b"exit\n")
        time.sleep(2)
        tn.write(b"sh int fa 0/%d\n" % ref_port)
        time.sleep(2)
        output = tn.read_very_eager().decode('utf-8')
        print(output)
        print("\n")
        print("Look at billing system for AUTH")


    refresh_port()
elif user_input == 7:
    print("1.Write Vlan In the Current Switch")
    print("2.Write Vlan for Other Switch")
    print("3.Untagged Vlan\n")
    choice_write = int(input("Please Choose the Option :"))

    if choice_write == 1:
        def current_vlan():
            switch = input("Enter switch IP here:  ")
            vlan_for_port = int(input("Please write Port Number: "))
            vlan = int(input("Specify Vlan Number:  "))
            print("\n")
            password = 'j0hn256w00'
            username = 'gus'

            tn = telnetlib.Telnet(switch)
            tn.read_until(b"Username")
            tn.write(username.encode("ascii") + b"\n")
            tn.read_until(b"Password")
            tn.write(password.encode("ascii") + b"\n")
            print("Successfully connected to %s" % switch)
            time.sleep(2)
            tn.write(b"vlan database\n")
            time.sleep(3)
            tn.write(b"vlan %d state active\n" % vlan)
            time.sleep(3)
            tn.write(b"exit\n")
            time.sleep(3)
            tn.write(b"conf t\n")
            time.sleep(2)
            tn.write(b"int fa 0/%d\n" % vlan_for_port)
            time.sleep(2)
            tn.write(b"switchport access vlan %d\n" % vlan)
            time.sleep(2)
            tn.write(b"spanning-tree portfast\n")
            time.sleep(2)
            tn.write(b"end\n")
            time.sleep(2)
            tn.write(b"write memory\n")
            time.sleep(5)
            output = tn.read_very_eager().decode('utf-8')
            print(output)
            print("\n")
            print("Vlan Writed Successfuly\n")
            print("Please check billing system for AUTH\n")
        current_vlan()

    elif choice_write == 2:
        def other_vlan():
            switch = input("Enter switch IP here:  ")
            vlan = int(input("Specify Vlan Number:  "))
            print("\n")
            password = 'j0hn256w00'
            username = 'gus'

            tn = telnetlib.Telnet(switch)
            tn.read_until(b"Username")
            tn.write(username.encode("ascii") + b"\n")
            tn.read_until(b"Password")
            tn.write(password.encode("ascii") + b"\n")
            print("Successfully connected to %s\n" % switch)
            tn.write(b"vlan database %d\n" % vlan)
            time.sleep(2)
            tn.write(b"vlan %d state active\n" % vlan)
            time.sleep(2)
            tn.write(b"exit\n")
            time.sleep(2)
            tn.write(b"write memory\n")
            output = tn.read_very_eager().decode('utf-8')
            print(output)
            print("\n")
            print("Vlan Writed Successfuly\n")
            print("Please check billing system for AUTH\n")

        other_vlan()

    elif choice_write == 3:
        def untagged_vlan():
            switch = input("Enter switch IP here:  ")
            vlan_port = int(input("Please write Port Number: "))
            vlan = int(input("Specify Vlan Number:  "))
            print("\n")
            password = 'j0hn256w00'
            username = 'gus'

            tn = telnetlib.Telnet(switch)
            tn.read_until(b"Username")
            tn.write(username.encode("ascii") + b"\n")
            tn.read_until(b"Password")
            tn.write(password.encode("ascii") + b"\n")
            print("Successfully connected to %s\n" % switch)
            tn.write(b"conf t\n")
            time.sleep(2)
            tn.write(b"int fa 0/%d\n" % vlan_port)
            time.sleep(2)
            tn.write(b"Switchport Access vlan %d\n" % vlan)
            time.sleep(2)
            tn.write(b"Spanning-tree portfast\n")
            time.sleep(2)
            tn.write(b"end\n")
            time.sleep(2)
            tn.write(b"write memory\n")
            time.sleep(2)
            tn.write(b"exit\n")
            
            print(type("output"))
            output = tn.read_very_eager().decode('utf-8')
            print(output)
            print("\n")
            print("Vlan Untagged Successfuly\n")
            print("Please check billing system for AUTH\n")

        untagged_vlan()
