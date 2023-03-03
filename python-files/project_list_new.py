# Python 3.6+
# pip(3) install requests
import requests
import os

# Standard headers
HEADERS_AUTH = {"Content-Type": "application/x-www-form-urlencoded"}
HEADERS = {"Content-Type": "application/json"}

client_id = os.getenv('secwiz_clientid')
client_secret = os.getenv('secwiz_clientsecret')

# Uncomment the following section to define the proxies in your environment,
#   if necessary:
# http_proxy  = "http://"+user+":"+passw+"@x.x.x.x:abcd"
# https_proxy = "https://"+user+":"+passw+"@y.y.y.y:abcd"
# proxyDict = {
#     "http"  : http_proxy,
#     "https" : https_proxy
# }

# The GraphQL query that defines which data you wish to fetch.
query = ("""
    query ControlFilterAutosuggest($after: String) {
      controls(first: 500, after: $after) {
        nodes {
          id
          name
          query
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
""")

# The variables sent along with the above query
variables = {}


def query_wiz_api(query, variables):
    """Query WIZ API for the given query data schema"""
    data = {"variables": variables, "query": query}

    try:
        # Uncomment the next first line and comment the line after that
        # to run behind proxies
        # result = requests.post(url="https://api.us16.app.wiz.io/graphql",
        #                        json=data, headers=HEADERS, proxies=proxyDict)
        result = requests.post(url="https://api.us16.app.wiz.io/graphql",
                               json=data, headers=HEADERS)

    except Exception as e:
        if ('502: Bad Gateway' not in str(e) and
                '503: Service Unavailable' not in str(e) and
                '504: Gateway Timeout' not in str(e)):
            print("<p>Wiz-API-Error: %s</p>" % str(e))
            return(e)
        else:
            print("Retry")

    return result.json()


def request_wiz_api_token(client_id, client_secret):
    """Retrieve an OAuth access token to be used against Wiz API"""
    auth_payload = {
      'grant_type': 'client_credentials',
      'audience': 'wiz-api',
      'client_id': client_id,
      'client_secret': client_secret
    }
    # Uncomment the next first line and comment the line after that
    # to run behind proxies
    # response = requests.post(url="https://auth.app.wiz.io/oauth/token",
    #                         headers=HEADERS_AUTH, data=auth_payload,
    #                         proxies=proxyDict)
    response = requests.post(url="https://auth.app.wiz.io/oauth/token", headers=HEADERS_AUTH, data=auth_payload)

    if response.status_code != requests.codes.ok:
        raise Exception('Error authenticating to Wiz [%d] - %s' %
                        (response.status_code, response.text))

    try:
        response_json = response.json()
        TOKEN = response_json.get('access_token')
        if not TOKEN:
            message = 'Could not retrieve token from Wiz: {}'.format(
                    response_json.get("message"))
            raise Exception(message)
    except ValueError as exception:
        print(exception)
        raise Exception('Could not parse API response')
    HEADERS["Authorization"] = "Bearer " + TOKEN

    return TOKEN


def main():

    print("Getting token.")
    request_wiz_api_token(client_id, client_secret)

    result = query_wiz_api(query, variables)
    print(result)  # your data is here!

    # The above code lists the first <x> items.
    # If paginating on a Graph Query,
    #   then use <'quick': False> in the query variables.
    # Uncomment the following section to paginate over all the results:
    # pageInfo = result['data']['controls']['pageInfo']
    # while (pageInfo['hasNextPage']):
    #     # fetch next page
    #     variables['after'] = pageInfo['endCursor']
    #     result = query_wiz_api(query, variables)
    #     print(result)
    #     pageInfo = result['data']['controls']['pageInfo']


if __name__ == '__main__':
    main()