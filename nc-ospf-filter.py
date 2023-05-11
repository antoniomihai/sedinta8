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

ospf_filter="""
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state>
        <ospf-instance>
          <af>address-family-ipv4</af>
          <router-id>2886755332</router-id>
          <ospf-area>
            <area-id>0</area-id>
                <ospf-interface>
                    <name>GigabitEthernet2</name>
                    <ospf-neighbor>
                        <neighbor-id></neighbor-id>
                        <state></state>
                    </ospf-neighbor>
                </ospf-interface>
          </ospf-area>
        </ospf-instance>     
    </ospf-state>
</ospf-oper-data>
"""

response = conn.get(
    filter_ = ospf_filter, filter_type='subtree'
)
print(response.result)