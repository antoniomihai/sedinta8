from scrapli_netconf.driver import NetconfDriver

my_device = {
  "host":"10.5.1.225",
  "auth_username":"student",
  "auth_password":"cisco",
  "auth_strict_key":False,
  "port":830
}

conn = NetconfDriver(**my_device)
conn.open()

rpc_filter="""
<get>
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
            <interface>
                <name></name>
            </interface>
        </interfaces>
    </filter>
</get>
"""

response = conn.rpc(rpc_filter)
print(response.result)