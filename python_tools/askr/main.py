import requests_async as requests
import asyncio
from collections import Counter
from json import dumps

expected_hosts = {'nodo1', 'nodo2', 'nodo3'}
url_check = "https://cookiedwebsite.com"
jids_list = []
# counter_dict = {host: 0 for host in expected_hosts}
counter_dict = {}
header = r"""
 _______ _______ __  __ ______ 
|   _   |     __|  |/  |   __ \
|       |__     |     <|      <
|___|___|_______|__|\__|___|__|
                               

"""


async def do_call():
    async with requests.Session() as session:
        response = await session.get(url_check, timeout=10)
        jsess = response.cookies.get_dict()
        # print(jsess.get('JSESSIONID'))
        jids_list.append(jsess.get('JSESSIONID').split('.')[1])

async def main():
    checks = []
    for n_req in range(10):
        await do_call()

if __name__ == "__main__":
    print(header, f"\n\nURL consultada { url_check }\nComprobando balanceo... \n")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # counter_dict = {host: counter_dict.get(host, 0) + 1 for host in expected_hosts for jid in jids_list}
    #for jid in jids_list:
    #    for host in expected_hosts: 
    #        if host in jids_list:
    #           counter_dict[host] = counter_dict.get(host) + 1 
    # print(Counter(jids_list))
    final_list = Counter(jids_list)
    print(dumps(final_list, indent=4, sort_keys=True))
    nodos_culpables = list(expected_hosts - set(final_list.keys()))
    print(f"\nNodos sin respuesta: {nodos_culpables}")
    # print(nodos_culpables)
